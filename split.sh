#!/bin/bash

awk -F ' ' '{ print > ("chr-" $1 ".tped") }' ki_phased_conv_pop3.tped
