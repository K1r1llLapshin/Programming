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
		cout << "����������� ������� get() ��� ������ TextBox "+ str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infTextBox()
	{
		cout << "���������� TextBox" << '\t' + str << std::endl;
	}


};

class ComboBox : public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "����������� ������� get() ��� ������ ComboBox " + str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infComboBox()
	{
		cout << "���������� ComboBox " << '\t' + str << std::endl;
	}
};

class DataEdit: public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "����������� ������� get() ��� ������ DataEdit " + str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infDataEdit()
	{
		cout << "���������� DataEdit" << '\t' + str << std::endl;
	}
};

class RichTextBox : public Control {
private:
	string str;
public:
	void get() override
	{
		cout << "����������� ������� get() ��� ������ RichTextBox "+ str << std::endl;
	}

	void set(string str) override
	{
		this->str = str;
	}

	void infRichTextBox()
	{
		cout << "���������� RichTextBox" << '\t' + str << std::endl;
	}
};