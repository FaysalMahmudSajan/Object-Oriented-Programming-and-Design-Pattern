package staticKeyWord;

public class Test {

    String name, gender;
    static String varsity = "DIU";

    Test(String n,String g) {
        name=n;
        gender=g;

    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Gender: " + gender);
        System.out.println("Varsity: " + varsity);
    }
}
