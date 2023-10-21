#pragma once

int main() {
    setlocale(LC_ALL, "ru");
    char* h;
    sprintf(h, "%f", function(10));
    std::cout << h << '\n';
    TrapezoidMetod integral_tr;
    integral_tr.Calcer(function, -1, 10);

    ParabolicMetod integral_pr;
    integral_pr.Calcer(function, -1, 10);

    ParabolicMetodImproved integral_prim;
    integral_prim.Calcer(function, -1, 10);


    return 0;
}
