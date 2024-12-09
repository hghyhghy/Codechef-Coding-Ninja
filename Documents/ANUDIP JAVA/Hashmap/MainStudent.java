package Hashmap;



import java.util.HashMap;
import java.util.Map;

public class MainStudent {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Student s1 = new Student(101,"Subham",85);
		Student s2 = new Student(102,"Swarnodip",89);
		Student s3 = new Student(103,"Tonmoy",65);
		Student s4 = new Student(104,"Bobby",55);
		Student s5 = new Student(105,"Bobbly",70);
		
		HashMap<Integer, Student> mpp = new HashMap<>();
		
		mpp.put(s1.getsId(), s1);
		mpp.put(s2.getsId(), s2);
		mpp.put(s3.getsId(), s3);
		mpp.put(s4.getsId(), s4);
		mpp.put(s5.getsId(), s5);
		
		//Print all the students
		System.out.println("All the students : ");
		for(Map.Entry<Integer, Student> entry : mpp.entrySet()) {
			System.out.println(entry);
		}
		
		System.out.println();
		
		// Printing students with percentage > 70
        System.out.println("Students with percentage > 70 : ");
        
        for (Map.Entry<Integer, Student> entry : mpp.entrySet()) {
            Student student = entry.getValue();
            if (student.getPercentage() > 70)    System.out.println(student);   
        }
	}
}
/*
OUTPUT : 

All the students : 
101=Student [ID : 101, Name : Shyam, Percentage : 85.0]
102=Student [ID : 101, Name : Rohan, Percentage : 69.0]
103=Student [ID : 101, Name : Chandan, Percentage : 65.0]
104=Student [ID : 101, Name : Shubham, Percentage : 75.0]
105=Student [ID : 101, Name : Atanu, Percentage : 70.0]

Students with percentage > 70 : 
Student [ID : 101, Name : Shyam, Percentage : 85.0]
Student [ID : 101, Name : Shubham, Percentage : 75.0]

*/