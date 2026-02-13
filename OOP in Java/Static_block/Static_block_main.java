package Static_block;

class Static_block_main {

    public static void main(String[] args) {
        System.out.println("2");
        System.out.println("3");
        Static_block_main t1=new Static_block_main();
        t1.display1();
        display();
    }

    static {
        System.out.println("1");
    }

    static {
        System.out.println("5");
    }

    static void display() {
        System.out.println("4");
    }

    void display1() {
        System.out.println("6");
    }

}
