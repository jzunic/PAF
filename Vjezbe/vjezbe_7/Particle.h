class Particle 
{
    private:
        double x, y, v_x, v_y, t = 0, dt, g = -9.81;
        void move();
        
    public:
        Particle(double v, double kut, double x_0, double y_0, double korak = 0.001);

        double range(), time();
};