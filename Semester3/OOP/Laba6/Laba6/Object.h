#pragma once
#include <iostream>
#include <string>
using namespace std;
class Control {
public:
	virtual void get() = 0;
	virtual void set(string str) = 0;
};

class TextBox: public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "Выполнилась функция get() для класса TextBox "+ str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infTextBox()
	{
		cout << "Информация TextBox" << '\t' + str << std::endl;
	}


};

class ComboBox : public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "Выполнилась функция get() для класса ComboBox " + str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infComboBox()
	{
		cout << "Информация ComboBox " << '\t' + str << std::endl;
	}
};

class DataEdit: public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "Выполнилась функция get() для класса DataEdit " + str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infDataEdit()
	{
		cout << "Информация DataEdit" << '\t' + str << std::endl;
	}
};

class RichTextBox : public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "Выполнилась функция get() для класса RichTextBox "+ str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infRichTextBox()
	{
		cout << "Информация RichTextBox" << '\t' + str << std::endl;
	}
};