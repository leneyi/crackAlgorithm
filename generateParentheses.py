
def generateParenthesis(n):
    string = '';
    rlist = [];
    generate(rlist,string,0,0,n);
    return rlist;


def generate(rlist,string,left,right,maxi):
    if len(string) == maxi*2:
       rlist.append(string);
       return;
    if left < maxi:
       generate(rlist,string+'(',left+1,right,maxi);
    if right < left:
       generate(rlist,string+')',left,right+1,maxi);

print (generateParenthesis(4));
