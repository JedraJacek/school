#include <iostream>
#include <math.h>
#define M_PI 3.14159265358979323846

using namespace std;

class Cylinder{
	public:
		double radius, height;
		
		Cylinder(double pRadius, double pHeight){
			radius = pRadius;
			height = pHeight;
		};
		
		void showAllData();
		void baseArea();
		void sideArea();
		void Area();
		void Volume();
		
		
};

void Cylinder::baseArea(){
	cout << M_PI * radius * radius;
}

void Cylinder::sideArea(){
	cout << 2 * M_PI * radius * height;
}

void Cylinder::Area(){
	cout << 2 * M_PI * radius * radius + 2 * M_PI * radius * height;
}

void Cylinder::Volume(){
	cout << M_PI * radius * radius * height;
}

void Cylinder::showAllData(){
	cout << "\nPromieñ: " << radius << "\nWysokoœæ: " << height << "\n\nPole podstawy: " << M_PI * radius * radius << "\nPole boczne: " << 
	2 * M_PI * radius * height << "\nPole ca³kowite: " << 2 * M_PI * radius * radius + 2 * M_PI * radius * height << "\nObjêtoœæ: " <<
	M_PI * radius * radius * height << endl;
}


int main(int argc, char** argv) {
	setlocale(LC_CTYPE, "polish");
	int a;
	int b;
	cout << "Podaj promieñ" << endl;
	cin >> a;
	cout << "\nPodaj wysokoœæ" << endl;
	cin >> b;
	
	Cylinder cyl(a, b);
	cyl.showAllData();
	
	return 0;
}
