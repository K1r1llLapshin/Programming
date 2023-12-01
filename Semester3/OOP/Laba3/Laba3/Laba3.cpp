#include <iostream>
#include "Alphabet.h">
using namespace std;
int main()
{
	Alphabet alf;
	alf.PrintText("ООП.", '*', "Yellow", 5, 20);//Blue, Green, Cyan, Red, Magenta, Yellow, White	

	Alphabet alf1;
	alf1.PrintText("Привет мир!", '#', "Green", 1, 60);

	Alphabet alf2;
	alf2.PrintText("ПрогРАМмирование!?", '+', "Red", 7, 0);
}

