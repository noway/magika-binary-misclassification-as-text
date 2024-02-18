#!/bin/bash

set -x

magika -r fuzz* | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" > magika_output.txt
