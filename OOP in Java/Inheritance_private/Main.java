
package Inheritance_private;
public class Main {

    public static void main(String[] args) {
        teacher p1=new teacher();
        p1.setName("Faysal");
        p1.setAge(23);
        p1.setSubject("Science");
        p1.displayinfo1();
        
        teacher p2=new teacher();
        p2.setName("Fay");
        p2.setAge(2);
        p2.setSubject("Sci");
        p2.displayinfo1();
    }
    
    
}
