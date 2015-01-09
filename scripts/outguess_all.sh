#!/bin/bash

cd ~/Dropbox/3301/2015/

for f in ./pics/*
do
	echo "Running outguess on: $f"
        outfile=${f##*/}.out
        echo $outfile
	outguess -r $f ./outguesses/$outfile
        echo ""
done
