# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))
# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.pecanwsme.rest',
    'sphinxcontrib.httpdomain',
    'wsmeext.sphinxext',
    'openstackdocstheme',
    'oslo_policy.sphinxext',
    'oslo_policy.sphinxpolicygen',
]

wsme_protocols = ['restjson']

suppress_warnings = ['app.add_directive']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Mistral'
copyright = u'2014, Mistral Contributors'

policy_generator_config_file = \
    '../../tools/config/policy-generator.mistral.conf'
sample_policy_basename = '_static/mistral'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
from mistral.version import version_info
release = version_info.release_string()
version = version_info.version_string()

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_static_path = ['_static']

html_theme = 'openstackdocs'

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['mistral.']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'
# Must set this variable to include year, month, day, hours, and minutes.
html_last_updated_fmt = '%Y-%m-%d %H:%M'

# The name for this set of Sphinx documents. If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Mistral'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': [
        'sidebarlinks.html', 'localtoc.html', 'searchbox.html',
        'sourcelink.html'
    ],
    '**': [
        'localtoc.html', 'relations.html',
        'searchbox.html', 'sourcelink.html'
    ]
}

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'mistral', u'Mistral',
     [u'OpenStack Foundation'], 1)
]

# If true, show URL addresses after external links.
man_show_urls = True

# -- Options for openstackdocstheme -------------------------------------------
repository_name = 'openstack/mistral'
bug_project = 'mistral'
bug_tag = ''

latex_use_xindy = False

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [
    ('index', 'doc-mistral.tex',
     u'Mistral Documentation',
     u'OpenStack','manual', True),
]

latex_elements = {
    'makeindex': '',
    'printindex': '',
    'preamble': r'\setcounter{tocdepth}{3}',
}
