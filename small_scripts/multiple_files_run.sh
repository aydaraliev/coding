#!/bin/bash

for i in *.tped; do ./selscan --ihs --tped $i --out $i.out; done
