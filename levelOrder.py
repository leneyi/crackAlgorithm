
def levelOrder(self, root):
    res = [];
    string = '';
    if root is None:
        return res;
    self.traverse(root, 0,res);
    return res;
    

def traverse(self, root, height, res):
    if root is None:
       return res;
    if len(res)<= height:
     res.append([]);
     res[height].append(root.val);
    self.traverse(root.left, height+1, res);
    self.traverse(root.right, height+1, res);
    return res;

   
