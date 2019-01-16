//
// Copyright 2003-2015 Mentor Graphics Corporation
//
// All Rights Reserved.
//
// THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION WHICH IS THE PROPERTY OF 
// MENTOR GRAPHICS CORPORATION OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
// 

#include "ann_types.h"
#include "image_ppm.h"
#include "CNN_coeff_3x3.h"
#include "math.h"
#include <fstream>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include "mc_scverify.h"


CCS_MAIN(int argc, char *argv) {

	cout << "Starting Test" << endl ;
	ofstream INPUT_SIGNAL("input_signal.txt");
	ofstream OUTPUT_SIGNAL("output_signal.txt");
	
	c_type coeffs_fixed[X_FILTRE][Y_FILTRE][K_FILTRE][CH_FILTRE];

	for (int i=0;i<X_FILTRE;i++) {
		for (int j=0;j<Y_FILTRE;j++){
			for (int k=0;k<K_FILTRE;k++){
				for (int channel=0;channel<CH_FILTRE;channel++) {
					coeffs_fixed[i][j][k][channel] = coeffs_double[i][j][k][channel];
				}
			}
		}
	}

	//variables for the convolution function
	static ac_channel<d_type> data_in ;
	static ac_channel<d_type> data_out ;
	//
	double double_in, double_out;
	double fixed_out;
	double worst_error = 0 ;
	double diff ;

	d_type channel_read = 0;
	
	//TO DO: double img =  ;
 
 	d_type img_d_type = img_double ;
		
	// reference double precision filter
	double_in = img_d_type.to_double();
		 
	double_out = CONVOLUTION_REFERENCE(double_in, coeffs_double) ;
		
	data_in.write(img_d_type);
		
	INPUT_SIGNAL << temp.to_int() << endl ;
 
 	CCS_DESIGN(CONVOLUTION)(data_in,coeffs_fixed,data_out);
 	
 	if (data_out.available(1)) {
			channel_read = data_out.read() ;
			// compare with double precision reference
			fixed_out = channel_read.to_double() ;
			diff = fixed_out - double_out ;
			diff = (diff<0) ? -diff : diff ;
			worst_error = (diff > worst_error) ? diff : worst_error ;
			OUTPUT_SIGNAL << channel_read.to_int() << endl ;
	}
 	
	cout << "Simulation Done" << endl ;
	cout << "Worst error compared with double precision = " << worst_error << endl ;
	INPUT_SIGNAL.close() ;
	OUTPUT_SIGNAL.close() ;
	CCS_RETURN(0) ;
	
}
