import java.io.*;

public class Main {
    public static void main(String[] args) {
        String filePath = "example.txt"; // File name to write and read
        String contentToWrite = "Hello, this is a test for FileOutputStream and FileInputStream!";

        // Write to file using FileOutputStream
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(contentToWrite.getBytes()); // Write the string as bytes
            System.out.println("Data successfully written to file: " + filePath);
        } catch (IOException e) {
            System.out.println("An error occurred during writing to the file.");
            e.printStackTrace();
        }

        // Read from file using FileInputStream
        try (FileInputStream fis = new FileInputStream(filePath)) {
            System.out.println("Reading from file: " + filePath);
            int content;
            while ((content = fis.read()) != -1) {
                System.out.print((char) content); // Convert byte to char and print
            }
            System.out.println(); // Add a newline after reading
        } catch (IOException e) {
            System.out.println("An error occurred during reading from the file.");
            e.printStackTrace();
        }
    }
}
