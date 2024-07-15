#Aex-05-01.py
import random

class GuessNumberParent():
    def __init__(self,number):
        self.number=number
        self.sum=0

    def new_game(self):
        """親の数のリセット"""
        self.number=random.randint(1,101)

class GuessNumberChild():
    def __init__(self,number):
        self.number=number
        self.sum=0
        self.count=0

    def new_game(self):
        """子の数のリセット"""
        self.number=random.randint(1,101)
        self.count+=1

    def guess(self,parent):
        """数あて"""
        point=100
        m=parent//2
        print("%d回目"%(self.count))
        print("親=%d"%(parent))
        while m!=0:
            if parent>self.number:
                self.number+=m
                print(self.number)
                point-=1
            elif parent<self.number:
                self.number-=m
                print(self.number)
                point-=1
            else:
                print(self.number)
                return point
            m=m//2
        return point

def main():
    parent=GuessNumberParent(random.randint(1,101))
    child=GuessNumberChild(random.randint(1,101))

    for i in range(10000):
        child.new_game()
        parent.new_game()
        child.sum+=child.guess(parent.number)
        parent.sum+=parent.number
    
    point_ave=child.sum/10000
    parent_ave=parent.sum/10000
    print("親平均=",parent_ave)
    print("得点平均=",point_ave,"点")

if __name__=="__main__":
    main()

