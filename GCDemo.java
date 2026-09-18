import java.util.ArrayList;
import java.util.List;

public class GCDemo {
    static class Trash {
        byte[] data = new byte[1024]; // 1 KB per object
        String name;
        Trash(String name) { this.name = name; }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("GCDemo started — watch GC with -Xlog:gc* and VisualVM");
        List<Trash> leak = new ArrayList<>();

        for (int i = 1; i <= 12; i++) {
            // 1. Disposable garbage: dies immediately -> collected in Young Gen
            for (int j = 0; j < 50_000; j++) {
                Trash t = new Trash("temp-" + j);
            }
            // 2. A few survivors: kept in a list -> promoted to Old Gen
            for (int k = 0; k < 500; k++) {
                leak.add(new Trash("kept-" + i + "-" + k));
            }
            System.out.println("Iteration " + i + " done. Kept: " + leak.size());
            Thread.sleep(400);
        }
        System.out.println("Done. Total kept objects: " + leak.size());
    }
}
