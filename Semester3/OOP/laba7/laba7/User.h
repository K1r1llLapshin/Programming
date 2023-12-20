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
	void setName(const string& mName);
	void setEmail(const string& mEmail);
	void setPhone(const string& mPhone);
	void setCity(const string& mCity);
	void setGender(Gender mGender);

	~User() {};
};


