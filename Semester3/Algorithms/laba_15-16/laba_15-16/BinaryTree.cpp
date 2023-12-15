#include "BinaryTree.h"


BinaryTree::Node* BinaryTree::createNode(int data)
{
	Node* newNode = new Node();
	if (!newNode) {
		cout << "Ошибка выделения памяти!" << endl;
		return NULL;
	}
	newNode->root = data;
	newNode->left = newNode->right = NULL;
	return newNode;
}

void BinaryTree::preorder_recursive(Node* binTree)
{
	if (binTree != NULL)
	{
		cout << binTree->root << " "; // выводим значение текущего узла
		preorder_recursive(binTree->left); // рекурсивно обходим левое поддерево
		preorder_recursive(binTree->right); // рекурсивно обходим правое поддерево
	}
}
void BinaryTree::inorder_recursive(Node* binTree)
{
	if (binTree != NULL)
	{
		inorder_recursive(binTree->left);
		cout << binTree->root << " ";
		inorder_recursive(binTree->right);
		
	}
}
void BinaryTree::postorder_recursive(Node* binTree)
{
	if (binTree != NULL)
	{
		postorder_recursive(binTree->left);
		postorder_recursive(binTree->right);
		cout << binTree->root << ' ';
	}
}

void BinaryTree::preorder(Node* binTree)
{
	if (binTree == NULL)
		return;
	else
	{
		stack<Node*> nodes;
		nodes.push(binTree);

		while (!nodes.empty())
		{
			Node* node_ = nodes.top();
			nodes.pop();

			cout << node_->root << ' ';

			if (node_->right != NULL)
				nodes.push(node_->right);
			if (node_->left != NULL)
				nodes.push(node_->left);
		}
	}
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
void BinaryTree::printTree_preorder_recursive()
{
	preorder_recursive(&binaryTree);
}
void BinaryTree::printTree_inorder_recursive()
{
	inorder_recursive(&binaryTree);
}
void BinaryTree::printTree_postorder_recursive()
{
	postorder_recursive(&binaryTree);
}
void BinaryTree::printTree_preorder()
{
	preorder(&binaryTree);
}