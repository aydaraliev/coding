#!/bin/bash


for f in {1..22}; do  ~/Desktop/plink-1.07-x86_64/plink --file ceu_missing_inds_filtered_2 --chr $f --recode --out chr$f --noweb; done

