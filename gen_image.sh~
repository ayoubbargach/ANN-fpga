#!/bin/bash

# If the env variable do not exist, create it :
if [[ -z "${PHELMA_ANN_PROJECT_IMAGE_RAW}" ]]; then
  PHELMA_ANN_PROJECT_IMAGE_RAW=../../cifar10_data/cifar-10-batches-bin/test_batch.bin
fi

if [[ -z "${PHELMA_ANN_PROJECT_OFFSET}" ]]; then
  PHELMA_ANN_PROJECT_OFFSET=1
fi

if [[ -z "${PHELMA_ANN_PROJECT_STEP}" ]]; then
  PHELMA_ANN_PROJECT_STEP=0
fi

cat $PHELMA_ANN_PROJECT_IMAGE_RAW | dd count=3073 bs=1 skip=$PHELMA_ANN_PROJECT_OFFSET > tmp.raw
cat $PHELMA_ANN_PROJECT_IMAGE_RAW | dd count=4 bs=1 skip=$PHELMA_ANN_PROJECT_STEP > class.raw
# display -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw
convert -compress none -size 32x32 -depth 8 -interlace Plane rgb:tmp.raw image.ppm
