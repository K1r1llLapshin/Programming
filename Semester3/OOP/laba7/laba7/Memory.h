#pragma once
#include "Repository.h"

template <class T>
class MemoryRepository: public IRepository<T>
{
public:
	vector<T*> mItem;
	void Add(T* item) override
	{
		mItem.push_back(item);
	}
	void Update(T* item) override
	{
	
	}
	void Delete(T* item) override
	{
		auto it = find(mItem.begin(), mItem.end(), item);

		if (it != mItem.end()) {
			mItem.erase(it);
		}
	}
	vector<T*> Get(const string where, const string orderBy) override
	{
		return mItem;
	}
};

