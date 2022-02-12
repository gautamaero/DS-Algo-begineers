class Phone:
    #This is blueprint which is generalisation 
    # to create different type of phone
    def make_call(self):
        print("I am making a call")
    def play_call(self):
        print("I am playing a game")

p1=Phone()
p1.make_call()

p1.make_call()



class Phone:
    
    def set_color(self,color):
        self.color = color