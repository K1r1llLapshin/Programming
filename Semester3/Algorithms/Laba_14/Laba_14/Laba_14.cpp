#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <codecvt>
using namespace std;

class HashTable
{
private:

	vector<list<wstring>> _HashTable;

	int hashFunction(wstring key, vector<list<wstring>> HashTable)
	{
		int res = key[0] % HashTable.size();
		while (!HashTable[res].empty() && HashTable[res].front()[0] != key[0])
		{
			if (res == HashTable.size() - 1)
				res = 0;
			else
				res += 1;
		}

		return res;
	}
	int fullnessTable()
	{
		int filledElements = 0;
		for (int count = 0; count < _HashTable.size(); count++)
		{
			if (!_HashTable[count].empty())
				filledElements += 1;
		}

		return (filledElements * 100) / _HashTable.size() ;
	}
	void overrideHashTable()
	{
		vector<list<wstring>> new_HashTable(_HashTable.size()+10);
		
		for (int count = 0; count < _HashTable.size(); count++)
		{
			list<wstring>::iterator it;
			for (it = _HashTable[count].begin(); it != _HashTable[count].end(); ++it)
			{
				int index = hashFunction(*it, new_HashTable);
				new_HashTable[index].push_back(*it);
			}
		}
		_HashTable = new_HashTable;
	}
public:
	HashTable(int size)
	{
		_HashTable.resize(size);
	}

	void add(wstring value)
	{
		if (fullnessTable() >= 80)
		{
			overrideHashTable();
		}

		int index = hashFunction(value, _HashTable);
		_HashTable[index].push_back(value);

	}
	void makeFile()
	{
		wofstream Hash_Table;

		Hash_Table.open("HashTable.txt");
		Hash_Table << wstring(250, '-') << '\n' << '|' << '\t' << "Key" << '\t' << '|' << '\t' << "Value" << '\n' << wstring(250, '-') << '\n';

		for (int count = 0; count < _HashTable.size(); count++)
		{
			Hash_Table << '\t' << count << '\t' << '|' << '\t';
			typename list<wstring>::iterator it;
			for (it = _HashTable[count].begin(); it != _HashTable[count].end(); ++it)
			{
				Hash_Table << *it << ' ';
			}
			Hash_Table << '\n' << wstring(250, '-') << '\n';
		}
		Hash_Table.close();
	}
};


int main()
{
    locale::global(locale("ru_RU.utf8"));

	HashTable hashTable(15);
	wstring word;

	wifstream file("File.txt");
	if (!file.is_open())
		cout << "Error";
	else
	{
		while (file >> word)
		{
			hashTable.add(word);
		}
	}
	file.close();

	hashTable.makeFile();


}

