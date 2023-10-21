#include <iostream>
#include "TrapezoidMetod.h"

void TrapezoidMetod::Calcer(double(*function)(double), double left_border, double right_border)
{
    double step = ((right_border) - left_border) / getNumPoints();
    double x = left_border;
    double result = 0.0;

    while (x < right_border)
    {
        double argument_1 = (function(x) + function(x + step)) / 2;
        double argument_2 = step;
        result += argument_1 * argument_2;
        x += step;
    }
    
   std::cout << "Метод трапеции.\n" 
         << "Результат: " << result << '\n' 
         << "Шаг: " << step << '\n' 
         << "Колличество точек: " << getNumPoints() 
         << '\n' << '\n';
}
