package method_overriding;

public class Main {

    public static void main(String[] args) {

        person p1 = new person();
        p1.age = 23;
        p1.name = "ovi";
        p1.display();

        teacher t1 = new teacher();
        t1.name = "Faysal";
        t1.age = 132;
        t1.subject = "science";
        t1.display();
    }
}
