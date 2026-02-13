package variable_length_arguments;

public class test {

    void add(int... num) {
        int sum = 0;
        for (int x : num) {
            sum+=x;
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {
        test t1 = new test();
        t1.add(12,23);
        t1.add(23,34,563);

    }
}
