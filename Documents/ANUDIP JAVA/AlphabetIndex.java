public class AlphabetIndex {
    public static void main(String[] args) {
        String input = "The quick brown fox jumps over the lazy dog.";
        int[] alphabetIndices = new int[26]; // To store the first occurrence of each letter
        for (int i = 0; i < 26; i++) {
            alphabetIndices[i] = -1; // Initialize all indices to -1 (not found)
        }

        // Convert the string to lowercase for consistency
        String lowerInput = input.toLowerCase();

        // Traverse the string and update the index of each alphabet letter
        for (int i = 0; i < lowerInput.length(); i++) {
            char ch = lowerInput.charAt(i);

            // Check if the character is a letter
            if (ch >= 'a' && ch <= 'z') {
                int index = ch - 'a'; // Calculate the position of the letter (0 for 'a', 1 for 'b', etc.)
                if (alphabetIndices[index] == -1) {
                    alphabetIndices[index] = i; // Store the first occurrence of the letter
                }
            }
        }

        // Print the result
        System.out.println("Indexes of the alphabet in the given string:");
        for (int i = 0; i < 26; i++) {
            char letter = (char) (i + 'a'); // Convert index back to the corresponding letter
            if (alphabetIndices[i] != -1) {
                System.out.println(letter + " -> " + alphabetIndices[i]);
            } else {
                System.out.println(letter + " -> Not found");
            }
        }
    }
}
