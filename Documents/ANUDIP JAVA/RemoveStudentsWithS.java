import java.util.ArrayList;

public class RemoveStudentsWithS {
    public static void main(String[] args) {
        // Create an ArrayList of student names
        ArrayList<String> students = new ArrayList<>();
        students.add("Alice");
        students.add("Sam");
        students.add("Bob");
        students.add("Sophie");
        students.add("Charlie");

        System.out.println("Original List: " + students);

        // Remove names starting with 'S' using lambda expression
        students.removeIf(name -> name.startsWith("S"));

        System.out.println("Updated List (after removal): " + students);
    }
}
