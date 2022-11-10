# Makefile for creating our standalone Cython program
PYTHON := python3
PYVERSION := $(shell $(PYTHON) -c "import sys; print(sys.version[:3])")
PYPREFIX := $(shell $(PYTHON) -c "import sys; print(sys.prefix)")

INCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
PLATINCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc(plat_specific=True))")
LIBDIR1 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
LIBDIR2 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBPL'))")
PYLIB := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")

CC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('CC'))")
LINKCC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKCC'))")
LINKFORSHARED := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKFORSHARED'))")
LIBS := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBS'))")
SYSLIBS :=  $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('SYSLIBS'))")


WORKDIR := $(shell pwd)

CYTHON := $(shell which cython)
.PHONY: paths all clean test

paths:
	@echo "PYTHON=$(PYTHON)"
	@echo "PYVERSION=$(PYVERSION)"
	@echo "PYPREFIX=$(PYPREFIX)"
	@echo "INCDIR=$(INCDIR)"
	@echo "PLATINCDIR=$(PLATINCDIR)"
	@echo "LIBDIR1=$(LIBDIR1)"
	@echo "LIBDIR2=$(LIBDIR2)"
	@echo "PYLIB=$(PYLIB)"
	@echo "CC=$(CC)"
	@echo "LINKCC=$(LINKCC)"
	@echo "LINKFORSHARED=$(LINKFORSHARED)"
	@echo "LIBS=$(LIBS)"
	@echo "SYSLIBS=$(SYSLIBS)"
	@echo "CYTHON=$(CYTHON)"
	@echo "WORKDIR=$(WORKDIR)"

cython:
	$(PYTHON) setup.py build_ext --inplace 

clean:
	@rm -f ./mol2obj/*.c
	@rm -f ./mol2obj/*.so
	@rm -f ./write/*.c
	@rm -f ./write/*.so
	@rm -f ./parameters/*.c
	@rm -f ./parameters/*.so
	@rm -f ./sql_scripts/*.c
	@rm -f ./sql_scripts/*.so
	@rm -f ./psql_handeler/*.c
	@rm -f ./psql_handeler/*.so
	@rm -rf ./build
	@rm -f *.c *.so

localclean:
	@rm -f ./mol2obj/*.c
	@rm -f ./mol2obj/*.so
	@rm -f ./write/*.c
	@rm -f ./write/*.so
	@rm -f ./parameters/*.c
	@rm -f ./parameters/*.so
	@rm -f ./sql_scripts/*.c
	@rm -f ./sql_scripts/*.so
	@rm -f ./psql_handeler/*.c
	@rm -f ./psql_handeler/*.so
	@rm -rf ./build
	@rm -f *.c *.so
