#include <iostream>
#include "ParabolicMetod.h"

void ParabolicMetod::Calcer(double(*function)(double), double left_border, double right_border) 
{
    double argunet_1 = (right_border - left_border) / 6;
    double argument_2 = (left_border + right_border) / 2;
    double resulst = argunet_1 * (function(left_border) + 4 * function(argument_2) + function(right_border));

    std::cout << "Метод парабол (метод Симсона).\n"
        << "Результат: " << resulst << '\n'
        << "Шаг: ---\n"
        << "Количество точек: ---\n" << '\n'; 

}
