import os


REPO_NAME = ""  # Used for FREEZER_BASE_URL

# settings used in development
DEBUG = True
HOST = 'localhost'
PORT = 5000  # Over 9000!

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))


def get_extra_watch_files(app_dir, extra_dirs):
    extra_dirs = [os.path.join(app_dir, extra) for extra in extra_dirs]
    extra_files = []
    extra_files += extra_dirs
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)
    return extra_files


def parent_dir(path):
    """
    Return the parent of a directory.
    """
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = APP_DIR
FREEZER_DESTINATION = os.path.join(os.path.dirname(PROJECT_ROOT), 'build')
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = True  # IMPORTANT: If this is True, all app files
