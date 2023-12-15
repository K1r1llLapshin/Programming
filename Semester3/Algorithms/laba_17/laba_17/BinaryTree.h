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
	bool preorder_recursive(Node* binTree, int voide);// прямой 

	void printTree(Node* binTree);
	Node* Add(Node* binTree, int value);
	Node* Delete(Node* binTree, int value);
	Node* minValueNode(Node* node);
	Node* searchNode(Node* binTree, int value);
public:

	BinaryTree() 
	{
		binaryTree.root = NULL;
		binaryTree.left = NULL;
		binaryTree.right = NULL;
	};

	void createTree(string list);
	void printBinaryTree();
	void AddElement(int value);
	void DeleteElement(int value);
	void FindeElement(int value);
};

