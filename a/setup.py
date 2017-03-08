from distutils.core import setup, Extension

module1 = Extension('libgpio', sources = ['gpio.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'turns stuff on',
       ext_modules = [module1])

