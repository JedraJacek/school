#include <iostream>

using namespace std;

struct Date {
unsigned short int dd, mm, rrrr;
};

struct User {
    string login{}, password{}, status{}, type{};
    unsigned int id{};
    Date creationDate{};

    void showAllData();
    void setId(string login1, string password1, int id1, string status1, string type1, int dd1, int mm1, int rrrr1){
    login=login1;
    password=password1;
    id=id1;
    status=status1;
    type=type1;
    creationDate.dd = dd1;
    creationDate.mm = mm1;
    creationDate.rrrr = rrrr1;
    };
};

void User::showAllData(){
cout << "Login: " << login << "\nHas³o: " << password << "\nID u¿ytkownika: " << id
<< "\nStatus: " << status << "\nTyp konta: " << type << "\nData utworzenia konta: "
<< creationDate.dd << "-" << creationDate.mm << "-" << creationDate.rrrr << endl;
}

int main(int argc, char** argv)
{
    setlocale(LC_CTYPE, "polish");

    User uzytkownik;

    uzytkownik.setId("JedraJacek","niePowiem",1,"unactive","moderator",16,9,2021);
    uzytkownik.showAllData();
    return 0;
}
