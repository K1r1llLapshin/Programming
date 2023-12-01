#pragma once
#include<windows.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Alphabet
{
private:   
    char letter;
    vector<vector<char>> Letters(char letter, char syb);
    int GetColor(string color);
public:
    Alphabet() {};
    vector<vector<char>> GivenLetter(char letter, char symbol);
    void PrintText(string text, char symbol, string color, int y, int x);

};

