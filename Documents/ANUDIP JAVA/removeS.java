
import java.util.ArrayList;

public class removeS {

    public  static  void  main(String[]args){

        ArrayList<String>students = new ArrayList<>();

        students.add("Alice");
        students.add("Sam");
        students.add("Bob");
        students.add("Sophie");
        students.add("Charlie");

        System.out.println("Original list" + students);

        students.removeIf(name -> name.startsWith("S"));

        System.out.println("Updated List (after removal): " + students);
    }
}
