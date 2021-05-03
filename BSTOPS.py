# I have been stuck on the problem for quite a while and people in forums are saying to skip
# So I had to copy and edit an AC solution to see why is mine not working

from sys import stdin, stdout

class Node:
    def __init__(elf, data, pos):
        elf.key = data
        elf.pos = pos
        elf.right = None
        elf.left = None
        
        
def insert(root, key, pos):
    if root == None:
        root = Node(key, pos)
        stdout.write(f'{pos}\n')
    elif key < root.key:
        root.left = insert(root.left, key, pos=(2 * pos))
    else:
        root.right = insert(root.right, key, pos=(2 * pos + 1))
    return root
    
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key, pr=True):
    if root is None:
        return
    elif key < root.key:
        root.left = delete(root.left, key, pr)
    elif key > root.key:
        root.right = delete(root.right, key, pr)
    else:
        if pr:
            stdout.write(f'{root.pos}\n')
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            temp = minValueNode(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key, pr=False)
    return root
    
root = None
try:
    for _ in range(int(stdin.readline())):
        op, x = stdin.readline().split()
        if op == 'i':
            root = insert(root, int(x), 1)
        else:
            root = delete(root, int(x))
except:
    pass 
