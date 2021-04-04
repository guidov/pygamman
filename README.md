The python package install does not seem to work.
For the simple f2py wrapper see: https://github.com/guidov/pygamman_f2py

pygamman: Python interface to PreTEOS-10 neutral density fortran code
================================================================================================

Jackett, David R., Trevor J. McDougall, 1997: A Neutral Density Variable for the World's Oceans. J. Phys. Oceanogr., 27, 237–263. doi: 10.1175/1520-0485(1997)0272.0.CO;2

- Author: 
- License: BSD 3-clause

See:
http://www.teos-10.org/preteos10_software/neutral_density.html


About
-----
Neutral Density surfaces are the most natural layer interfaces stratifying the deep ocean circulation. Neutral Density arises as the continuous analogue of discretely defined locally-referenced potential density surfaces, surfaces which have long been recognised as the most sophisticated for deep ocean density stratification. To account for the compressible nature of sea-water, neutral density is a function of both hydrography and geographical position, and as such is much simpler to use than the cumbersome potential density surface method currently in use.

The Neutral Density code comes as a package of FORTRAN routines which enable the user to fit neutral density surfaces to arbitrary hydrographic data. The FORTRAN implementation consists of a FORTRAN subroutine which labels a cast of hydrographic data with neutral density, and another subroutine which then finds the positions of specified neutral density surfaces within the water column. All code comes with documentation in the form of Readme files, as well as Makefiles and examples to provide check values for the user.



Installation (only tested on Ubuntu 14.04 with gcc 4.8.2 and numpy 1.9.0)
----------------------------------------------------------------------------------------------
Requires f2py, gfortran (or other fortran compiler)
 

*********************NOTE*********************************
There is a problem with the order of the compilation of the fortran module and data files and the order of the python module installation.

With the current version of the code the install command has to be run twice (or build then install) for the data and wrapped library to be installed to python lib directory correctly
**********************************************************

You can build the package locally using

    [~]$ python setup.py build

or install the package to the standard Python path using:

    [~]$ python setup.py install

Or, to install to another location, use

    [~]$ python setup.py install --prefix=/path/to/location/

Then make sure your PYTHONPATH environment variable points to this location.


Trying it out
-------------
See examples and notebook directory


Known Problems and TODO:
------------------------
1) Geting this message on calculation of gamma_n on CTD
 WARNING 1 in goor-solve.f

 Solution: ignore warning

2) Getting error which kills the python interpreter (also in the ipython notebook)
 ERROR 1 in gamma-n.f : out of oceanographic range

 Solution: Routine will not work for latitudes < 80S and > 64N



