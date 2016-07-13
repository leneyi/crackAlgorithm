
def intToRoman(num):
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
    strs = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
    res = "";
    for i in range(len(values)):
        while num >= values[i]:
            num -= values[i];
            res +=strs[i];
    print res;
    return res;
intToRoman(1998);
