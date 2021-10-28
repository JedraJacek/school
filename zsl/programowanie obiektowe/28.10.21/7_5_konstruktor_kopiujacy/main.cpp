#include <iostream>
//https://pastebin.com/3icqPRaq

using namespace std;

class Rectangle {
	private:
		double sideA;
		double sideB;
		
		public:
			Rectangle();
			Rectangle(double pSideA, double pSideB);
		Rectangle(const Rectangle &);		/* <--konstruktor kopiuj�cy*/		
	
	void catchSides(double&, double &);
	void setSides(double, double);
	double area();
	double circuit();
};

Rectangle::Rectangle(){
	cout << "Konstruktor domy�lny" << endl;
}

Rectangle::Rectangle(double pSideA, double pSideB){
	sideA = pSideA;
	sideB = pSideB;
	cout << "Konstruktor parametryczny" << endl;
}

Rectangle::Rectangle(const Rectangle& model){
	sideA=model.sideA;
	sideB=model.sideB;
	cout << "Konstruktor kopiuj�cy" << endl;
}

void Rectangle::catchSides(double &pSideA ,double &pSideB){
	sideA=pSideA;
	sideB=pSideB;
}

void Rectangle::setSides(double pSideA, double pSideB){
	 sideA=pSideA;
	 sideB=pSideB;
}

double Rectangle::area(){
	return sideA * sideB;
}

double Rectangle::circuit(){
	return 2 * sideA + 2 * sideB;
}

Rectangle copyRectangle(Rectangle rectangle){
	return rectangle;
}

int main(int argc, char** argv) {
	setlocale(LC_CTYPE, "polish");
	
	double a=10.5, b=2;
	cout << "Pierwszy prostok�t: " << endl;
	Rectangle prostokat1(2,4);
	prostokat1.catchSides(a, b);
	cout << "Bok a: " << a << endl;
	cout << "Bok b: " << b << endl;
	
	cout << "\nDrugi prostok�t: " << endl;
	Rectangle prostokat2=prostokat1; /*<--konstruktor kopiuj�cy*/
	prostokat2.catchSides(a, b); 
	cout << "Bok a: " << a << endl;
	cout << "Bok b: " << b << endl;
	
	cout << "\nTrzeci prostok�t: " << endl;
	Rectangle prostokat3(prostokat1);
	prostokat3.catchSides(a, b);
	cout << "Bok a: " << a << endl;
	cout << "Bok b: " << b << endl;
	
	cout << "\nCzwarty prostok�t: " << endl;
	Rectangle prostokat4;
	prostokat4 = copyRectangle(prostokat1);
	prostokat4.catchSides(a, b);
	cout << "Bok a: " << a << endl;
	cout << "Bok b: " << b << endl; 	
	
	return 0;
}
