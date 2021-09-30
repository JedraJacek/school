#include <iostream>

using namespace std;

class Student {
public:

    static string s_class;
    static string s_job;

    string name;
    string surname;

    static void s_getClassJob();
    void getNameSurname(string name, string surname){
        cout << "Imiê i nazwisko: " << name << " " << surname << endl;
    };
};

string Student::s_class = "2PT";
string Student::s_job = "Programista";

void Student::s_getClassJob(){
    cout << "Klasa: " << s_class << "\nZawód: " << s_job << endl;
}

int main()
{
    setlocale(LC_CTYPE, "polish");

    Student uczen;

    uczen.getNameSurname("Jacek", "Jêdra");
    uczen.s_getClassJob();

    return 0;
}
