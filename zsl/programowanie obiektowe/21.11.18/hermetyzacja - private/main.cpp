#include <iostream>

using namespace std;

class Rectangle {
private:
    double sideA {0};
    double sideB {0};

public:
    Rectangle();
    Rectangle(double pSideA, double pSideB);

    void getSides();

    double getSideA();
    double getSideB();

    void setSideA(double pSideA);
    void setSideB(double pSideB);
};

Rectangle::Rectangle(){};
Rectangle::Rectangle(double pSideA, double pSideB){
    sideA = pSideA;
    sideB = pSideB;
}

void Rectangle::getSides(){
    cout << "Bok a: " << sideA << ", bok b: " << sideB << endl;
}

void getSides(double a, double b){
    cout << "Bok a: " << a << ", bok b: " << b << endl;
}

double Rectangle::getSideA(){
    return sideA;
}

double Rectangle::getSideB(){
    return sideB;
}

void Rectangle::setSideA(double pSideA){
    sideA = pSideA;
};


void Rectangle::setSideB(double pSideB){
    sideB = pSideB;
};

int main()
{
    setlocale(LC_CTYPE, "polish");
    double width = 10;
    double height = 20;

    getSides(width, height);

    Rectangle p1;
    p1.getSides();

    Rectangle p2(width, height);
    p2.getSides();

    cout << "Bok a: " << p2.getSideA() << endl;

    p2.setSideA(3);
    cout << "Bok a: " << p2.getSideA() << endl;

    return 0;
}
