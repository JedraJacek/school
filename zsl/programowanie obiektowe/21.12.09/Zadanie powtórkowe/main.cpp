#include <iostream>

using namespace std;

class Car {
public:
    string brand, model, color;
    int year;
    static int s_numberOfWheels;
private:
    float price;
    string registration;
public:

void setPrice(float pPrice);
void setRegistration( string pRegistration);
void showData();
float getPrice();
string getRegistration();

    Car(string pBrand, string pModel, string pColor, int pYear, float pPrice, string pRegistration);
    Car(string pBrand, string pModel, int pYear);
    Car();

    ~Car();
};

int Car::s_numberOfWheels = 4;

    Car::~Car(){
        cout << "Wywo³ano destruktor" << endl;
    }

    Car::Car(string pBrand, string pModel, string pColor, int pYear, float pPrice, string pRegistration){
        brand = pBrand;
        model = pModel;
        color = pColor;
        year = pYear;
        price = pPrice;
        registration = pRegistration;
    }

    Car::Car(string pBrand, string pModel, int pYear){
        brand = pBrand;
        model = pModel;
        year = pYear;
    }

    Car::Car(){
        cout << "Wywo³ano konstruktor domyœlny" << endl;
    }

void Car::setPrice(float pPrice){
    price = pPrice;
}

void Car::setRegistration(string pRegistration){
    registration = pRegistration;
}

void Car::showData(){
    cout << "Marka: " << brand << "\nModel: " << model << "\nKolor" << color << "\nRok: " << year << "\nCena: " << price << "\nrejestracja: " << registration << endl;
}

float Car::getPrice(){
    return price;
}

string Car::getRegistration(){
    return registration;
}

int main()
{
    setlocale(LC_CTYPE, "polish");

    Car fiat("Fiat","Multipla","szary",2000,2000.99,"");
    //fiat.showData();
    Car *superauto;
    superauto = &fiat;
    superauto->setPrice(2000);
    //fiat.showData();

    /*
        Przeci¹¿enie konstruktora - stworzenie wiêcej ni¿ jednego konstruktora dla jednej klasy

        Przyk³ady:

        Car();

        Car(string pBrand, string pModel, int pYear);

        Car(string pBrand, string pModel, string pColor, int pYear, pYear, pPrice, pRegistration);
    */

    //Jacek Jêdra 2PT

    return 0;
}

