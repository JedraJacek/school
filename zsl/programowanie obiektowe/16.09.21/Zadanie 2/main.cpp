#include <iostream>

using namespace std;

class rectangle{
public:
    float a;
    float b;

    float rectangleArea(float a, float b);
    float rectangleCircumference(float a, float b);
};

float rectangle::rectangleArea(float a, float b){
float Area = a*b;

cout << Area << endl;
};

float rectangle::rectangleCircumference(float a, float b){
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
