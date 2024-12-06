import java.util.Scanner;

// Custom exception class
class InvalidEmailException extends Exception {
    public InvalidEmailException(String message) {
        super(message);
    }
}

public class EmailValidation {
    public static void main(String[] args) {
        // Using try-with-resources for scanner
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter your email: ");
            String email = scanner.nextLine();

            try {
                validateEmail(email);
                System.out.println("Email is valid.");
            } catch (InvalidEmailException e) {
                System.out.println("Invalid Email: " + e.getMessage());
            }
        }
    }

    // Method to validate the email
    public static void validateEmail(String email) throws InvalidEmailException {
        if (!email.contains("@")) {
            throw new InvalidEmailException("Email must contain '@'.");
        }
        if (!email.contains(".")) {
            throw new InvalidEmailException("Email must contain '.'.");
        }
        if (email.endsWith(".")) {
            throw new InvalidEmailException("Email cannot end with a '.'.");
        }
        if (email.endsWith("@")) {
            throw new InvalidEmailException("Email cannot end with an '@'.");
        }
    }
}


