package Encapsulation;

public class Main {

    public static void main(String[] args) {

        Test t1 = new Test();
        t1.setName("Faysal");
        System.out.println(t1.getName());
        t1.age = 123456;
        t1.display();
    }

}
