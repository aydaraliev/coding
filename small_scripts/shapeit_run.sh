#!/bin/bash


for i in {1..22}; do ./shapeit_stat/shapeit --input-ped 'chr'$i'.ped' 'chr'$i'.map' -M './rates/genetic_map_chr'$i'_b36.txt' -O 'chr'$i'_phased'; done
