
package polymorphisom1;

public class triangle extends shape {
        double base, height;

    triangle(double h, double b) {
        height = h;
        base = b;
    }
    @Override
        double area() {
        return 0.5*height*base;
    }
}
