#!/bin/bash

# If the env variable do not exist, create it :
if [[ -z "${PHELMA_ANN_PROJECT_IMAGE_RAW}" ]]; then
  PHELMA_ANN_PROJECT_IMAGE_RAW="../cifar10_data/cifar-10-batches-bin/test_batch.bin"
fi

if [[ -z "${PHELMA_ANN_PROJECT_STEPS}" ]]; then
  PHELMA_ANN_PROJECT_STEPS=1
fi

cat $PHELMA_ANN_PROJECT_IMAGE_RAW | dd count=3072 bs=1 skip=$PHELMA_ANN_PROJECT_STEPS > tmp.raw
display -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw
convert -compress none -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw image.ppm
