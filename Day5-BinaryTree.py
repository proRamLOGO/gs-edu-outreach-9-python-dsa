
# class <name> :
#    pass 

class node :
    def __init__(self, x) :
        self.val = x
        self.left = None
        self.right = None

def createTree( root, l ) :

    if l[-1] == len(l)-1 :
        return None
    
    # Base Case
    if l[ l[-1] ]==-1:
        l[-1] += 1
        return None

    # Recursive Case
    root = node(l[ l[-1] ])
    l[-1] += 1
    root.left  = createTree( root.left , l )
    root.right = createTree( root.right, l )
    return root    
        
def preOrder( root ) :

    # Base Case
    if root == None :
        return

    # Recursive Case
    print(root.val)       #N
    preOrder(root.left)   #L
    preOrder(root.right)  #R
            
def postOrder( root ) :

    # Base Case
    if root == None :
        return

    # Recursive Case
    postO           m,rder(root.left)   #L
    postOrder(root.right)  #R
    print(root.val)        #N
            
def inOrder( root ) :

    # Base Case
    if root == None :
        return

    # Recursive Case
    inOrder(root.left)   #L
    print(root.val)      #N
    inOrder(root.right)  #R
    
        
def main():
    n = int(input())
    l = list(map(int,input().split())) + [0]
    root = createTree(node(0), l )
    preOrder(root)
    

main()



