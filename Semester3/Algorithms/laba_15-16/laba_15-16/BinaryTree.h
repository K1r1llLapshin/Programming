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
	//����������� ������ 
	void preorder_recursive(Node* binTree);// ������ 
	void inorder_recursive(Node* binTree);// �����������
	void postorder_recursive(Node* binTree);// ��������
	//�� ����������� ����
	void preorder(Node* binTree);// ������
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

