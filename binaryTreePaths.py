
def binaryTreePaths(root):
    string = '';
    path = [];
    if root is None:
        return path;
    string +=str(root.val);
    search(root, string, path);
    return path;
def search(root, string, path):
    if root.left is None and root.right is None:
       path.append(string);
       return path;
    if root.left is not None:
       search(root.left, string+'->'+str(root.left.val),path);
    if root.right is not None:
       search(root.right, string+'->'+str(root.right,val),path);
    

