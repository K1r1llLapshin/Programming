#include <iostream>
#include "Array3D.h"
using namespace std;
int main()
{
	/*Array3D<int> array;
	array = Array3D<int>::CreateFill(2, 2, 3, 10);
	Array3D<int> res;

	res = array.getValue0(1);
	cout << "i(1): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue0(1, 5);
	res = array.getValue0(1);
	cout << "i(1): " << '\n' << res << '\n';

	res = array.getValue1(1);
	cout << "j(1): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue1(1, 1);
	res = array.getValue1(1);
	cout << "j(1): " << '\n' << res << '\n';

	res = array.getValue2(1);
	cout << "k(1): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue2(1, 7);
	res = array.getValue2(1);
	cout << "k(1): " << '\n' << res << '\n';

	res = array.getValue01(1,0);
	cout << "i(1) and j(0): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue01(1, 0, 17);
	res = array.getValue01(1, 0);
	cout << "i(1) and j(0): " << '\n' << res << '\n';


	res = array.getValue02(1,2);
	cout << "j(1) and k(2): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue02(1, 2, 45);
	res = array.getValue02(1,2);
	cout << "j(1) and k(2): " << '\n' << res << '\n';

	res = array.getValue12(1, 2);
	cout << "i(1) and k(2): " << '\n' << res;
	cout << "Overwriting" << ' ';
	array.setValue12(1, 2, 32);
	res = array.getValue12(1, 2);
	cout << "i(1) and k(2): " << '\n' << res << '\n';
	
	cout << "i(1) and j(1) and k(1): " << '\n' << array.getValue(1, 1, 2) << '\n' << '\n';
	cout << "Overwriting" << ' ';
	array.setValue(1, 1, 2, 123);
	cout << "i(1) and j(1) and k(1): " << '\n' << array.getValue(1, 1, 2) << '\n' << '\n';


	cout << "array[0][1][2]: " << array(0, 1, 2) << '\n' << '\n';

	cout << "All array: " << '\n' << array << '\n';*/


	Array3D<char> array_char(3, 5, 2);

	array_char.setValue01(1, 3, 'K');
	Array3D<char> res_char;
	res_char = array_char.getValue01(1, 3);
	cout << "i(1) and j(3): " << '\n' << res_char;

	array_char.setValue0(0, 'L');
	res_char = array_char.getValue0(0);
	cout << "i(0): " << '\n' << res_char;

	array_char.setValue2(0, 'i');
	res_char = array_char.getValue2(0);
	cout << "k(1): " << '\n' << res_char;

	cout << "All array: " << '\n' << array_char << '\n';
}


