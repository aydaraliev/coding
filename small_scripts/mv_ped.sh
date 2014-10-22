#!/bin/bash

mkdir chromosomes

for i in {1..22}; do mv chr$i.* ./chromosomes; done
