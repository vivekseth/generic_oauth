from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='generic_oauth',
      version='0.1',
      description='generic_oauth makes it extremely simple to use any OAuth v2 API purely from the command line.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='oauth api google facebook spotify github',
      url='http://github.com/vivekseth/generic_oauth',
      author='Vivek Seth',
      author_email='viveksethm@example.com',
      license='MIT',
      packages=['generic_oauth'],
      install_requires=['requests']
      )
