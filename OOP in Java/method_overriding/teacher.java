package method_overriding;

public class teacher extends person {

    String subject;

    @Override
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Subject: "+subject);
    }

}
