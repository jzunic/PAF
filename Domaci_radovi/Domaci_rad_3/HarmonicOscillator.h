class HarmonicOscillator
{
    private:
        double x[9999], v[9999], a[9999], t[9999], dt, m, k, vrijeme;
        double *pt;

        void move();

    public:
        HarmonicOscillator(double x_0, double m, double vrijeme_oscilacije, double k, double korak = 0.01);

        void oscillate();
};