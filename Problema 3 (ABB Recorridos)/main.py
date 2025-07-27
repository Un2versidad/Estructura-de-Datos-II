class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Construcción del árbol
root = Node(66)
root.left = Node(44)
root.right = Node(85)

root.left.left = Node(22)
root.left.right = Node(50)
root.left.right.left = Node(47)

root.left.left.left = Node(9)
root.left.left.right = Node(37)
root.left.left.right.right = Node(39)

root.right.left = Node(73)
root.right.right = Node(90)
root.right.right.left = Node(88)
root.right.right.right = Node(94)

def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result

def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result

def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result

# Imprimir los resultados de los recorridos
print("Recorrido PreOrden:", preorder(root))
print("Recorrido InOrden:", inorder(root))
print("Recorrido PosOrden:", postorder(root))