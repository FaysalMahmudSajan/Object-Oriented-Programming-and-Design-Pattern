package Inheritance;

public class teacher extends person {

    String subject;

    void displayinfo1() {
        displayinfo();
        System.out.println("Subject: "+subject);
    }

}
