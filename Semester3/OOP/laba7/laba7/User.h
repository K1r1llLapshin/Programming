#pragma once
#include "Repository.h"

enum Gender { Male, Female };
class User
{
private:
	int mId;
	string mName;
	string mEmail;
	string mPhone;
	string mCity;
	Gender mGender;

public:
	User() {};

	int getId();
	string getName();
	string getEmail();
	string getPhone();
	string getCity();
	Gender getGender();

	void setId(int mId);
	void setName(string mName);
	void setEmail(string mEmail);
	void setPhone(string mPhone);
	void setCity(string mCity);
	void setGender(Gender mGender);

	~User() {};
};


