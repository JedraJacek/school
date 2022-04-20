#include <iostream>

using namespace std;

struct date{
    unsigned short int dd, mm, yyyy;
};

class car{
    public:
    unsigned int id=3;
    string brand = "nieznana", model, color;
    unsigned short int power;
    float price;
    date dateOfProduction;

    void getData();

    car(unsigned int pId=3, string pBrand="MARKA");
};

car::car(unsigned int pId, string pBrand){
    id=pId;
    brand=pBrand;
}

void car::getData(){
    cout << "Identyfikator: " << id << "\nMarka: " << brand << endl << endl;
};


int main()
{
    setlocale(LC_CTYPE, "polish");

    car opel;
    opel.getData();

    car fiat(15,"Fiat");
    fiat.getData();

    car bmw = car(12);
    bmw.getData();


    car *ptr;
    ptr = &bmw;
    ptr->getData();
    ptr->brand="BMW";
    ptr->getData();

    return 0;
}
