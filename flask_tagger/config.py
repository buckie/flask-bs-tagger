import os

REPO_NAME = "flask-tagger"  # Used for FREEZER_BASE_URL

# settings used in development
DEBUG = True
HOST = 'localhost'
PORT = 5000  # Over 9000!

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = APP_DIR
FREEZER_DESTINATION = os.path.join(os.path.dirname(PROJECT_ROOT), 'gh-pages')
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = True  # IMPORTANT: If this is True, all app files
