#ifndef __ANN_TYPES_H__
#define __ANN_TYPES_H__

#include "coeffs"
#include "ac_int.h"
#include "ac_fixed.h"


#define W_COLOR 8 // Each RGB color for each pixel is defined on 8-bit structure

#define W_COEFF 32 
#define I_COEFF 4

#define WIDTH 26 // Because the padding is already added to the image
#define WIDTH_OUT 24

#define HEIGHT 26 // Because the padding is already added to the image
#define HEIGHT_OUT 24

#define DEPTH 3
#define DEPTH_OUT 64


typedef ac_int<W_COLOR> e_type;
typedef ac_fixed<W_COEFF,I_COEFF,true,AC_RND_INF,AC_SAT> c_type ;



#endif


