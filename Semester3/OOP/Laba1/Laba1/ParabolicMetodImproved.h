#pragma once
#include "Integral.h"
class ParabolicMetodImproved : public Integral
{
public:
	void Calcer(double (*function)(double), double left_border, double right_border)  override;

};

