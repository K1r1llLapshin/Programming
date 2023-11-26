#include <iostream>
#include "BinaryTree.h"
int main()
{
	BinaryTree tree;
	string input = "8(3(1,6(4,7)),10(,14(13,)))";
	tree.createTree(input);
	tree.printTree();
}


