#include "Key.h"

void Key::setKey(string name_key, Commands command)
{
	key.name_key = name_key;
	key.command = command;
}

Commands Key::getKeyCommand()
{
	return this->key.command;
}

void Key::overrideKey (Commands command)
{
	key.command = command;
	for (int count_ = 0; count_ < 42; ++count_)
	{
		cout << ' ';
		count_++;
	}
	cout << "| " << "Override " << '\n';
}

string Key::getName_Key()
{
	return this->key.name_key;
	
}

Key& Key::operator=(Key& key)
{
	if (this != &key) {
		this->key.name_key = key.key.name_key;
		this->key.command = key.key.command;
	}
	return *this;
}

bool Key::operator==(Key& key)
{
	this->key.name_key == key.key.name_key;
	this->key.command == key.key.command;
	return this;
}



