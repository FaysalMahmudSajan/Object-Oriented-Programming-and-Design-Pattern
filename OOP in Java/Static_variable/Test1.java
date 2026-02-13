package Static_variable;

public class Test1 {
// none static
    int count = 0;

    Test1() {
        count++;
    }

    void display() {
        System.out.println("Count: "+count);
    }
}
