# -*- makefile -*-
.PHONY: all clean


#F2PY = f2py --fcompiler=gfortran
F2PY = f2py
F2PY_FLAGS = --f77flags=-ffixed-line-length-132

MODULE=gamman

all: ${MODULE}.so

${MODULE}.so: ${MODULE}.f
	${F2PY} ${F2PY_FLAGS} -c ${MODULE}.pyf ${MODULE}.f

clean:
	${RM} ${MODULE}.so

