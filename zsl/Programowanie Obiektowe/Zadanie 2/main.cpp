#include <iostream>

using namespace std;

class rectangle{
public:
    float a;
    float b;

    void rectangleArea();
    void rectangleCircumference();
};

void rectangle::rectangleArea(){
float Area = a*b;

cout << Area << endl;
};

void rectangle::rectangleCircumference(){
float Circumference = a*2 + b*2;

cout << Circumference << endl;
};

int main()
{
    rectangle test;
    test.a = 3;
    test.b = 3;

    test.rectangleArea();
    test.rectangleCircumference();

    return 0;
}
