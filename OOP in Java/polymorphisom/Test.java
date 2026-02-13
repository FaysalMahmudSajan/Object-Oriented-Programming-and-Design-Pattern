package polymorphisom;

public class Test {

    public static void main(String[] args) {

        //polymorphisom 
        person p1 = new person();
        p1.display();
        p1 = new student();
        p1.display();
        p1 = new teacher();
        p1.display();
    }
}
