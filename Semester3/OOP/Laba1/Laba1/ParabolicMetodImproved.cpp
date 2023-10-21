#include <iostream>
#include "ParabolicMetodImproved.h"

void ParabolicMetodImproved::Calcer(double(*function)(double), double left_border, double right_border)
{
    double step = ((right_border)-left_border) / getNumPoints();
    double x = left_border;
    double result = 0.0;

    while (x < right_border)
    {
        double argument_1 = step / 6;
        double argument_2 = (2 * x + step) / 2;
        result += argument_1 * (function(x) + 4 * function(argument_2) + function(x + step));
        x += step;

    }
    std::cout << "Метод парабол (метод Симсона) Улучшенный.\n"
        << "Результат: " << result << '\n'
        << "Шаг: " << step << '\n'
        << "Колличество точек: " << getNumPoints()
        << '\n' << '\n';
}
