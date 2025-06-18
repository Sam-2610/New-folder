import java.util.Arrays;

class p1 {
    public static void main(String[] args) {
        int[] n = new int[5];
        n[0] = 1;
        n[1] = 2;
        n[2] = 3;
        n[3] = 4;
        n[4] = 5;
        System.out.println(Arrays.toString(n));
        int x = n[1] + n[3];
        System.out.println(x);
    }
}
