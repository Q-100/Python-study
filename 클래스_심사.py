class Annie:
    def __init__(self,*args):
        self.__health = args[0] # __변수명 : 비공개 속성으로 클래스 외부에선 사용 불가능(private)
        self.mana = args[1]
        self.ap = args[2]

    def tibbers(self):
        print("티버: 피해량 %.1f"%(self.ap*0.65+400))


a = list(map(float,input().split()))
x = Annie(*a)
x.tibbers()


