package Method_overloading;

public class Overloading {

    void add() {
        System.out.println("Nothing");
    }

    void add(int a, int b) {
        System.out.println(a+b);
    }

    void add(double a, double b) {
        System.out.println(a+b);
    }

    void add(double a, int b, double c) {
        System.out.println(a+b+c);
    }

    public static void main(String[] args) {
        Overloading t1 = new Overloading();
        t1.add(4,5);
        t1.add();
        t1.add(5.6,7.9);
        t1.add(1.2,2,3);
    }
}
