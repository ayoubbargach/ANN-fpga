//
// Copyright 2003-2015 Mentor Graphics Corporation
//
// All Rights Reserved.
//
// THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION WHICH IS THE PROPERTY OF 
// MENTOR GRAPHICS CORPORATION OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
// 

#include "types.h"
#include "coeffs.h"
#include "image_ppm.h"
#include "image_24x24x3.h"
#include "math.h"
#include <fstream>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include "mc_scverify.h"


CCS_MAIN(int argc, char *argv) {

	cout << "Starting Test" << endl ;

	ofstream OUTPUT_FILE("output.txt");
	
	c_type coeffs_fixed[X_FILTRE][Y_FILTRE][K_FILTRE][CH_FILTRE];

	for (int i=0;i<X_FILTRE;i++) {
		for (int j=0;j<Y_FILTRE;j++){
			for (int k=0;k<K_FILTRE;k++){
				for (int channel=0;channel<CH_FILTRE;channel++) {
					coeffs_fixed[i][j][k][channel] = filtre[i][j][k][channel];
				}
			}
		}
	}

	e_type img_out[WIDTH_OUT][HEIGHT_OUT][DEPTH_OUT];

	convolution(image, coeffs_fixed, img_out);

	OUTPUT_FILE << img_out << endl;

	cout << "Simulation Done" << endl ;

	OUPUT_SIGNAL.close();

	CCS_RETURN(0);
	
}
