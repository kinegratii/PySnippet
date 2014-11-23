#coding=utf8
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

RESOUCE_DIR  = os.path.join(BASE_PATH, 'resource')

VERSION = 'v1.0.3'

APP_NAME = 'Minesweeper'

APP_FULL_NAME = '{name} {version}'.format(name=APP_NAME, version=VERSION)

GITHUB_HOME = 'https://github.com/kinegratii/PySnippet/tree/master/minesweeper'
