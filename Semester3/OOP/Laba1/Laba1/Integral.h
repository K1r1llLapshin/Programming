#pragma once
class Integral
{
private:
    int numPoints = 10000;
   
public:
    virtual void Calcer(double (*function)(double), double left_border, double right_border) = 0;

    int getNumPoints()
    {
        return numPoints;
    }
};

