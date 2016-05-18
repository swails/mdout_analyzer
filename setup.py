
from distutils.core import setup
import os
import sys

# First the ParmedTools packages:
packages = ['mdoutanalyzer']

modules = []

# Scripts
scripts = ['mdout_analyzer.py']

if __name__ == '__main__':
    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
        PY3 = True
    except ImportError:
        from distutils.command.build_py import build_py
        from distutils.command.build_scripts import build_scripts
        PY3 = False

    setup(name='mdout_analyzer',
          version='0.1',
          description='Analyzes Mdout files from Amber simulations',
          author='Jason Swails',
          author_email='jason.swails -at- gmail.com',
          url='http://ambermd.org',
          license='GPL v2 or later',
          packages=packages,
          py_modules=modules,
          cmdclass={'build_py': build_py, 'build_scripts': build_scripts},
          scripts=scripts)
