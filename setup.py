import os
import sys
import fileinput
import shutil
import site
import platform
#from setuptools.command.install import install
from distutils.command.install import install
from distutils.command.build import build
from subprocess import call
# get some sys info
from sys import version
from numpy.distutils.core import setup, Extension
#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup


DESCRIPTION = "Python wrapper for preTEOS-10 neutral density"
LONG_DESCRIPTION = open('README.md').read()
NAME = "pygamman"
AUTHOR = "Guido"
AUTHOR_EMAIL = "2guido@gmail.com"
MAINTAINER = "Guido"
MAINTAINER_EMAIL = "2guido@gmail.com"
URL = 'http://github.com/guidov/pygamman'
DOWNLOAD_URL = 'http://github.com/guidov/pygamman'
LICENSE = 'BSD 3-clause'
VERSION = '0.1'
INSTALL_REQ = ['numpy']
wrapper = Extension('gamman',
       sources=['pygamman/fortran/gamman.pyf','pygamman/fortran/gamman.f'],
       extra_f77_compile_args=["-ffixed-line-length-132"])

# Build fortran program to create fortran unformatted ocn data (in fortran/ocndata)
BASEPATH = os.path.dirname(os.path.abspath(__file__))
GENUNF_PATH = os.path.join(BASEPATH, 'pygamman/fortrandata')

class build_genunf(build):
    def run(self):
        # run original build code
        build.run(self)

        # build 
        print 'running Makefile (in fortran/data)'

        build_path = os.path.abspath(self.build_temp)
	def clean():
	    cmd=['make']
            options = ['clean']
            cmd.extend(options)
	    call(cmd, cwd=GENUNF_PATH)
        self.execute(clean, [], 'make clean')

	def make():
	    call(['make'], cwd=GENUNF_PATH)
        self.execute(make, [], 'make genunformatted')

	def rungenunf():
	    call(['./genunformatted'], cwd=GENUNF_PATH)
        self.execute(rungenunf, [], 'run genunformatted')


# Replace the fortran path of ocndata to sys.prefix/egg_name/ocndata 
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

#
#   determine package parameters:
#       package version, python version, os version, architecture
#

# python version
python_version = "py" + str(sys.version_info[0]) + "." + str(sys.version_info[1])

# os version
uname = platform.uname()
#os_version = "unknown-x.x"
os_version = uname[0].lower()
arch = platform.uname()[4]
#eggext = ".egg"
#pkg_name = "-".join([NAME, VERSION, python_version, os_version, arch])
eggext = ".egg-info"
pkg_name = "-".join([NAME, VERSION])
egg_name = pkg_name+eggext
print "Egg name:",egg_name

#ocndataprefix=site.getsitepackages()[0]+"/"+egg_name+"/ocndata/"
ocndataprefix=site.getsitepackages()[0]+"/pygamman/ocndata"
shutil.copy2('pygamman/fortran/gamman_nodata.f', 'pygamman/fortran/gamman.f')
replaceAll("pygamman/fortran/gamman.f","OCNDATAPATH",str(ocndataprefix))


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['pygamman'],
      package_dir={'pygamman':'pygamman','pygamman/ocndata':'pygamman'},
     data_files=[('pygamman/ocndata',['pygamman/fortrandata/llp.fdt','pygamman/fortrandata/stga.fdt']),('pygamman',[BASEPATH+'/gamman.so'])],
      ext_modules = [wrapper],
      cmdclass={'build':build_genunf,'install':install},
      classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: >2.6']
      )

