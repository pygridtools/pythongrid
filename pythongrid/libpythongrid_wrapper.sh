#!/bin/bash
#$ -S /bin/bash
LIBPYTHONGRID=$1;
shift;
python $LIBPYTHONGRID $@;
