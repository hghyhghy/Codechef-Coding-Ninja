
import java.util.HashMap;
import java.util.Map;

class Student {
    int sid;
    String sname;
    double percentage;


    public Student(int sid, String sname, double percentage) {
        this.sid = sid;
        this.sname = sname;
        this.percentage = percentage;
    }

    
    @Override
    public String toString() {
        return "Student ID: " + sid + ", Name: " + sname + ", Percentage: " + percentage;
    }
}

public class Storemain {
    public static void main(String[] args) {
        // Create a HashMap with SID as key and Student object as value
        HashMap<Integer, Student> studentMap = new HashMap<>();

        // Adding students to the HashMap
        studentMap.put(1, new Student(1, "Subham", 85.5));
        studentMap.put(2, new Student(2, "Tonmoy", 65.4));
        studentMap.put(3, new Student(3, "Swarnodip", 72.3));
        studentMap.put(4, new Student(4, "Bobby", 90.0));
        studentMap.put(5, new Student(5, "Bobbly", 55.6));

        
        System.out.println("Name of Students with percentage  greater than 70:");
        
        for (Map.Entry<Integer, Student> entry : studentMap.entrySet()) {
            Student student = entry.getValue();
            if (student.percentage > 70) {
                System.out.println(student);
            }
        }
    }
}
