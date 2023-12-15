#include <iostream>
#include "BinaryTree.h"
using namespace std;
//8(3(1,6(4,7)),10(,14(13,)))
int main()
{
	setlocale(LC_ALL, "ru");
	BinaryTree tree;
	string bintree;
	cout << "Введите бинарное дерево в виде линейно-скобочной записи: ";
	cin >> bintree;
	tree.createTree(bintree);

    bool end = false;
    int choice, value;
    while (!end) {
        cout << "Выберите операцию:" << '\n';
        cout << "1. Добавить узел" << '\n';
        cout << "2. Удалить узел" << '\n';
        cout << "3. Найти узел" << '\n';
        cout << "4. Вывести БДН" << '\n';
        cout << "5. Выйти из программы" << '\n';
        cout << "Введите номер операции: ";
        cin >> choice;
        switch (choice) {
        case 1:
            cout << "Введите значение: ";
            cin >> value;
            tree.AddElement(value);
            cout << '\n';
            break;
        case 2:
            cout << "Введите значение: ";
            cin >> value;
            tree.DeleteElement(value);
            cout << '\n';
            break;
        case 3:
            cout << "Введите значение: ";
            cin >> value;
            cout << '\n';
            cout << "Данный узел : ";
            tree.FindeElement(value);
            cout << '\n';
            break;
        case 4:
            cout << '\n';
            cout << "Бинарное дерево: ";
            tree.printBinaryTree();
            cout << '\n';
            break;

        case 5:
            cout << '\n';
            cout << "Бинарное дерево: ";
            tree.printBinaryTree();
            end = true;
            cout << '\n';
            break;
        }
    }
}

