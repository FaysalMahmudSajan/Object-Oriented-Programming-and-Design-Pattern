package oop;

public class Teacher {

    String name, Gender;
    int number;
    //constructor

    Teacher() {
        System.out.println("No ans");
    }

    Teacher(String n, String g, int ph) {
        name = n;
        Gender = g;
        number = ph;
    }

    void Displayinfo() {
        System.out.println("Name: " + name);
        System.out.println("Gender: " + Gender);
        System.out.println("number: " + number);
    }
}
