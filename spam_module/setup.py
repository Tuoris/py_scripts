from distutils.core import setup, Extension

spam_module = Extension('spam', sources=['spammodule.c'])

setup(name='spam_module',
      version='0.1',
      description='An Example For Python C Extensions',
      ext_modules=[spam_module],
      )
