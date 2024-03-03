# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys

import sphinx_nefertiti


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme_path = [sphinx_nefertiti.get_html_theme_path()]
else:
    # Add `sphinx_nefertiti` to the python path.
    PRJ_PATH = Path(__file__).parents[2]
    sys.path.insert(0, str(PRJ_PATH))
from sphinx.locale import _

project = 'GetControl'
copyright = '2011-2024, WildRam'
author = 'Přemysl (Premek) Beran'
release = '0.8.0.1'
version = '0.8.0.1'
author = 'WildRam'
copyright = author
language = 'en'
email_automode = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

myst_enable_extensions = [
    'amsmath',
    'attrs_block',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'tasklist',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

language = "en"

html_theme = "sphinx_nefertiti"

if not 'READTHEDOCS' in os.environ:
    html_static_path = ['_static/']

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = "pastie"
pygments_dark_style = "dracula"

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']

release_pattern_url = 'https://github.com/wildrams/getcontrol/releases/tag/v{release}/'
releases = [
    release,
    '0.7.2.1',
    '0.7.1.1',
    '0.7.0.1'
]

html_context = {}

html_show_sourcelink = False
html_favicon = "_static/img/favicon.ico"

html_theme_options = {
    "documentation_font": "Open Sans",
    "documentation_font_size": "1.1rem",
    "monospace_font": "Ubuntu Mono",
    "monospace_font_size": "1.2rem",

    "style": "blue",

    "logo": "img/getcontrol.svg",
    "logo_alt": "GetControl",

    "repository_url": "https://github.com/wildrams/getcontrol",
    "repository_name": "wildrams/getcontrol",

    "current_version": f"v{release}",
    "versions": [
        ("v%s" % item, release_pattern_url.format(release=item))
        for item in releases
    ],

    "footer_links": ",".join([
        "Documentation|https://wildrams.github.io/getcontrol",
        "Download|https://github.com/wildrams/getcontrol/releases/latest",
        "Repository|https://github.com/wildrams/getcontrol",
    ]),

    "show_colorset_choices": False
}

# -- Options for HTMLHelp output ---------------------------------------

htmlhelp_basename = 'sphinx_nefertitidoc'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {}
latex_documents = [
    (master_doc, 'sphinx_nefertiti.tex',
     'Nefertiti for Sphinx - Documentation',
     'Daniela Rus Morales', 'manual'),
]

# -- Options for manual page output ------------------------------------

man_pages = [
    (master_doc, 'sphinx_nefertiti',
     'Nefertiti for Sphinx - Documentation',
     ['Daniela Rus Morales'], 1)
]
