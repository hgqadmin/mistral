# Copyright 2014 - Mirantis, Inc.
# Copyright 2015 - StackStorm, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistral.workbook import types
from mistral.workbook.v2 import base
from mistral.workbook.v2 import policies


class TaskDefaultsSpec(base.BaseSpec):
    # See http://json-schema.org
    _task_policies_schema = policies.PoliciesSpec.get_schema(
        includes=None)

    _schema = {
        "type": "object",
        "properties": {
            "retry": policies.RETRY_SCHEMA,
            "wait-before": policies.WAIT_BEFORE_SCHEMA,
            "wait-after": policies.WAIT_AFTER_SCHEMA,
            "timeout": policies.TIMEOUT_SCHEMA,
            "pause-before": policies.PAUSE_BEFORE_SCHEMA,
            "concurrency": policies.CONCURRENCY_SCHEMA,
            "on-complete": types.UNIQUE_STRING_OR_YAQL_CONDITION_LIST,
            "on-success": types.UNIQUE_STRING_OR_YAQL_CONDITION_LIST,
            "on-error": types.UNIQUE_STRING_OR_YAQL_CONDITION_LIST
        },
        "additionalProperties": False
    }

    @classmethod
    def get_schema(cls, includes=['definitions']):
        return super(TaskDefaultsSpec, cls).get_schema(includes)

    def __init__(self, data):
        super(TaskDefaultsSpec, self).__init__(data)

        self._policies = self._group_spec(
            policies.PoliciesSpec,
            'retry',
            'wait-before',
            'wait-after',
            'timeout',
            'pause-before',
            'concurrency'
        )
        self._on_complete = self._as_list_of_tuples("on-complete")
        self._on_success = self._as_list_of_tuples("on-success")
        self._on_error = self._as_list_of_tuples("on-error")

    def validate(self):
        super(TaskDefaultsSpec, self).validate()

        # Validate YAQL expressions.
        [self.validate_yaql_expr(transition)
         for transition in (self._data.get('on-complete', []) +
                            self._data.get('on-success', []) +
                            self._data.get('on-error', []))
         if isinstance(transition, dict)]

    def get_policies(self):
        return self._policies

    def get_on_complete(self):
        return self._on_complete

    def get_on_success(self):
        return self._on_success

    def get_on_error(self):
        return self._on_error
