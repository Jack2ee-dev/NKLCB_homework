class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        s = ""

        def recursive(node):
            nonlocal s
            if node is None:
                return
            s += str(node.value) + " "
            recursive(node.left)
            recursive(node.right)
        
        recursive(self.root)
        print(s)

    def inorder(self):
        s = ""

        def recursive(node):
            nonlocal s
            if node is None:
                return
            recursive(node.left)
            s += str(node.value) + " "
            recursive(node.right)

        recursive(self.root)
        print(s)

    def postorder(self):
        s = ""

        def recursive(node):
            nonlocal s
            if node is None:
                return
            recursive(node.left)
            recursive(node.right)
            s += str(node.value) + " "

        recursive(self.root)
        print(s)


    def bfs(self, value):
        queue = [self.root]
        isFound = False
         
        while len(queue) > 0:
            dequed = queue.pop(0)
            if dequed is None:
                break

            if dequed.value == value:
                isFound = True
                break

            queue.append(dequed.left)
            queue.append(dequed.right)

        print(isFound)

    def dfs(self, value):
        isFound = False

        def recursive(node):
            nonlocal isFound
            if node is None:
                return
            
            if node.value == value:
                isFound = True
                return

            recursive(node.left)
            recursive(node.right)

        recursive(self.root)
        print(isFound)

if __name__ == "__main__":
    bt = BinaryTree([x for x in range(1, 11)])
    print("--------- preorder ---------")
    bt.preorder()
    print("--------- inorder ---------")
    bt.inorder()
    print("--------- postorder ---------")
    bt.postorder()
    print("--------- bfs ---------")
    for i in range(1, 20, 1):
        bt.bfs(i)
    print("--------- dfs ---------")
    for i in range(1, 20, 1):
        bt.dfs(i)