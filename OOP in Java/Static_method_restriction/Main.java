package Static_method_restriction;

public class Main {

    public static void main(String[] args) {
        Test t1 = new Test();
        t1.display();
       Test.display1();//static jonne object lagbe na
    }
}
