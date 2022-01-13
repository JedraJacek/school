#include <iostream>
using namespace std;

class Worker {
  private:
    string name {""}, surname {""};

  public:
    void setName(string pName){
      name=pName;
    }

    void setSurname(string pSurname){
      surname=pSurname;
    }

    string getName(){
      return name;
    }

    string getSurname(){
      return surname;
    }

    string getData(){
    return name + " " + surname;
  }
};

class Teacher : public Worker {
  private:
    string school_subject {""};
  public:
    void setSchool_subject(string pSchool_subject){
      school_subject = pSchool_subject;
    }
    string getSchool_subject(){
      return school_subject;
    }

    string getData(){
      return getName() + " " + getSurname() + ", zajêcia: " + school_subject + "\n";
  }
};

class Supervising : public Teacher {
private:
    string school_class {""};
public:
    void setSchool_class(string pSchool_class){
        school_class=pSchool_class;
    }
    string getSchool_class(){
        return school_class;
    }
    string getData(){
        return getName() + " " + getSurname() + ", zajêcia: " + getSchool_subject() + ", klasa: " + school_class + "\n";
    }
};

int main()
{
    setlocale(LC_CTYPE, "polish");

    Teacher nowak;
    nowak.setName("Jan");
    nowak.setSurname("Nowak");
    nowak.setSchool_subject("Programowanie obiektowe");
    cout << nowak.getData();

    Supervising wychowawca;
    wychowawca.setName("Test");
    wychowawca.setSurname("Testowy");
    wychowawca.setSchool_subject("Matematyka");
    wychowawca.setSchool_class("2PT");
    cout << wychowawca.getData();

    return 0;
}
