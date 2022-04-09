#include <iostream>

using namespace std;

int main()
{
    double a1, a2, b1, b2, c1, c2, x, y;

    a1 = -1;
    b1 = 2;
    c1 = 3;

    a2 = 3;
    b2 = 4;
    c2 = 11;

    //a1x+b1y=c1
    //a2x+b2y=c2

    y = (c2 - ((c1 * a2) / a1))/(b2 - ((b1 * a2) / a1));
    x = (c1 / a1) - (b1 / a1) * y;

    cout << "x = " << x << ", y = " << y;

    return 0;
}