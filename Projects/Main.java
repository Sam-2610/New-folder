import java.util.HashSet;
import java.util.Iterator;

public class Main {

    public static void main(String[] args) {
        HashSet<Integer> list1 = new HashSet<>();

        list1.add(1);
        list1.add(2);
        list1.add(3);
        list1.add(4);
        System.out.println(list1);

        int e = list1.size();
        System.out.println(e);

        list1.remove(2);
        System.out.println(list1);

        if (list1.isEmpty()) {
            System.out.println("list1 is Empty");
        } else {
            System.out.println("list1 is not Empty");
        }

        if (list1.contains(3)) {
            System.out.println("Present");
        }
        if (!list1.contains(3)) {
            System.out.println("Absent");
        }

        Iterator w = list1.iterator();
        while (w.hasNext()) {
            System.out.println(w.next());
        }
        System.out.println();

    }
}
