#!/usr/bin/env python

from distutils.core import setup

setup(name='Chess',
      version='1.0',
      description='Chess game',
      author='Brandon Shimanek',
      url='Na',
      packages=['chess', 'chess.app', 'chess.app.controller',
                'chess.app.view'],
      entry_points={
            'console_scripts': ['chess = chess.app.__main__:main']
          }
      )
