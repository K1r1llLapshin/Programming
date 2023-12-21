#include "Keyboard.h"
#include <cstring>
#include <cctype>
void Keyboard::setKeyboard(Key key)
{
	keys.push_back(key);
}

void Keyboard::pressKey(Key key)
{
	Key this_key;
	int count_ = 0;
	for (int count = 0; count < keys.size(); ++count)
	{
		int count_ = 0;
		if (keys[count] == key)
		{
			this_key = key;
			count_ = count;
		}

		else
			cout << "íåò òàêîé êëàâèøè";

	}
	switch (this_key.getKeyCommand())
	{
		
		case Press:
			if (tab == true)
				for(int i = 0; i<tab_count; ++i)
					cout << '\t';
			if (caps == true)
			{
				int key_nam = this_key.getName_Key()[0];
				char key_str = toupper(key_nam);
				cout << key_str;
			}
			else
				cout << this_key.getName_Key();
			for (int count_ = 0; count_ < 40 - this_key.getName_Key().size(); ++count_)
			{
				cout << ' ';
				count_++;
			}
			cout << "| " << "Press " + this_key.getName_Key() << '\n';
			break;
		case Caps:
			for (int count_ = 0; count_ < 42; ++count_)
			{
				cout << ' ';
				count_++;
			}
			cout << "| " << "Caps " << '\n';
			caps = true;
			break;
		case Tab:
			tab_count++;
			for (int count_ = 0; count_ < 42; ++count_)
			{
				cout << ' ';
				count_++;
			}
			cout << "| " << "Tab " << '\n';
			tab = true;
			break;
		case VolumeUp:
			volume += 10;
			cout << "Volum: " << volume << '%';
			for (int count_ = 0; count_ < 22; ++count_)
			{
				cout << ' ';
				count_++;
			}
			cout << "| " << "VolumeUp" << '\n';
			
			break;
		case VolumeDown:
			volume -= 10;
			cout << "Volum: " << volume << '%';
			for (int count_ = 0; count_ < 22; ++count_)
			{
				cout << ' ';
				count_++;
			}
			cout << "| " << "VolumeDown" << '\n';
			
			break;
		default:
			break;
	}

	
}


void Keyboard::undo()
{
	if (tab == true)
	{
		tab = false;
		tab_count = 0;
	}
	if (caps == true)
		caps = false;

}
