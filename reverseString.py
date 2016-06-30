
def reverseString(s):
      listS = list(s);
      i = 0;
      j = len(s)-1;
      while (i<j):
          temp = listS[i];
          listS[i] = listS[j];
          listS[j] = temp;
          i +=1;
          j -=1;
      print ''.join(listS);
      return ''.join(listS);
reverseString('hello');
