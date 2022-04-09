#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void jednadzbaPravca(double x1, double y1, double x2, double y2)
{
    double k, l;
    k = (y1 - y2)/(x1 - x2);
    l = -k*x1 + y1;

    string jednadzba = "Jednadzba pravca je " + to_string(k) + "x" + " + " + "(" + to_string(l) + ")";

    cout << jednadzba << endl;
}

string tockaIKruznica(double x_s, double y_s, double x1, double y1, double radijus)
{
    string lokacijaTocke;
    double uvjetLijevaStrana = pow(x_s - x1, 2) + pow(y_s - y1, 2);

    if(uvjetLijevaStrana > pow(radijus, 2))
    {
        lokacijaTocke = "Tocka se nalazi van kruznice";
    }
    else if(uvjetLijevaStrana < pow(radijus, 2))
    {
        lokacijaTocke = "Tocka se nalazi unutar kruznice";
    }
    else
    {
        lokacijaTocke = "Tocka se nalazi na kruznici";
    }

    return lokacijaTocke;
}


int main()
{
    jednadzbaPravca(1, 2, 3, 4);
    cout << tockaIKruznica(1, 1, 1, 1, 1) << endl;

    return 0;
}