"""Read settings from config/config.ini.

Keeping settings in one file means a test never hard-codes a URL,
a timeout, or a demo credential. Change the config, not the tests.
"""

import configparser
import os

_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "config",
    "config.ini",
)

_parser = configparser.ConfigParser()
_parser.read(_CONFIG_PATH)


def get(section, key, fallback=None):
    return _parser.get(section, key, fallback=fallback)


def getint(section, key, fallback=0):
    return _parser.getint(section, key, fallback=fallback)


def getboolean(section, key, fallback=False):
    return _parser.getboolean(section, key, fallback=fallback)
