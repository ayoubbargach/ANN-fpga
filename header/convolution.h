#ifndef __CONVOLUTION_H__
#define __CONVOLUTION_H__

#include "types.h"

void convolution (
    e_type      img[WIDTH][HEIGHT][DEPTH],
    c_type      coeffs[WEIGHTS1_i][WEIGHTS1_j][WEIGHTS1_k][WEIGHTS1_channel],
    e_type      img_out[WIDTH_OUT][HEIGHT_OUT][DEPTH_OUT] );

#endif