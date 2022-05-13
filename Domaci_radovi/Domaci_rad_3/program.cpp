#include <iostream>
#include <HarmonicOscillator.h>

using namespace std;

int main()
{
    HarmonicOscillator ho1(0.3, 10, 2, 1000);
    ho1.oscillate();
}