#include <iostream>

using namespace std;

class book{
public:
    string title;
    string author;

    void getTitle();
    void getAuthor();
    void setAuthor(string name);
    void showAllData();

    book(string pTitle, string pAuthor);
};

void book::showAllData(){
    cout << "Tytu�: " << title << "\nAutor: " << author << endl;
}

book::book(string pTitle, string pAuthor){
    title = pTitle;
    author = pAuthor;
};

void book::getTitle(){
    cout << "Tytu�: " << title << endl;
};

void book::getAuthor(){
    cout << "Autor: " << author << endl;
};

void book::setAuthor(string name){
    author = name;
};

int main()
{
    setlocale(LC_CTYPE, "polish");

    book kordian("Kordian","Juliusz S�owacki");
    kordian.getTitle();
    kordian.getAuthor();
    kordian.setAuthor("Adam Mickiewicz");
    kordian.getAuthor();

    return 0;
}
