#pragma once
#include <string>
#include <iostream>
using namespace std;

enum Commands
{
	Tab,
	Caps,
	VolumeUp, 
	VolumeDown,
	Press
};


class Key
{
private:
	struct Keys
	{
		string name_key;
		Commands command;
	};

	Keys key;
public:
	Key() {};
	void setKey(string name_key, Commands command);
	Commands getKeyCommand();
	void overrideKey (Commands command);
	string getName_Key();
	Key& operator=(Key& key);
	bool operator==(Key& key);
};

