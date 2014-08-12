# compiler
FC      := gfortran

# compiler flags
FCFLAGS = 
# link flags
FLFLAGS =

# source files and objects
SRCS = $(patsubst %.f, %.o, $(wildcard *.f))
#       $(patsubst %.h, %.mod, $(wildcard *.h))

# program name
PROGRAM = genunformatted

all: $(PROGRAM)

$(PROGRAM): $(SRCS)
	$(FC) $(FLFLAGS) -o $@ $^

%.o: %.F
	$(FC) $(FCFLAGS) -o $@ $<

# %.mod: %.h
# $(FC) $(FCFLAGS) -o $@ $<

clean:
	rm -f *.o *.mod $(PROGRAM) llp.fdt stga.fdt
