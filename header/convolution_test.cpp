#ifndef __CONVOLUTION_H__
#define __CONVOLUTION_H__

#include "types.h"

void convolution (
    e_type      img[WIDTH][HEIGHT][DEPTH],
    c_type      coeffs[X_FILTRE][Y_FILTRE][K_FILTRE][CH_FILTRE],
    e_type      img_out[WIDTH_OUT][HEIGHT_OUT][4] );

#endif