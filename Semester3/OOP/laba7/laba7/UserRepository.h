#pragma once
#include "User.h"
class UserRepository
{
public:

	virtual User* getById(int id) = 0;
	virtual User* getByName(const string& name) = 0;
	virtual User* getByEmail(const string& email) = 0;
	virtual vector<User*> getByCity(const string& city) = 0;
	virtual vector <User*> getByGender(Gender gender) = 0;

};

