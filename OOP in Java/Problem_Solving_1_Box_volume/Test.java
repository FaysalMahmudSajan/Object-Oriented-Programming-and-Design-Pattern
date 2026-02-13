package Problem_Solving_1_Box_volume;

public class Test {

    double height, width, depth;

    Test(double h, double w, double d) {
        height = h;
        width = w;
        depth = d;
    }

    void display() {
        double vol=height*width*depth;
        System.out.println("volume: "+vol);
    }
}
