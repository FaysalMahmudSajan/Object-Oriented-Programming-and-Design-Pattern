package Encapsulation;

public class Test {

    private String name;
    int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    void display() {
        System.out.println("Age: " + age);
    }

}
