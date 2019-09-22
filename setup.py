from setuptools import setup
exec(open('keras_squeezenet/version.py').read())
setup(name='keras_squeezenet2',
      version=__version__,
      description='Squeezenet implementation for tensorflow2',
      url='https://github.com/daviddexter/keras-squeezenet2',
      author='DavidDexter',
      author_email = "dmwangimail@gmail.com",
      license='MIT',
      packages=['keras_squeezenet2'],
      zip_safe=False,
      install_requires=['tensorflow==2.0.0-rc1',                   
                        'pyyaml'])
