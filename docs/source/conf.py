# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from pathlib import Path
import os
import sys

sys.path.insert(0, os.path.abspath("."))
from datetime import datetime
# from overlap_check import __version__ as version


sys.path.insert(0, os.path.abspath('../../overlap_check'))

# -- Project information -----------------------------------------------------

project = 'overlap-check'
copyright = '2022, Mahdi Sadeghi'
author = 'Sadeghi'

# The full version, including alpha/beta/rc tags
# release = version.__version__
release = "0.0.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
default_role = "py:obj"

extensions = [
    "sphinx_panels",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_click.ext",
    "sphinx-jsonschema",
    "sphinxemoji.sphinxemoji",
    "sphinx_copybutton",
    "sphinxcontrib.yt",
    "versionwarning.extension",
    #"sphinx_sitemap",
    "myst_nb",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.autosummary",
    #"sphinx_external_toc",
    "sphinx_thebe",
    "sphinxcontrib.autodoc_pydantic",
]
extensions.append('autoapi.extension')

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
]

autoapi_type = 'python'
autoapi_dirs = ['../../overlap_check']
# Python methods should be presented in source code order
# autodoc_member_order = "bysource"
# autodoc_typehints = 'signature'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "repository_url": "https://github.com/Milad-diconium/Rect_Over",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "doc/source",
    "home_page_in_toc": False,
    "show_navbar_depth": 0,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
