#!/bin/bash

for i in *.tped; do ./selscan --ihs --threads 5 --tped $i --out $i.out; done
