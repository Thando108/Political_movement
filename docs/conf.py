import os
import sys
import django

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('..'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'political_movement.settings'
django.setup()

# -- Project information -----------------------------------------------------

project = 'Political Movement'
author = 'Thando'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
