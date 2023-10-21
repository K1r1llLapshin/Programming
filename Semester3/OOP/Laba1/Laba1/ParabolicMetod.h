#pragma once
#include "Integral.h"
class ParabolicMetod : public Integral
{
public:
    void Calcer(double (*function)(double), double left_border, double right_border) override;
};

