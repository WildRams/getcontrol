# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys

import sphinx_nefertiti

if 'READTHEDOCS' in os.environ:
    html_theme_path = [sphinx_nefertiti.get_html_theme_path()]
else:
    # Add `sphinx_nefertiti` to the python path.
    PRJ_PATH = Path(__file__).parents[2]
    sys.path.insert(0, str(PRJ_PATH))
    html_static_path = ['_static/']

# -- Project information ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GetControl'
author = 'Přemysl (Premek) Beran'
copyright = '2011-2025, WildRam'

version = '0.9.2.4'
release = version

language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
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

source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
suppress_warnings = ['image.nonlocal_uri']

numfig = False

show_authors = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

release_pattern_url = 'https://github.com/wildrams/getcontrol/releases/tag/v{release}/'
releases = [
    release,
    '0.9.0.1',
    '0.8.0.1',
    '0.7.2.1',
    '0.7.1.1'
]

html_context = {}

html_show_sourcelink = False
html_favicon = "_static/img/favicon.ico"

html_theme = "sphinx_nefertiti"
html_theme_options = {
    "documentation_font": "Open Sans",
    "documentation_font_size": "1.0rem",
    "monospace_font": "Andale Mono",
    "monospace_font_size": "1.0rem",

    "style": "blue",

    "logo": "img/getcontrol.svg",
    "logo_alt": "GetControl",

    "pygments_light_style": "pastie",
    "pygments_dark_style": "dracula",

    "repository_url": "https://github.com/wildrams/getcontrol",
    "repository_name": "wildrams/getcontrol",

    "current_version": f"v{release}",
    "versions": [
        ("v%s" % item, release_pattern_url.format(release=item))
        for item in releases
    ],

    'header_links': [
        {'text': 'Home', 'link': 'index'},
        {'text': 'Documentation', 'link': 'documentation/introduction'},
        {'text': 'What is new','link': 'documentation/changelog'},
    ],

    "footer_links": [
        {'text':'Documentation', 'link':'https://wildrams.github.io/getcontrol'},
        {'text':'Download', 'link':'https://github.com/wildrams/getcontrol/releases/latest'},
        {'text':'Repository', 'link':'https://github.com/wildrams/getcontrol'},
    ],

    "show_colorset_choices": False
}

# -- Options for HTMLHelp output ---------------------------------------

htmlhelp_basename = 'sphinx_nefertitidoc'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {}
latex_documents = [
    (master_doc, 'GetControl-manual.tex',
     'GetControl - Documentation',
     'WildRam', 'manual'),
]

# -- Options for manual page output ------------------------------------

man_pages = [
    (master_doc, 'sphinx_nefertiti',
     'Nefertiti for Sphinx - Documentation',
     ['Daniela Rus Morales'], 1)
]
