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
    stack<Node*> s;
    Node* help_node;
    int value, count = 0;

    while (list[count] != '\0')
    {
        if (list[count] == '(')
        {
            Node* newNode = createNode(value);
            if (s.empty())
                binaryTree = *newNode;
            else
            {
                help_node = s.top();
                if (help_node->left == NULL)
                    help_node->left = newNode;
                else
                    help_node->right = newNode;
            }
            s.push(newNode);
        }
        else if (list[count] == ')')
            s.pop();
        else if (isdigit(list[count]))
        {
            int num = 0;
            while (isdigit(list[count]))
            {
                num = num * 10 + (list[count] - '0');
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