import java.util.Arrays;

class p1 {
    public static void main(String[] args) {
        int[] n = new int[5];     // Declare an array of size 5
        n[0] = 1;                 // Initialize elements
        n[1] = 2;
        n[2] = 3;
        n[3] = 4;
        n[4] = 5;

        System.out.println(Arrays.toString(n));  // Print the array
        int x = n[1] + n[3];     // Add n[1] (2) + n[3] (4)
        System.out.println(x);   // Output the result
    }
}
