import random

class coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwarg):

        for key,value in kwarg.items():
            setattr(self,key,value)

            
        self.is_rare = rare
        self.is_clean = clean
        self.is_heads = heads

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
            self.color = self.rusty_color

    def clean(self):
            self.color =  self.clean_color

    def __del__(self):
            print("The coin spent")

    def flip(self):
        head_options =[True,False]
        choice = random.choice(head_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${}coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value*100))
        
class One_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.01,
            "clean_color":"gold",
            "rusty_color" :"greenesh",
            "num_edges" :1,
            "diameter" : 22.5,
            "thickness":3.15,
            "mass":7.28
            }

        super().__init__(**data)

class Two_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.02,
            "clean_color":"bronze",
            "rusty_color" :"brownish",
            "num_edges" :1,
            "diameter" : 25.9,
            "thickness":1.85,
            "mass":8.15
            }

        super().__init__(**data)

class Five_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.05,
            "clean_color":"blue",
            "rusty_color" :"none",
            "num_edges" :1,
            "diameter" : 27.9,
            "thickness":2.85,
            "mass":3.15
            }

        super().__init__(**data)
        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color =  self.clean_color

class Ten_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.10,
            "clean_color":"gray",
            "rusty_color" :"none",
            "num_edges" :1,
            "diameter" : 28.9,
            "thickness":2.95,
            "mass":4.15
            }

        super().__init__(**data)
        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color =  self.clean_color

class Twenty_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.20,
            "clean_color":"blue",
            "rusty_color" :"none",
            "num_edges" :1,
            "diameter" : 29.9,
            "thickness":3.85,
            "mass":5.15
            }

        super().__init__(**data)
        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color =  self.clean_color


class Fifty_Pence(coin):
    def __init__(self):

        data = {
            "original_value" :0.50,
            "clean_color":"yellow",
            "rusty_color" :"none",
            "num_edges" :1,
            "diameter" : 27.9,
            "thickness":2.85,
            "mass":3.15
            }

        super().__init__(**data)
        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color =  self.clean_color

class One_Pound(coin):
    def __init__(self):

        data = {
            "original_value" :1.00,
            "clean_color":"blue",
            "rusty_color" :"greensh",
            "num_edges" :1,
            "diameter" : 30.9,
            "thickness":2.85,
            "mass":9.15
            }

        super().__init__(**data)

class Two_Pound(coin):
    def __init__(self):

        data = {
            "original_value" :2,
            "clean_color":"blue",
            "rusty_color" :"gray",
            "num_edges" :1,
            "diameter" : 27.9,
            "thickness":2.85,
            "mass":10.15
            }

        super().__init__(**data)

coins = [One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]

for coin in coins:
    arguments = [coin,coin.value,coin.color,coin.thickness,coin.diameter,coin.num_edges,coin.mass]
    string = "{},value:{},color:{},thickness(mm):{},daimeter(mm):{},num_edges:{},mass:{}".format(*arguments)
    print(string)












































































































































   
        
        

