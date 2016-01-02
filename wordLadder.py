
def ladderLength(beginWord,endWord,wordList):
    reached = set();
    reached.add(beginWord);
    wordList.add(endWord);
    distance = 1;
    while(endWord not in reached):
        toAdd = set();
        for each in reached:
            for i in range(0,len(each)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    each1= each[:i]+ch + each[i+1:];
                    #print each;
                    if each1 in wordList:
                        toAdd.add(each1);
                        wordList.remove(each1);
        distance +=1;
        if len(toAdd) == 0:
            return 0;
        reached = toAdd;
    return distance;
print(ladderLength('hit','cog',set(['hot','dot','dog','lot','log'])));

