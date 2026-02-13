package constructor_overloading;

public class Teacher {

    String name, gender;
    int number;

    Teacher() {
        System.out.println("No info");
    }

    Teacher(String n, String g) {
        name = n;
        gender = g;

    }

    Teacher(String n, String g, int ph) {
        name = n;
        gender = g;
        number = ph;
    }

    void display() {
        System.out.println("name: " + name + " \ngender: " + gender + "\nphone: " + number);
    }
}
