package Static_variable;

public class Test {
// static
    static int count = 0;

    Test() {
        count++;
    }

    void display() {
        System.out.println("Count: "+count);
    }
}
