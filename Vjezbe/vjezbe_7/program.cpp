#include <iostream>
#include <Particle.h>

using namespace std;

int main()
{
    Particle p1(100, 45, 0, 0);
    cout << "Domet je: " << p1.range() << "m" << endl;
    cout << "Vrijeme gibanja je: " << p1.time() << "s" << endl;

    Particle p2(10, 60, 0, 0);
    cout << "Domet je: " << p2.range() << "m" << endl;
    cout << "Vrijeme gibanja je: " << p2.time() << "s" << endl;

    return 0;
}