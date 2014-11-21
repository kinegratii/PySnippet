#code=UTF-8
from distutils.core import setup
import py2exe

options = {'py2exe':{'compressed':1,
                     'optimize':2,
                     'bundle_files':1,}}

setup(name = 'nms_config',
      author = 'zhenwei.yan',
      author_email = 'zhenwei.yan@hengjiatech.com',
      version = '1.0.0',
      url = 'www.hengjiatech.com',
      options = options,
      windows=[{"script":"nms_config.py"}],
      zipfile = None
      )
