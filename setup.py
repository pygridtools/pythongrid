# installation scripts based on these:
# http://www.scotttorborg.com/python-packaging/minimal.html
# http://packages.python.org/distribute/setuptools.html

from setuptools import setup

def readme():
    with open('README.md') as f:
       return f.read()

setup(name='pythongrid',
      version='0.1',
      description='High-level python wapper for the Sun Grid Engine (SGE) using DRMAA and ZMQ',
      long_description=readme(),
      keywords='drmaa sge cluster distributed parallel',
      url='http://code.google.com/p/pythongrid/',
      author='Chris Widmer',
      author_email='cwidmer@cbio.mskcc.org',
      license='GPL',
      packages=['pythongrid'],
      #py_modules=['pythongrid', 'pythongrid_cfg'],
      install_requires=['drmaa', 'pyzmq'],
      zip_safe=False)
