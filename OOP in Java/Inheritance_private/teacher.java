
package Inheritance_private;
public class teacher extends person {
        private String subject;

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    void displayinfo1() {
        displayinfo();
        System.out.println("Subject: "+getSubject());
    }
}
