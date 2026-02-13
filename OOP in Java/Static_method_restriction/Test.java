package Static_method_restriction;

public class Test {

    void display() {
        display1();
        System.out.println("I am not static method");
    }

    static void display1() {
        System.out.println("I am static method 1");
        display2();
    }
    static void display2() {
        System.out.println("I am static method 2");
        
    }
}
