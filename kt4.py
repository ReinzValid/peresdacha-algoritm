class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    # Повторяющиеся значения не добавляем.
    return root


def search(root, value):
    while root:
        if value == root.value:
            return True
        root = root.left if value < root.value else root.right
    return False


def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.value
        yield from inorder(root.right)


if __name__ == '__main__':
    root = None
    for value in (50, 30, 70, 20, 40, 60, 80):
        root = insert(root, value)
    print('40 найден:', search(root, 40))
    print('100 найден:', search(root, 100))
    print('In-order:', list(inorder(root)))
