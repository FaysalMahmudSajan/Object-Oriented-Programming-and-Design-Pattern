
package polymorphisom1;
public class test {
    public static void main(String[] args) {
        shape s=new shape();
        rectangle r=new rectangle(10,20);
        triangle t= new triangle(10,20);
        
        System.out.println(s.area());
        System.out.println(r.area());
        System.out.println(t.area());
        
    }
    
}
