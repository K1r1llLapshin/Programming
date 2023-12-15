#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void Quick_Sort(vector<int>& numbers, int start, int end)
{
    if (start >= end)
        return;

    int pivot = numbers[start];
    int left = start + 1;
    int right = end;

    while (left <= right)
    {
        if (numbers[left] > pivot && numbers[right] < pivot)
        {
            swap(numbers[left], numbers[right]);
            left++;
            right--;
        }

        if (numbers[left] <= pivot)
            left++;

        if (numbers[right] >= pivot)
            right--;
    }

    swap(numbers[start], numbers[right]);

    Quick_Sort(numbers, start, right - 1);
    Quick_Sort(numbers, right + 1, end);
}

void Sort_File(string link)
{
    vector<int> num;
    string num_str;
    ifstream read(link);
    if(!read.is_open())
      cout << "ERROR:"<< link <<'\n';
    else
    {
        cout << "WORK:" << link << '\n';
        while (read >> num_str)
        {
            num.push_back(stoi(num_str));
        }
    }
    read.close();

    Quick_Sort(num, 0, num.size() - 1);

    ofstream overwriting(link, ios::trunc);
    for (int count = 0; count < num.size(); count++)
        overwriting << num[count] << ' ';
    overwriting.close();
}



int main()
{
    string exampleFileName = "Example.txt";
    ifstream read;
    string num;
    int count_num = 0;
    int current_file = 0;
    vector<string> link;

    read.open(exampleFileName);

    if (!read.is_open())
        cout << "Error\n";
    else
    {
        cout << "Work\n";
        ofstream write;

        while (read >> num)
        {
            if (count_num != 50)
            {
                write.open("Help_" + to_string(current_file) + ".txt", ios::app);
                write << num << ' ';
                write.close();
                count_num++;
            }
            else
            {
                current_file++;
                count_num = 0;
            }
        }        write.close();
    }
    read.close();

    for (int count = 0; count <= current_file; count++)
        link.push_back("Help_" + to_string(count) + ".txt");

    for (int count = 0; count < link.size(); count++)
        Sort_File(link[count]);


    string res = "Result.txt";

    ifstream read_file1;
    ifstream read_file2;
    ifstream read_result;
    ofstream write_result;
    ofstream write_file1;

    for (size_t count = 1; count < link.size(); ++count) {
        read_file1.open(link[0]);
        read_file2.open(link[count]);
        write_result.open(res);

        int num1, num2;
        if (read_file1 >> num1 && read_file2 >> num2) {
            while (true) {
                if (num1 < num2) {
                    write_result << num1 << ' ';
                    if (!(read_file1 >> num1)) break;
                }
                else {
                    write_result << num2 << ' ';
                    if (!(read_file2 >> num2)) break;
                }
            }
        }

        while (read_file1 >> num1) {
            write_result << num1 << ' ';
        }

        while (read_file2 >> num2) {
            write_result << num2 << ' ';
        }

        read_file1.close();
        read_file2.close();
        write_result.close();

        read_result.open(res);
        write_file1.open(link[0], ios::trunc);

        if (read_result) {
            write_file1 << read_result.rdbuf();
        }

        read_result.close();
        write_file1.close();
    }

    read_file1.open(link[0]);
    write_result.open(res, ios::trunc);

    if (read_file1)
        write_result << read_file1.rdbuf();

    read_file1.close();
    write_result.close();

}








