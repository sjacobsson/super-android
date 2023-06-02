#include <stdio.h>
#include <complex>

std::complex<double> get_z(
	int i,
	int j,
	int res_real,
	int res_imag,
	double upper_left_real,
	double upper_left_imag,
	double lower_right_real,
	double lower_right_imag
	) {
 
	return std::complex<double>(
		((double) i) / res_real * (lower_right_real - upper_left_real) + upper_left_real,
		((double) j) / res_imag * (upper_left_imag - lower_right_imag) + lower_right_imag
		);
}

//double julia(std::complex<double> z, std::complex<double> c) {
	//// TODO: make a macro
	//const int i_max = 1000;
	//const double zabs_max = 10.0;

	//int i = 0;
	//for (; (i < i_max) and (abs(z) <= zabs_max); i++) {
		//z = z * z + c;
	//}

	//return ((double) i) / i_max;
//}
double julia(double zr, double zi, double cr, double ci) {
	const int imax = 1000;
	const double z_max2 = 10*10;
	int i = 0;
	while((i < imax) && (zr*zr + zi*zi < z_max2)){
		double temp = zr*zr - zi*zi + cr;
		zi = 2*zr*zi + ci;
		zr = temp;
		i++;
	}
	return ((double) i)/imax;
}


int main(int argc, char** argv) {

	int res_real = atoi(argv[1]);
	int res_imag = atoi(argv[2]);
	double upper_left_real = atof(argv[3]);
	double upper_left_imag = atof(argv[4]);
	double lower_right_real = atof(argv[5]);
	double lower_right_imag = atof(argv[6]);

	std::complex<double> c = std::complex<double>(-0.1, 0.65);
	for (int i = 0; i < res_real; i++) {
		for (int j = 0; j < res_real; j++) {
			std::complex<double> z = get_z(i, j, res_real, res_imag, upper_left_real, upper_left_imag, lower_right_real, lower_right_imag);
			printf("%f\n", julia(real(z), imag(z), real(c), imag(c)));
		}
	}
	
	return 0;
}


