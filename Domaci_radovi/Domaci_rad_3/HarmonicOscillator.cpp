#include <HarmonicOscillator.h>
#include <fstream>
#include <iostream>

void HarmonicOscillator::move()
{
    int i = 0;
    std::ofstream datoteka;
    datoteka.open("datoteka.txt");

    while(t[i] < vrijeme)
    {
        a[i] = -k/m * x[i];
        v[i+1] = v[i] + a[i] * dt;
        x[i+1] = x[i] + v[i+1] * dt;
        t[i+1] = t[i] + dt;

        i++; 
    }

    for(int j = 0; j < i; j++)
    {
        datoteka << t[j] << "|" << a[j] << "|" << v[j] << "|" << x[j] << "\n";   
    }
}

HarmonicOscillator::HarmonicOscillator(double x_0, double masa, double vrijemeOscilacije, double konstantaOpruge, double korak)
{
    x[0] = x_0;
    v[0] = 0.;
    //a[0] = -konstantaOpruge * x_0 / masa;
    t[0] = 0;
    dt = korak;
    m = masa;
    k = konstantaOpruge;
    vrijeme = vrijemeOscilacije;
}

void HarmonicOscillator::oscillate()
{
    move();
}