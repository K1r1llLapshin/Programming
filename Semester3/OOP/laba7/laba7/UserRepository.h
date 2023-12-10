#pragma once
#include "User.h"
class UserRepository
{
public:

	virtual User* getById(int id) = 0;
	virtual User* getByName(string name) = 0;
	virtual User* getByEmail(string email) = 0;
	virtual vector<User*> getByCity(string city) = 0;
	virtual vector <User*> getByGender(Gender gender) = 0;

};

