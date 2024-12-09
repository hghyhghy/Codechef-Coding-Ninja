class Listnode {
    int val;
    Listnode next;

    // Constructor
    Listnode(int val) {
        this.val = val;
        this.next = null;
    }
}

public class Findindexinlinkedlist {

    // Method to find the index of the target value
    public static int find(Listnode head, int target) {
        int index = 0;
        Listnode current = head;

        while (current != null) {
            if (current.val == target) {
                return index;
            }
            current = current.next;
            index++;
        }

        return -1; // Target not found
    }

    // Method to print the list
    public static void printlist(Listnode head) {
        Listnode current = head;
        while (current != null) {
            System.out.print(current.val + (current.next != null ? " -> " : ""));
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Create the linked list: 3 -> 7 -> 10 -> 15
        Listnode head = new Listnode(3);
        head.next = new Listnode(7);
        head.next.next = new Listnode(10);
        head.next.next.next = new Listnode(15);

        System.out.println("Original List:");
        printlist(head);

        int target = 10; // Let's find this value in the list
        int result = find(head, target);
        System.out.println("Index of " + target + ": " + result); // Output: 2 (since 10 is at index 2)
    }
}
