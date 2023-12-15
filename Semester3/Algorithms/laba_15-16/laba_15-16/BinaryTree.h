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
	//рекурсивные обходы 
	void preorder_recursive(Node* binTree);// прямой 
	void inorder_recursive(Node* binTree);// центральный
	void postorder_recursive(Node* binTree);// концевой
	//не рекурсивный оход
	void preorder(Node* binTree);// прямой
public:

	BinaryTree() 
	{
		binaryTree.root = NULL;
		binaryTree.left = NULL;
		binaryTree.right = NULL;
	};

	void createTree(string list);
	void printTree_preorder_recursive();
	void printTree_inorder_recursive();
	void printTree_postorder_recursive();
	void printTree_preorder();
};

