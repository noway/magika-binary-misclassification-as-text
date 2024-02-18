#!/bin/bash

export n=$1
export n_slug=$(echo $n | sed 's/\.//g')

mkdir -p fuzz$n_slug

echo "generating fuzz for $n rate"
for i in {1..10000}
do
    zzuf -r $n -s$i < output.png > fuzz$n_slug/output_$i.png
done
