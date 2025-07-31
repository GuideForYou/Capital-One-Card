# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Capital One Card Guide'
copyright = '2025, Capital One'
author = 'Capital One Documentation Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

html_title = "How to Log In & Pay Your Capital One Credit Card Bill – Complete Guide"
html_short_title = "Capital One Card Help"
html_favicon = 'favicon.ico'

# Theme selection (optional)
# html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = False
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Template and static paths
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have static assets

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
