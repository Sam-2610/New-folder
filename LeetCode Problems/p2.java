import java.util.Arrays;

class p2 {
    public static void main(String[] args) {
        int[] n = new int[3];
        n[0] = 1;
        n[1] = 2;
        n[2] = 3;
        System.out.println(Arrays.toString(n));
        int[] q = new int[3];
        q[0] = 4;
        q[1] = 5;
        q[2] = 6;
        System.out.println(Arrays.toString(q));
        int[] w = new int[3];
        w[0] = n[0] + q[0];
        w[1] = n[1] + q[1];
        w[2] = n[2] + q[2];
        System.out.println(Arrays.toString(w));

    }
}