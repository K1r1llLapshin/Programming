#pragma once
#include <iostream>
#include <vector> 
using namespace std;

template <typename T>
class Array3D
{
private:
	vector<T> array3d;
	int size_1{}, size_2{}, size_3{};

public:
	Array3D() {};
	Array3D(int size_1, int size_2, int size_3)
	{
		array3d.resize(size_1 * size_2 * size_3);
		this->size_1 = size_1;
		this->size_2 = size_2;
		this->size_3 = size_3;
	}	
	
	T& operator()(int i, int j, int k)
	{
		return array3d[i * size_2 * size_3 + j * size_3 + k];
	}

	friend ostream& operator<<(ostream& os,  Array3D<T>& array)
	{
		for (int i = 0; i < array.size_1; ++i)
		{
			for (int j = 0; j < array.size_2; ++j)
			{
				for (int k = 0; k < array.size_3; ++k)
				{
					os << array(i, j, k) << " ";
				}
				os << '\n';
			}
			os << '\n';
		}
		return os;
	}

	static Array3D<T> CreateFill(int size_1, int size_2, int size_3, T value)
	{
		Array3D<T> array(size_1, size_2, size_3);
		for (int i = 0; i < size_1; ++i)
			for (int j = 0; j < size_2; ++j)
				for (int k = 0; k < size_3; ++k)
					array(i, j, k) = value;
		return array;
	}

	Array3D<T> getValue0(int i)
	{
		Array3D<T> res(1, size_2, size_3);

		for (int j = 0; j < size_2; ++j)
			for (int k = 0; k < size_3; ++k)
				res(0, j, k) = array3d[i * size_2 * size_3 + j * size_3 + k];
		return res;
	}
	Array3D<T> getValue1(int j)
	{
		Array3D<T> res(1, size_1, size_3);

		for (int i = 0; i < size_1; ++i)
			for (int k = 0; k < size_3; ++k)
				res(0, i, k) = array3d[i * size_2 * size_3 + j * size_3 + k];
		return res;
	}
	Array3D<T> getValue2(int k)
	{
		Array3D<T> res(1, size_1, size_2);

		for (int i = 0; i < size_1; ++i)
			for (int j = 0; j < size_2; ++j)
				res(0, i, j) = array3d[i * size_2 * size_3 + j * size_3 + k];
		return res;
	}
	Array3D<T> getValue01(int i, int j)
	{
		Array3D<T> res(1, 1, size_3);
		for (int k = 0; k < size_3; k++) {
			res(0, 0, k) = array3d[i * size_2 * size_3 + j * size_3 + k];
		}
		return res;
	}
	Array3D<T> getValue02(int j, int k)
	{
		Array3D<T> res(1, 1, size_1);
		for (int i = 0; i < size_1; i++) {
			res(0, 0, i) = array3d[i * size_2 * size_3 + j * size_3 + k];
		}
		return res;
	}
	Array3D<T> getValue12(int i, int k)
	{
		Array3D<T> res(1, 1, size_2);
		for (int j = 0; j < size_2; j++) {
			res(0, 0, j) = array3d[i * size_2 * size_3 + j * size_3 + k];
		}
		return res;
	}
	T getValue(int i, int j, int k) 
	{
		int index = i * size_2 * size_3 + j * size_3 + k;
		return array3d[index];
	}

	void setValue0(int i, T value)
	{
		for (int j = 0; j < size_2; ++j)
			for (int k = 0; k < size_3; ++k)
				array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue1(int j, T value)
	{
		for (int i = 0; i < size_1; ++i)
			for (int k = 0; k < size_3; ++k)
				array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue2(int k, T value)
	{
		for (int i = 0; i < size_1; ++i)
			for (int j = 0; j < size_2; ++j)
				array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue01(int i, int j, T value)
	{
		for (int k = 0; k < size_3; ++k)
			array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue02(int j, int k, T value)
	{
		for (int i = 0; i < size_1; ++i)
			array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue12(int i, int k, T value)
	{
		for (int j = 0; j < size_2; ++j)
			array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}
	void setValue(int i, int j, int k, T value)
	{
		array3d[i * size_2 * size_3 + j * size_3 + k] = value;
	}

	

	

	
	



	 
};


