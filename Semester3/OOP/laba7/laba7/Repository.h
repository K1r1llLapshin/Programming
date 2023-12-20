#pragma once
#include<vector>
#include<string>
using namespace std;

template<class T>
class IRepository
{
public:
	virtual void Add(T* item) = 0;
	virtual void Update(T* item) = 0;
	virtual void Delete(T* item) = 0;
	virtual vector<T*> Get(const string& where, const string& orderBy) = 0;
};





