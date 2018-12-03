#!/bin/bash

nb=1
cat ../cifar10_data/cifar-10-batches-bin/test_batch.bin | dd count=3072 bs=1 skip=$nb > tmp.raw
display -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw
convert -compress none -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw image.ppm
