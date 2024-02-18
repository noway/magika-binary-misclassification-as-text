#!/bin/bash

set -x

cat magika_output.txt | grep -v 'Low-confidence model best-guess' | grep -v .'png: Unknown binary data' | grep -v '.png: PNG image data' > magika_misclassifications.txt