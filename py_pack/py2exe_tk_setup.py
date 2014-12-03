#code=UTF-8
from distutils.core import setup
import py2exe

options = {'py2exe':{'compressed':1,
                     'optimize':2,
                     'bundle_files':1,}}

setup(name = 'tk_demo',
      author = 'kinegratii',
      author_email = 'kinegratii@gmail.com',
      version = '1.0.0',
      options = options,
      windows=[{"script":"tk_demo.py"}],
      zipfile = None
      )
