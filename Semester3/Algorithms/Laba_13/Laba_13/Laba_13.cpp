#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

class HashTable
{
private:
    vector<string> value_hash;

    int hashFunction(string key_, vector<string>& hash_table)
    {
        int key = key_.size() % hash_table.size();

        while (!hash_table[key].empty())
        {
            if (key == hash_table.size() - 1)
                key = 0;
            else
                key += 1;
        }
        return key;
    }
    void overrideHashTable()
    {
        int new_size_table = value_hash.size() + 10;
        vector<string> new_hash_table(new_size_table);

        for (int count = 0; count < value_hash.size(); count++)
        {
            if (!value_hash[count].empty())
            {
                int new_index = hashFunction(value_hash[count], new_hash_table);
                new_hash_table[new_index] = value_hash[count];
            }
        }

        value_hash = new_hash_table;
    }
    int fullnessTable()
    {
        int filledElements = 0;
        for (int count = 0; count < value_hash.size(); count++)
        {
            if (!value_hash[count].empty())
                filledElements++;
        }

        return filledElements / value_hash.size() * 100;
    }


public:
    HashTable(int size)
    {
        value_hash.resize(size);
    }
    void add(string value)
    {
        if (fullnessTable() >= 80)
        {
            overrideHashTable();
        }

        int index = hashFunction(value, value_hash);
        value_hash[index] = value;

    }
    void makeFile()
    {
        ofstream HashTable;

        HashTable.open("HashTable.txt");
        HashTable << string(50, '-') << '\n' << '|' << '\t' << "Key" << '\t' << '|' << '\t' << "Value" << '\n' << string(50, '-') << '\n';

        for (int count = 0; count < value_hash.size(); count++)
        {
            HashTable << '|' << '\t' << count << '\t' << '|' << '\t' << value_hash[count] << '\n' << string(50, '-') << '\n';
            
        }
        HashTable.close();
    }
};

int main()
{
    locale::global(locale("ru_RU.utf8"));


    HashTable hashTable(15);
    string word;

    ifstream file("File.txt");
    if (!file.is_open())
        cout << "Error";
    else
    {
        file.imbue(locale("ru_RU.utf8"));
        while (file >> word)
        {
            hashTable.add(word);
        }
    }
    file.close();

    hashTable.makeFile();
    

}
