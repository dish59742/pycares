#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re

from setuptools import setup
from setup_cares import cares_build_ext


def get_version():
    return re.search(r"""__version__\s+=\s+(?P<quote>['"])(?P<version>.+?)(?P=quote)""", open('pycares/_version.py').read()).group('version')


setup(name             = 'pycares',
      version          = get_version(),
      author           = 'Saúl Ibarra Corretgé',
      author_email     = 's@saghul.net',
      url              = 'http://github.com/saghul/pycares',
      description      = 'Python interface for c-ares',
      long_description = codecs.open('README.rst', encoding='utf-8').read(),
      platforms        = ['POSIX', 'Microsoft Windows'],
      classifiers      = [
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      cmdclass         = {'build_ext': cares_build_ext},
      setup_requires   = ['cffi>=1.5.0'],
      install_requires = ['cffi>=1.5.0'],
      cffi_modules     = ['pycares/_cfficore/pycares_build.py:ffi'],
      packages         = ['pycares', 'pycares._cfficore']
)
