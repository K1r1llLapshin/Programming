#pragma once
#include "Object.h"
class OS {
public:
	virtual TextBox* creatTextBox() = 0;
	virtual ComboBox* creatComboBox() = 0;
	virtual DataEdit* creatDataEdit() = 0;
	virtual RichTextBox* creatRichTextBox() = 0;
};

class Window: public OS {
public:
	TextBox* creatTextBox() override
	{
		return new TextBox();
	}
	ComboBox* creatComboBox() override
	{
		return new ComboBox();
	}
	DataEdit* creatDataEdit() override
	{
		return new DataEdit();
	}
	RichTextBox* creatRichTextBox() override
	{
		return new RichTextBox();
	}
};

class Linux : public OS {
public:
	TextBox* creatTextBox() override
	{
		return new TextBox();
	}
	ComboBox* creatComboBox() override
	{
		return new ComboBox();
	}
	DataEdit* creatDataEdit() override
	{
		return new DataEdit();
	}
	RichTextBox* creatRichTextBox() override
	{
		return new RichTextBox();
	}
};

class Mac: public OS {
public:
	TextBox* creatTextBox() override
	{
		return new TextBox();
	}
	ComboBox* creatComboBox() override
	{
		return new ComboBox();
	}
	DataEdit* creatDataEdit() override
	{
		return new DataEdit();
	}
	RichTextBox* creatRichTextBox() override
	{
		return new RichTextBox();
	}
};
