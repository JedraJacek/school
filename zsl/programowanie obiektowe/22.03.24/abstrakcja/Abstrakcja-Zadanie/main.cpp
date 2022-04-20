#include <iostream>

using namespace std;

class Person{
public:
    string name;
    string surname;

    virtual void showData()=0;
};

class Worker : public Person {
public:
    string position;

    void showData(){
        cout << "Imiê i nazwisko: " << name + " " + surname << ", pozycja: " << position << endl;
    }
};

class Student : public Person {
public:
    string classAtSchool;

    void showData(){
        cout << "Imiê i nazwisko: " << name + " " + surname << ", klasa: " << classAtSchool << endl;
    }
};

int main()
{
    setlocale(LC_ALL, "polish");

    //Person osoba;

    Worker pracownik1;
    pracownik1.name="Janusz";
    pracownik1.surname="Nowak";
    pracownik1.position="Programista";
    cout << "Dane pracownika:\n";
    pracownik1.showData();

    Student uczen1;
    uczen1.name="Anna";
    uczen1.surname="Kowalska";
    uczen1.classAtSchool="2PT";
    cout << "\nDane Ucznia:\n";
    uczen1.showData();

    return 0;
}
