# Copyright 2014 - Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
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

from oslo.config import cfg

from mistral import context as auth_context


# Make sure to import 'auth_enable' option before using it.
cfg.CONF.import_opt('auth_enable', 'mistral.config', group='pecan')


CONF = cfg.CONF
DEFAULT_PROJECT_ID = "<default-project>"


def get_project_id():
    if CONF.pecan.auth_enable and auth_context.has_ctx():
        return auth_context.ctx().project_id
    else:
        return DEFAULT_PROJECT_ID
