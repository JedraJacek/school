#include <iostream>

using namespace std;

class Rectangle {
public:
    double sideA {0};
    double sideB {0};

    Rectangle();
    Rectangle(double pSideA, double pSideB);

    void getSides();
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


    return 0;
}
