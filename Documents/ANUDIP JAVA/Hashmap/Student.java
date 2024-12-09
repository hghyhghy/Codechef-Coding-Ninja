package Hashmap;



public class Student {
    private int sId;
    private String sName;
    private double percentage;

    // Constructor
    public Student(int sId, String sName, double percentage) {
        this.sId = sId;
        this.sName = sName;
        this.percentage = percentage;
    }
    public int getsId() {
        return sId;
    }

    public void setsId(int sId) {
        this.sId = sId;
    }

    public String getsName() {
        return sName;
    }

    public void setsName(String sName) {
        this.sName = sName;
    }

    public double getPercentage() {
        return percentage;
    }

    public void setPercentage(double percentage) {
        this.percentage = percentage;
    }

    @Override
    public String toString() {
        return "Student [ID : " + sId + ", Name : " + sName + ", Percentage : " + percentage + "]";
    }
}

