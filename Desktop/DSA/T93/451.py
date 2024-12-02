

#search in the bst

class Node:

    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right


def main(root,target):

    if not root or not target:

        return False

    if target < root.val:

        return main(root.left,target)

    return main(root.right,target)

if __name__ == "__main__":
    # Create the BST manually
    # Example tree:
    #        50
    #       /  \
    #      30   70
    #     / \   / \
    #    20 40 60 80
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    # Search for the value 'X' in the BST
    X = 60
    result = main(root, X)
    print(f"Is {X} present in the BST? {'Yes' if result else 'No'}")

    # Search for another value
    X = 100
    result = main(root, X)
    print(f"Is {X} present in the BST? {'Yes' if result else 'No'}")