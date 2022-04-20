#include <iostream>

using namespace std;

class Test{
public:
    int a;
};

class Worker{
public:
    string name;
    string surname;
    string nationality;
    unsigned short int yearBirthday;
    float height;
    char gender;

    void showNameSurname(){
        cout << "imiê i nazwisko " << name << " " << surname;
    };
    //deklaracja (prototyp) metody showAllData
    void showAllData();
};

void Worker::showAllData(){
    string genderDescription;
    switch(gender){
    case 'm':
        genderDescription = "Mê¿czyzna";
        break;
    case 'w':
        genderDescription = "Kobieta";
        break;
    default:
        genderDescription = "-";

    }

    cout << "imiê i nazwisko: " << name << " " << surname << "\n"
    << "Narodowoœæ: " << nationality << ", data urodzenia: " << yearBirthday
    << "\nWzrost: " << height << ", p³eæ: " << genderDescription << endl;
};

int main(int argc, char** argv)
{
    setlocale(LC_CTYPE,"polish");
    Test newObject;
//    cout << newObject.a;

    Worker pracownik;
    pracownik.name="Jan";
    pracownik.surname="Kowalski";
    pracownik.nationality="Polska";
    pracownik.yearBirthday=1998;
    pracownik.height=180;
    pracownik.gender='m';
cout << pracownik.name << endl << endl;
//pracownik.showNameSurname();
pracownik.showAllData();

    return 0;
}
