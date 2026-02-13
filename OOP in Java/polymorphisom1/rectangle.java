package polymorphisom1;

public class rectangle extends shape {

    double height, weidth;

    rectangle(double h, double w) {
        height = h;
        weidth = w;
    }
    @Override
        double area() {
        return height*weidth;
    }
}
