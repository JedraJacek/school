#include <iostream>

using namespace std;

class Person{
protected:
    string name;
    string surname;
public:
    virtual void showData()=0;

    string getName(){
        return name;
    }
    string getSurname(){
        return surname;
    }

    void setName(string pName){
        name=pName;
    }
    void setSurname(string pSurname){
        surname=pSurname;
    }

    Person(){};
    Person(string pName, string pSurname){
        name=pName;
        surname=pSurname;
    }
};

class Worker : public Person {
protected:
    string position;
public:
    void showData(){
        cout << "Imiê i nazwisko: " << name + " " + surname << ", pozycja: " << position << endl;
    }

    string getPosition(){
        return position;
    }

    void setPosition(string pPosition){
        position = pPosition;
    }

    Worker(){};
    Worker(string pName, string pSurname, string pPosition) : Person(pName, pSurname){
        position = pPosition;
    }

};

class Student : public Person {
protected:
    string classAtSchool;
public:
    void showData(){
        cout << "Imiê i nazwisko: " << name + " " + surname << ", klasa: " << classAtSchool << endl;
    }

    string getClass(){
        return classAtSchool;
    }

    void setClass(string pClass){
        classAtSchool = pClass;
    }

    Student(){};
    Student(string pName, string pSurname, string pClass) : Person(pName, pSurname){
        classAtSchool = pClass;
    }
};

int main()
{
    setlocale(LC_ALL, "polish");

    //Person osoba;

    Worker pracownik1;  //("Janusz","Nowak","Programista");
    pracownik1.setName("Janusz");
    pracownik1.setSurname("Nowak");
    pracownik1.setPosition("Programista");
    cout << "Dane pracownika:\n";
    pracownik1.showData();

    Student uczen1;  //("Anna","Kowalska","2PT");
    uczen1.setName("Anna");
    uczen1.setSurname("Kowalska");
    uczen1.setClass("2PT");
    cout << "\nDane Ucznia:\n";
    uczen1.showData();

    return 0;
}
