FC = gfortran
FCFLAGS = -g -c -fdefault-real-8 -fPIC -fno-second-underscore -fbacktrace -fno-align-commons -fbounds-check -std=legacy
LDFLAGS =

MODDIR := .mod
ifneq ($(MODDIR),)
  $(shell test -d $(MODDIR) || mkdir -p $(MODDIR))
  FCFLAGS+= -J $(MODDIR)
endif

SRCS =  MOM_io.F90 MOM_error_handler.F90 pkg/MOM6/src/ALE/polynomial_functions.F90\
	pkg/MOM6/src/framework/MOM_string_functions.F90\
	pkg/MOM6/src/ALE/regrid_solvers.F90 pkg/MOM6/src/ALE/regrid_edge_values.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/P1M_functions.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/PCM_functions.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/P3M_functions.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/PLM_functions.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/PPM_functions.F90\
	pkg/MOM6/src/ALE/regrid_consts.F90 pkg/MOM6/src/ALE/PQM_functions.F90\
	pkg/MOM6/src/ALE/regrid_interp.F90 pkg/MOM6/src/ALE/MOM_remapping.F90


OBJECTS = $(SRCS:.F90=.o)
TARGET = libALE.a


$(TARGET): $(OBJECTS)
	rm -f $@
	ar cr $@ $^
	python setup.py config_fc --f90flags="-g -c -fdefault-real-8 -fPIC -fno-second-underscore -fbacktrace -fno-align-commons -fbounds-check" --fcompiler=gfortran build
	python setup.py install

%.o: %.F90
	$(FC) $(FCFLAGS) -I pkg/MOM6/config_src/dynamic -I pkg/MOM6/src/framework -c $< -o $@


clean:
	 rm -f *.o *.mod *.MOD
