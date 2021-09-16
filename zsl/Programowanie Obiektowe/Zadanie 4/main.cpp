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
    void setId(unsigned int x, string name1, string surname1, int dd1, int mm1, int rrrr1){
    id=x;
    name=name1;
    surname=surname1;
    dateBirthday.dd = dd1;
    dateBirthday.mm = mm1;
    dateBirthday.rrrr = rrrr1;
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
    pracownik.setId(100, "Janusz", "Nowak", 16, 9, 2021);

    pracownik.showAllData();

    return 0;
}
