#include <iostream>

using namespace std;

struct Data {
    unsigned short int dd, mm, rrrr;
};

struct Student {
    string name, surname;
    unsigned int id;
    Data dateBirthday;
    unsigned short int gradeInformatics[5];
};



int main(int argc, char** argv)
{
    setlocale(LC_CTYPE, "polish");
    Student student {"Katarzyna", "Nowak", 100, {16, 9, 2021}, {2, 3, 4, 5, 4}};
    cout << "Imiê i nazwisko: " << student.name << " " << student.surname << "\nId: " << student.id
    << "\nData urodzenia: "
    << student.dateBirthday.dd << "-"
    << student.dateBirthday.mm << "-"
    << student.dateBirthday.rrrr << "r."
    << "\n\nOceny z informatyki: "
    << "\n1 ocena: " << student.gradeInformatics[0] << endl
    << "\n2 ocena: " << student.gradeInformatics[1] << endl
    << "\n3 ocena: " << student.gradeInformatics[2] << endl
    << "\n4 ocena: " << student.gradeInformatics[3] << endl
    << "\n5 ocena: " << student.gradeInformatics[4] << endl << endl;
    return 0;
}
