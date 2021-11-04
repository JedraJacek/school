#include <iostream>


using namespace std;

class Animal{
	public:
		static int s_count;
		
		Animal(){
			s_count++;
			cout << "ilo�� obiekt�w: " << s_count << endl;
		}
		
		
		~Animal(){ //<-- destruktor
			s_count--;
			cout << "Ilo�� obiekt�w: " << s_count << endl;
		}
};

int Animal::s_count = 0;

int main(int argc, char** argv) {
	setlocale(LC_CTYPE, "polish");
	
	cout << "Ilo�� obiekt�w: " << Animal::s_count << endl; //0

	Animal dog;
//	delete dog;
	Animal cat;
	
	cout << "Ilo�� obiekt�w: " << Animal::s_count << endl; //2
	
	Animal *p_dog = new Animal();
	delete p_dog;
	
	return 0;
}
