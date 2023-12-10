#pragma once
#include "Repository.h"
#include "User.h"
#include "Memory.h"
#include "UserRepository.h"

class MemoryUserRepository: public MemoryRepository<User>, public UserRepository
{
public:
	User* getById(int id) override
	{
		for (User* user : mItem)
		{
			if (user->getId() == id)
				return user;
		}
	}
	User* getByName(string name)
	{
		for (User* user : mItem)
		{
			if (user->getName() == name)
				return user;
		}
	}
	User* getByEmail(string email)
	{
		for (User* user : mItem)
		{
			if (user->getEmail() == email)
				return user;
		}
	}
	vector<User*> getByCity(string city)
	{
		vector<User*> res;
		for (User* user : mItem)
			if (user->getCity() == city)
				res.push_back(user);
		return res;
	}
	vector <User*> getByGender(Gender gender)
	{
		vector<User*> res;
		for (User* user : mItem)
			if (user->getGender() == gender)
				res.push_back(user);
		return res;
	}
};

