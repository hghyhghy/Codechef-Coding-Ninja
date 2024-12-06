import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create an ArrayList of student names
        ArrayList<String> studentNames = new ArrayList<>();
        studentNames.add("Alice");
        studentNames.add("Sam");
        studentNames.add("Sophia");
        studentNames.add("John");
        studentNames.add("Steve");
        studentNames.add("Mike");

        // Remove names starting with 'S' using a lambda expression
        studentNames.removeIf(name -> name.startsWith("S"));

        // Print the updated list
        System.out.println("Student names after removal: " + studentNames);
    }
}
