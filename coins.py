import random


class Coin:
    
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.original_color
        else:
            self.color = self.rusty_color
            
    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.original_color

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1.00:
            return "${} coin".format(int(self.original_value))
        else:
            return "{}¢ coin".format(int(self.original_value * 100))

    def __del__(self):
        print("Coin Spent")

class Penny(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "original_color": "bronze",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 19.05, #mm
            "thickness": 1.52, #mm
            "mass": 2.500 #g
            } 
        super().__init__(**data)



class Nickel(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "original_color": "silver",
            "rusty_color": "rusty brown",
            "num_edges": 1,
            "diameter": 21.21, #mm
            "thickness": 1.95, #mm
            "mass": 5.000 #g
            } 
        super().__init__(**data)


class Dime(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "original_color": "silver",
            "rusty_color": "rusty brown",
            "num_edges": 1,
            "diameter": 17.91, #mm
            "thickness": 1.35, #mm
            "mass": 2.268 #g
            } 
        super().__init__(**data)


class Quarter(Coin):
    def __init__(self):
        data = {
            "original_value": 0.25,
            "original_color": "silver",
            "rusty_color": "rusty brown",
            "num_edges": 1,
            "diameter": 24.26, #mm
            "thickness": 1.75, #mm
            "mass": 5.670 #g
            } 
        super().__init__(**data)
        

class Half_Dollar(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "original_color": "silver",
            "rusty_color": "rusty brown",
            "num_edges": 1,
            "diameter": 30.61, #mm
            "thickness": 2.15, #mm
            "mass": 11.340 #g
            } 
        super().__init__(**data)


class Gold_Dollar(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "original_color": "gold",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 26.49, #mm
            "thickness": 2.00, #mm
            "mass": 8.1 #g
            } 
        super().__init__(**data)

        def rust(self):
            self.color = self.original_color


coins = [Penny(), Nickel(), Dime(), Quarter(), Half_Dollar(), Gold_Dollar()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    string = "{} - color:{}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)

   
        
