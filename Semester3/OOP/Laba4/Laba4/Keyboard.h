#pragma once
#include "Key.h"
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Keyboard
{
private:
	vector<Key> keys;

	int volume = 0;
	int tab_count = 0;
	bool tab = false;
	bool caps = false;
	
public:
	void setKeyboard(Key key);

	void pressKey(Key key);

	void undo();

};

