from distutils.core import setup, Extension

module1 = Extension('libsay', sources = ['say.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'says stuff',
       ext_modules = [module1])

