#include <iostream>

using namespace std;

class Worker{
private:
    float salary;
public:
    string name, surname;
    void setSalary(float pMoney);
    float getSalary();
};

class Teacher: public Worker{
public:
    string MedicalSpecialization;
};

void Worker::setSalary(float pMoney){
    salary=pMoney;
}

float Worker::getSalary(){
    return salary;
}


int main()
{
    setlocale(LC_CTYPE, "polish");

    Worker nowak;
    nowak.name="Janusz";
    nowak.surname="Nowak";
    nowak.setSalary(2000);

    cout << "Obiekt klasy Worker: " << nowak.name << " " << nowak.surname << endl;
    cout << "Zarobki: " << nowak.getSalary() << "z³" << endl;

    Teacher kowal;                                                     //Klasa pochodna u¿ywa zmiennej z klasy bazowej
    kowal.name="Anna";
    kowal.surname="Kowal";
    kowal.MedicalSpecialization="Kardiolog";

    cout << "\nObiekt klasy Teacher: " << kowal.name << " " << kowal.surname << endl;
    cout << "specjalizacja: " << kowal.MedicalSpecialization << endl;

    return 0;
}
