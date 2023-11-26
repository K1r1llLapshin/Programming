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
void BinaryTree::printTree(Node* node)
{
    if (node == NULL)
        return;

    printTree(node->left);
    cout << node->root << " ";
    printTree(node->right);
}

//-------------------------------------------------------------------------------

void BinaryTree::createTree(string list)
{
	stack<Node*> time_node;
	Node* help_node;
	int value = 0;
	int count = 0;
	
	while (list[count] != '\0')
	{
		if (list[count] == '(')
		{
			Node* new_node = createNode(value);

			if (time_node.empty())
				binaryTree = *new_node;
			else
			{
				help_node = new_node;
				time_node.push(help_node);
			}
			
		}
		else if (list[count] == ',')
		{
			if (time_node.empty())
				binaryTree.left = NULL;
			else
				binaryTree.left = time_node.top();
			time_node.pop();
		}
		else if (list[count] == ')')
		{
			if(time_node.empty())
				binaryTree.right = NULL;
			else 
				binaryTree.right = time_node.top();
			time_node.pop();
		}
		else if (isdigit(list[count]))
		{
			int num = 0;
			while (isdigit(list[count]))
			{
				num = num * 10 + (list[count] - '\0');
				count++;
			}
			value = num;
			count--;
		}
		count++;
	}

}


void BinaryTree::printTree()
{
    printTree(&binaryTree);
}