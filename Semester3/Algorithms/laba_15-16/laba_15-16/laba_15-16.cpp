#include <iostream>
#include "BinaryTree.h"
int main()
{
	setlocale(LC_ALL, "ru");
	BinaryTree tree;
	string input = "8(3(1,6(4,7)),10(,14(13,)))";
	tree.createTree(input);

	cout << "Рекурсивные обходы: " << '\n' << '\t';
	cout << "* Прямой обход: ";
	tree.printTree_preorder_recursive();
	cout << '\n' << '\t';
	cout << "* Центральный обход: ";
	tree.printTree_inorder_recursive();
	cout << '\n' << '\t';
	cout << "* Концевой обход: ";
	tree.printTree_postorder_recursive();
	cout << '\n' << '\n';
	cout << "Не рекурсивные обход: " << '\n' << '\t';
	cout << "* Прямой обход: ";
	tree.printTree_preorder();
	cout << '\n';
}