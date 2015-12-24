class MinStack(object):
  def __init__(self):
      self.minStack = [];
      self.stack = [];
      
  def push(self,x):
      self.stack.append(x);
      if len(self.minStack)>0 and x <= self.minStack[len(self.minStack)-1]:
          self.minStack.append(x);
      if len(self.minStack)== 0:
          self.minStack.append(x);

  def pop(self):
      tmp = self.stack.pop();
      if len(self.minStack)>0 and tmp== self.minStack[len(self.minStack)-1]:
          self.minStack.pop();

  def top(self):
      if len(self.stack)>0:
         return self.stack[len(self.stack)-1];
  def getMin(self):
      if len(self.minStack)>0:
         return self.minStack[len(self.minStack)-1];      
    



