#include <iostream>

using namespace std;

class Konto_bankow {
private:
    double kwota;
    int pesel;
public:
    int numerKonta;

    int getNumber();
    double getSum();
    int getPesel();

    void setNumber(int pNumerKonta);
    void setSum(double pKwota);
    void setPesel(int pPesel);

    Konto_bankow(){};

    Konto_bankow(double pKwota, int pPesel, int pNumerKonta){
    kwota = pKwota;
    pesel = pPesel;
    numerKonta = pNumerKonta;
    };
};

int Konto_bankow::getNumber(){
    return numerKonta;
}

int Konto_bankow::getPesel(){
    return pesel;
}

double Konto_bankow::getSum(){
    return kwota;
}

void Konto_bankow::setNumber(int pNumerKonta){
    numerKonta = pNumerKonta;
}

void Konto_bankow::setPesel(int pPesel){
    pesel = pPesel;
}

void Konto_bankow::setSum(double pKwota){
    kwota = pKwota;
}

int main()
{
    setlocale(LC_CTYPE, "polish");

    Konto_bankow k1(123.45, 214253, 1);

    cout << "\nNumer konta: " << k1.getNumber() <<  "\nPesel: " << k1.getPesel() << "\nKwota: " << k1.getSum() << endl;

    Konto_bankow k2;
    k2.setNumber(2);
    k2.setSum(1224.2);
    k2.setPesel(1215);

    cout << "\nNumer konta: " << k2.getNumber() << "\nPesel: " << k2.getPesel() << "\nKwota: " << k2.getSum() << endl;

    return 0;
}
