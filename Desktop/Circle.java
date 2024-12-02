public class Circle implements Shape {
    private int radius;

    // Constructor to initialize radius
    public Circle(int radius) {
        this.radius = radius;
    }

    // Implement the area method
    @Override
    public int area() {
        return (int) (Math.PI * radius * radius);
    }

    // Implement the drawShape method
    @Override
    public void drawShape() {
        System.out.println("Drawing a Circle with radius " + radius);
    }
}
