#include <iostream>

using namespace std;

struct Date {
    unsigned short int dd, mm, rrrr;
};

class worker{
public:
    unsigned int id {};
    string name {}, surname {};
    Date dateBirthday {};

    void showAllData();
    void setId(unsigned int id, string name, string surname, Date dateBirthday){
    worker::id=id;
    worker::name=name;
    worker::surname=surname;
    worker::dateBirthday = dateBirthday;
    };
};

void worker::showAllData(){
    cout << "Dane pracownika:\n" << "Id: " << id
    << "\nImiê i nazwisko: " << name << " " << surname
    << "\nData urodzenia: " << dateBirthday.dd << "-"
    << dateBirthday.mm << "-" << dateBirthday.rrrr << "r." << endl;
}

int main(int argc, char** argv)
{
    setlocale(LC_CTYPE, "polish");
    worker pracownik;
    pracownik.setId(100, "Janusz", "Nowak",{16, 9, 2021});

    pracownik.showAllData();

    return 0;
}
