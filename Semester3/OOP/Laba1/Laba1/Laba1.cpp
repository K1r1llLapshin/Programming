#include <iostream>
#include <cmath>
#include "ParabolicMetod.h"
#include "TrapezoidMetod.h"
#include "ParabolicMetodImproved.h"

double function(double x) {
    return cos(x)+pow(x,2);
}

int main() {
    setlocale(LC_ALL, "ru");
    
    TrapezoidMetod integral_tr;
    integral_tr.Calcer(function, -1, 10);
    
    ParabolicMetod integral_pr;
    integral_pr.Calcer(function, -1, 10);
  
    ParabolicMetodImproved integral_prim;
    integral_prim.Calcer(function, -1, 10);


    return 0;
}