#include <iostream>

using namespace std;

void dvijeLinearneJednadzbe(double a1, double b1, double c1, double a2, double b2, double c2)
{
    double x, y;

    if(a1 == 0 && b1 != 0 && a2 != 0)
    {
        y = c1 / b1;
        x = (c2 - b2 * y) / a2;

        cout << "x = " << x << ", y = " << y; 
    }
    else if(a1 != 0 && b1 == 0 && b2 != 0)
    {
        x = c1 / a1;
        y = (c2 - a2 * x) / b2;

        cout << "x = " << x << ", y = " << y;
    }
    else if(a2 == 0 && b2 != 0 && a1 != 0)
    {
        y = c2 / b2;
        x = (c1 - b1 * y) / a1;

        cout << "x = " << x << ", y = " << y;
    }
    else if(a2 != 0 && b2 == 0 && b1 != 0)
    {
        x = c2 / a2;
        y = (c1 - a1 * x) / b1;

        cout << "x = " << x << ", y = " << y;
    }
    else if(a1 != 0 && b1 != 0 && a2 != 0 && b2 != 0)
    {
        y = (c2 - ((c1 * a2) / a1))/(b2 - ((b1 * a2) / a1));
        x = (c1 / a1) - (b1 / a1) * y;

        cout << "x = " << x << ", y = " << y;
    }
    else 
    {
        cout << "Jednadzbe nemaju jedinstvena rjesenja/uopce nemaju rjesenja";
    }
}

int main()
{
    double a1, a2, b1, b2, c1, c2;

    a1 = 1;
    b1 = 2;
    c1 = 3;

    a2 = 4;
    b2 = 5;
    c2 = 6;

    dvijeLinearneJednadzbe(a1, b1, c1, a2, b2, c2);

    return 0;
}