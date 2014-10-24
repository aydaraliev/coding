#!/bin/bash


for f in *.haps; do ./haps_to_selscan_tped.py $f ${f%.haps}; done
