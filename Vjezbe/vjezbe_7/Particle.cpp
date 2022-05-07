#define _USE_MATH_DEFINES

#include <math.h>
#include <Particle.h>

void Particle::move()
{
    v_x += double(0);
    v_y += g * dt;

    x += v_x * dt;
    y += v_y * dt;

    t += dt;  
}

Particle::Particle(double v, double kut, double x_0, double y_0, double korak)
{
    dt = korak;
    v_x = v * cos(M_PI * kut / 180);
    v_y = v * sin(M_PI * kut / 180);
    x = x_0;
    y = y_0;
}

double Particle::time()
{
    double vrijeme = 0;

    while(y >= 0)
    {
        move();
    }

    vrijeme = t;

    return vrijeme;
}

double Particle::range()
{
    double domet = 0;

    while(y >= 0)
    {
        move();
    }

    domet = x;

    return domet;
}