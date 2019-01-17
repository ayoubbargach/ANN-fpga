
#include "convolution_test.h"

void convolution (
		    e_type      img[WIDTH][HEIGHT][DEPTH],
            c_type      coeffs[X_FILTRE][Y_FILTRE][K_FILTRE][CH_FILTRE],
            e_type      img_out[WIDTH_OUT][HEIGHT_OUT][CH_FILTRE] ) {
	
	ac_fixed<W_COEFF,I_COEFF,true,AC_RND_INF,AC_SAT> acc;

	for (h=0;h<CH_FILTRE;h++) {
		for (i=0;i<WIDTH-2;i++) {
			for (j=0;j<HEIGHT-2;j++) {
				
				// Calcul du kernel
				for(ki=0; ki<X_FILTRE; ki++) {
					for(kj=0; kj<Y_FILTRE; kj++) {
						for(kk=0; kk<K_FILTRE; kk++) {
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
