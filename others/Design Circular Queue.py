import os


class MyCircularQueue:
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.data = [-1] * k
        self.tail, self.head = -1, -1
        self.size = k
    
    def go(self, n):
        return (n+1) % self.size
    
    def refresh(self):
        self.tail = self.head = -1
    
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.tail = self.head = 0
            self.data[0] = value
            return True
        
        if not self.isFull():
            self.tail = self.go(self.tail)
            self.data[self.tail] = value
            return True
        else:
            return False
    
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.getCurrentItemCount() == 1:
            self.refresh()
            return True
        # 如果不提前排除掉特例，head和tail的指向会非法，再用getCurrentItemCount必然得到奇怪的结果
        
        if self.isEmpty():
            return False
        else:
            self.head = self.go(self.head)
            return True
            
    
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.data[self.head]
    
    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.data[self.tail]

    def getCurrentItemCount(self):
        if self.tail == -1:  # 避开特例
            return 0
        
        res = self.tail - self.head + 1
        if res <= 0:
            res += self.size
        return res
    
    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.getCurrentItemCount() == 0
    
    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.getCurrentItemCount() == self.size
        
if __name__ == '__main__' and ('SJDEAK' in os.environ):
    circularQueue = MyCircularQueue(6)
    print(circularQueue.enQueue(6), circularQueue.getCurrentItemCount())
    print(circularQueue.Rear(), circularQueue.getCurrentItemCount())
    print(circularQueue.Rear(), circularQueue.getCurrentItemCount())
    print(circularQueue.deQueue(), circularQueue.getCurrentItemCount())
    print(circularQueue.enQueue(5), circularQueue.getCurrentItemCount())
    print(circularQueue.Rear(), circularQueue.getCurrentItemCount())
    print(circularQueue.deQueue(), circularQueue.getCurrentItemCount())
    print(circularQueue.Front(), circularQueue.getCurrentItemCount())
    print(circularQueue.deQueue(), circularQueue.getCurrentItemCount())
    print(circularQueue.deQueue(), circularQueue.getCurrentItemCount())
    print(circularQueue.deQueue(), circularQueue.getCurrentItemCount())
