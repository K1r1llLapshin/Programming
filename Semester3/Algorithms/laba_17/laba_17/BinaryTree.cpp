#include "BinaryTree.h"

BinaryTree::Node* BinaryTree::createNode(int data)
{
	Node* newNode = new Node();
	if (!newNode) {
		cout << "ќшибка выделени€ пам€ти!" << endl;
		return NULL;
	}
	newNode->root = data;
	newNode->left = newNode->right = NULL;
	return newNode;
}

 bool BinaryTree::preorder_recursive(Node* binTree, int value)
{
	if (binTree != NULL)
	{
		if (binTree->root == value)
			return true;
		if (preorder_recursive(binTree->left, value))
			return true;
		if (preorder_recursive(binTree->right, value))
			return true;
	}
	return false;
}

void BinaryTree::printTree(Node* binTree)
{
	if (binTree == NULL)
		return;

	if (binTree->left == NULL && binTree->right == NULL)
	{ 
		cout << binTree->root;
		return;
	}

	cout << binTree->root << '(';

	if (binTree->left != NULL)
		printTree(binTree->left);

	cout << ',';

	if (binTree->right != NULL)
		printTree(binTree->right);

	cout << ')';
}

BinaryTree::Node* BinaryTree::Add(Node* binTree, int value)
{
	if (binTree == NULL) {
		// ≈сли дерево пустое, создаем новый узел и делаем его корнем
		binTree = createNode(value);
	}

	// –екурсивно переходим к левому или правому поддереву 
	if (value < binTree->root) {
		binTree->left = Add(binTree->left, value);
	}
	else if (value > binTree->root) {
		binTree->right = Add(binTree->right, value);
	}

	// ¬озвращаем указ
	return binTree;
}

BinaryTree::Node* BinaryTree::minValueNode(Node* binTree)
{
	Node* current = binTree;

	while (current && current->left != NULL)
	{
		current = current->left;
	}

	return current;
}
BinaryTree::Node* BinaryTree::Delete(BinaryTree::Node* binTree, int value)
{
	if (binTree == NULL)
	{
		return binTree;
	}

	if (value < binTree->root)
	{
		binTree->left = Delete(binTree->left, value);
	}
	else if (value > binTree->root)
	{
		binTree->right = Delete(binTree->right, value);
	}
	else
	{
		if (binTree->left == NULL)
		{
			Node* temp = binTree->right;
			delete binTree;
			return temp;
		}
		else if (binTree->right == NULL)
		{
			Node* temp = binTree->left;
			delete binTree;
			return temp;
		}

		Node* temp = minValueNode(binTree->right);
		binTree->root = temp->root;
		binTree->right = Delete(binTree->right, temp->root);
	}

	return binTree;
}

BinaryTree::Node* BinaryTree::searchNode(Node* binTree, int value) {
	if (binTree == nullptr || binTree->root == value) {
		return binTree;
	}
	if (value < binTree->root) {
		return searchNode(binTree->left, value);
	}
	return searchNode(binTree->right, value);
}

//-------------------------------------------------------------------------------

void BinaryTree::createTree(string list)
{
	stack<Node*> nodes;
	int value;
	int count_ = 0;
	int sign = 1;
	while (list[count_] != '\0')
	{
		if (list[count_] == '-' && isdigit(list[count_+1]))
			sign = -1;
		if (isdigit(list[count_]))
		{
			int num = 0;
			while (isdigit(list[count_]))
			{
				num = num * 10 + (list[count_] - '0');
				count_++;
			}
			
			value = num*sign;
			count_--;
			sign = 1;
		}
		else if (list[count_] == '(')
		{
			Node* new_node = createNode(value);
			nodes.push(new_node);
		}
		else if (list[count_] == ',')
		{
			if (list[count_ - 1] == '(')
			{
				Node* top_node = nodes.top();
				nodes.pop();
				top_node->left = NULL;
				nodes.push(top_node);
			}
			else if (list[count_ - 1] == ')')
			{
				Node* top_node2 = nodes.top();
				nodes.pop();
				Node* top_node1 = nodes.top();
				nodes.pop();
				top_node1->left = top_node2;
				nodes.push(top_node1);
			}
			else
			{
				Node* top_node = nodes.top();
				nodes.pop();
				top_node->left = createNode(value);
				nodes.push(top_node);
			}

		}
		else if (list[count_] == ')')
		{
			if (list[count_ - 1] == ',')
			{
				Node* top_node = nodes.top();
				nodes.pop();
				top_node->right = NULL;
				nodes.push(top_node);
			}
			else if (list[count_ - 1] == ')')
			{
				Node* top_node2 = nodes.top();
				nodes.pop();
				Node* top_node1 = nodes.top();
				nodes.pop();
				top_node1->right = top_node2;
				nodes.push(top_node1);
			}
			else
			{
				Node* top_node = nodes.top();
				nodes.pop();
				top_node->right = createNode(value);
				nodes.push(top_node);
			}

		}
		count_++;
	}
	binaryTree = *nodes.top();
}

void BinaryTree::printBinaryTree()
{
		printTree(&binaryTree);
}

void BinaryTree::AddElement(int value)
{
	if (preorder_recursive(&binaryTree, value))
	{
		cout << "Ёлемент уже есть в дереве!";
		cout << '\n';
	}
	else 
		binaryTree = *Add(&binaryTree, value);
}

void BinaryTree::DeleteElement(int value)
{
	if (preorder_recursive(&binaryTree, value) == false)
	{
		cout << "Ёлементa нет в дереве!";
		cout << '\n';
	}
	else
		binaryTree = *Delete(&binaryTree, value);
}

void BinaryTree::FindeElement(int value)
{
	if (preorder_recursive(&binaryTree, value) == false)
	{
		cout << "Ёлементa нет в дереве!";
		cout << '\n';
	}
	else
		cout << searchNode(&binaryTree, value)->root;
}




