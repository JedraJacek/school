#include <iostream>
#include <fstream>
using namespace std;

int main(){
    setlocale(LC_ALL, "polish");
    cout<<"Nazwa pliku: "<<endl;
    char name[20];
    cin >> name;
    ofstream File;
    File.open(name, ios_base::app);
    if(File.is_open()){
        cout << "Plik otwarty"<< endl;
        cout << "Podaj zawartosc do pliku: "<<endl;
        string text;
        getline(cin, text, 'x');
        File << text;
		File.close();
    }
    else{
        cout<<"Blad";
    }
    ifstream myFile(name);
    string myText;
   	cout << "\nPlik:" << endl;
   	while(getline(myFile, myText)) {
       	cout << myText << endl;
	}
    return 0;
}

