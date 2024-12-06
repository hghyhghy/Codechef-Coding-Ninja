public class Triangle implements Shape {
    private int base;
    private int height;

    // Constructor to initialize base and height
    public Triangle(int base, int height) {
        this.base = base;
        this.height = height;
    }

    // Implement the area method
    @Override
    public int area() {
        return (base * height) / 2;
    }

    // Implement the drawShape method
    @Override
    public void drawShape() {
        System.out.println("Drawing a Triangle with base " + base + " and height " + height);
    }
}
