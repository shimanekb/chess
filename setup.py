from setuptools import setup

setup(name='chess-cli-bshio',
      version='0.0.1',
      author='Brandon Shimanek',
      author_email='brandon.j.shimanek@gmail.com',
      description='Cli game of chess',
      long_description='Cli game of chess',
      url='https://github.com/shimanekb/chess',
      packages=['chess.set', 'chess.app'],
      entry_points={
            'console_scripts': ['chess = chess.app.__main__:main']
          },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          ],
      )
