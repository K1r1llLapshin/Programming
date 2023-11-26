#pragma once
#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

class BinaryTree
{
private:
	struct Node
	{
		int root;
		Node* left;
		Node* right;
	};

	Node binaryTree;

	Node* createNode(int data);
	void printTree(Node* node);
public:

	BinaryTree() {};
	void createTree(string list);
	void printTree();
};

