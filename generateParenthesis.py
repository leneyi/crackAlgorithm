
def generateParenthesis(n):
    string = '';
    res = [];
    generate(string,n,0,0,res);
    return res;




def generate(string,n,left,right,res):
    if (len(string)==2*n):
        res.append(string);
        return res;
    if left<n:
        generate(string + '(',n,left+1,right,res);
    if right<left:
        generate(string + ')',n,left,right+1,res);

print(generateParenthesis(3));
