
def letterCombi(digits):
    dictD = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',\
             '7':'pqrs', '8':'tuv', '9':'wxyzs'};
    res = [''];
    for digi in digits:
         midres = [];
         for char in dictD[digi]:
      
             for re in res:
                 temp = re+ char;
                 midres.append(temp);
         res = midres;
    print res;
    return res;
        
letterCombi('23');
