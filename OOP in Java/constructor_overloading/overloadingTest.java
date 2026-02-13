package constructor_overloading;

public class overloadingTest {

    public static void main(String[]args) {
        Teacher t1 = new Teacher("Faysal", "Male");
        t1.display();
        Teacher t2 = new Teacher();
        Teacher t3 = new Teacher("Faysal", "Male", 13245798);
        t3.display();
    }
}
