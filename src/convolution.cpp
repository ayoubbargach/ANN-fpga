
#include "convolution.h"

void convolution (
		e_type      img[WIDTH][HEIGHT][DEPTH],
		c_type      coeffs[WEIGHTS1_i][WEIGHTS1_j][WEIGHTS1_k][WEIGHTS1_channel],
		e_type      img_out[WIDTH_OUT][HEIGHT_OUT][DEPTH_OUT] ) {
	
	ac_fixed<W_COEFF,I_COEFF,true,AC_RND_INF,AC_SAT> acc;

	for (h=0;h<WEIGHTS1_channel;h++) {
		for (i=0;i<WIDTH-2;i++) {
			for (j=0;j<HEIGHT-2;j++) {
				
				// Calcul du kernel
				for(ki=0; ki<WEIGHTS1_i; ki++) {
					for(kj=0; kj<WEIGHTS1_j; kj++) {
						for(kk=0; kk<WEIGHTS1_k; kk++) {
							acc += img[i+ki][j+kj][k] * coeffs[ki][kj][kk];
						}
					}
				}


				img_out[i,j,h] = acc;
				acc = 0;
			}
		}
	}

}
