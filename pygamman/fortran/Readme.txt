
						         GAMMA-N

		 			A PACKAGE OF NEUTRAL DENSITY ROUTINES
	

		   			 David Jackett and Trevor McDougall


		     			CSIRO Division of Marine Research
		        GPO Box 1538, Hobart, Tasmania, 7001, Australia


			     			   Version 3.1
			      			  January, 1997



This directory contains FORTRAN code which enables the user to label
arbitrary hydrographic data with neutral density (subroutine gamma_n), and
subsequently find the positions of specified neutral density surfaces on a
cast of hydrographic data (subroutine neutral_surfaces). Complete details
of the algorithms used in the package can be found in 'A neutral density
variable for the world's oceans' by D.R. Jackett and T.J. McDougall,
Journal of Physical Oceanography, Vol.27(2) 1997, 237-263.

Two executable files have been included suitable for compilation of the
library on a PC under Microsoft Fortran Version 5.1: 'make_lib.bat' will
compile the complete library while 'csub.bat' will compile a single routine.
An example of labelling and the fitting of neutral density surfaces to a
cast of data can be found in the file 'example.for', the output of which can
be compared to the file 'example.out'. This program can be compiled by 
typing 'cprog example' at a DOS prompt.

In principle this same code should compile on machines other than a PC with
FORTRAN compilers other than Microsoft. This version of the code does not
use the NETCDF data archiving library but rather random access files, so if
you are compiling this on a machine other than a PC or using a different
compiler you may need to generate the random access files in the gamma_n/data
directory - there are instructions there to assist with this.

The gamma_n code will stop if you give it a cast whose longitude or
latitude is outside the range of the data set, namely [0,360]x[-80,64].
Also, bottle data outside the range of validity of the present equation of
state do not label, returning with a gamma value of -99.1.

The code sometimes does not successfully label a bottle, in which case it
returns with a value of -99.0. This could be caused by it being extremely
dense data, or it could be due to 'triple solutions' (currently being
investigated).

The neutral_surfaces code expects all bottles on the cast to be labelled,
so if your data contains -99's after labelling, these will need to be
eliminated from the input to this routine.

The neutral_surface code does, on occasions, detect the existence of more
than one solution (sns,tns,pns) for particular input neutral surfaces.
In this case, the code returns with sns, tns and pns values corresponding
to the middle crossing, and dsns, dtns and dpns values giving the possible
error in this crossing. Also the file 'ns-multi.dat' is written, containing
all relevant information on the multiply defined surfaces. Specifically, for
each surface which is not uniquely defined, the file contains a line
containing (isfce = surface #, ncr = # crossings) and then ncr lines
containing the ncr (sns,tns,pns) triples. This situation arises when the
user's data is statically unstable. In many of these cases, particularly
when such a cast comes from a section of data with well defined surfaces on
neighbouring casts, the 'ns-multi.dat' file can be inspected to make an
objective choice of the most appropriate crossing.

There are several ERROR and WARNING messages that can be produced by this
software (most of them low level): descriptions of these messages, should
they occur, can be found in gamma.errors.

Details of the calling sequences of the two top level routines follow.
Similar descriptions can be found on all routines written by the first
author. 

We are keen to hear of your experiences with the package, and of any problems
that you encounter. If you do install the code on your machine and use it or
intend using it in the future, would you please drop a short line to either 
jackett@ml.csiro.au or mcdougal@ml.csiro.au saying so, and perhaps indicating
your particular application. In the likely event that there are updates to 
the code, such a list of users will enable us to alert you to the 
availability of the updates and indicate any improvements we have made to
the algorithms.

Finally, we have included a ConditionsOfUse file, which should be read prior
to using the code.




        subroutine gamma_n(s,t,p,n,along,alat,gamma,dg_lo,dg_hi)
ccc
ccc
ccc
ccc DESCRIPTION:   	Label a cast of hydrographic data at a specified 
ccc                 location with neutral density
ccc
ccc PRECISION:     	Single
ccc
ccc INPUT:  	    s(n)        array of cast salinities
ccc                 t(n)        array of cast in situ temperatures
ccc                 p(n)        array of cast pressures
ccc                 n           length of cast (n=1 for single bottle)
ccc                 along       longitude of cast (0-360)
ccc                 alat        latitude of cast (-80,64)
ccc
ccc OUTPUT:        	gamma(n)    array of cast gamma values
ccc                 dg_lo(n)    array of gamma lower error estimates
ccc                 dg_hi(n)    array of gamma upper error estimates
ccc
ccc                 NOTE:       -99.0 denotes algorithm failed
ccc                             -99.1 denotes input data is outside
ccc                             the valid range of the present
ccc                             equation of state
ccc
ccc UNITS:         	salinity    psu (IPSS-78)
ccc                 temperature degrees C (IPTS-68)
ccc                 pressure    db
ccc                 gamma       kg m-3
ccc
ccc
ccc AUTHOR:        	David Jackett
ccc
ccc CREATED:       	July 1993
ccc
ccc REVISION:      	3.1     23/1/97
ccc
ccc
ccc





		subroutine neutral_surfaces(s,t,p,gamma,n,glevels,ng,
     &								sns,tns,pns,dsns,dtns,dpns)
ccc
ccc
ccc
ccc	DESCRIPTION:	For a cast of hydrographic data which has been 
ccc					labelled with the neutral density variable gamma,
ccc					find the salinities, temperatures and pressures
ccc					on ng specified neutral density surfaces.
ccc
ccc	PRECISION:		Single
ccc
ccc	INPUT:			s(n)		array of cast salinities
ccc					t(n)		array of cast in situ temperatures
ccc					p(n)		array of cast pressures
ccc					gamma(n)	array of cast gamma values
ccc					n			length of cast
ccc					glevels(ng)	array of neutral density values
ccc					ng			number of neutral density surfaces
ccc
ccc	OUTPUT:			sns(ng)		salinity on the neutral density surfaces
ccc					tns(ng)		in situ temperature on the surfaces
ccc					pns(ng)		pressure on the surfaces
ccc					dsns(ng)	surface salinity errors
ccc					dtns(ng)	surface temperature errors
ccc					dpns(ng)	surface pressure errors
ccc
ccc					NOTE:		sns, tns and pns values of -99.0
ccc								denotes under or outcropping
ccc
ccc								non-zero dsns, dtns and dpns values
ccc								indicates multiply defined surfaces,
ccc								and file 'ns-multiples.dat' contains
ccc								information on the multiple solutions
ccc
ccc	UNITS:			salinity	psu (IPSS-78)
ccc					temperature	degrees C (IPTS-68)
ccc					pressure	db
ccc					gamma		kg m-3
ccc
ccc
ccc	AUTHOR:			David Jackett
ccc
ccc	CREATED:		July 1993
ccc
ccc	REVISION:		3.1		25/1/95
ccc
ccc
ccc

