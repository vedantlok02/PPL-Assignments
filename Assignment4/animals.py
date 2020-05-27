from abc import ABC, abstractmethod
class living_things(ABC):
    @abstractmethod		# this is decorated as an abstract method now, cannot be instantiated later
    def set_voice(self, voice):
        pass
    @abstractmethod		# this is decorated as an abstract method now, cannot be instantiated later
    def get_voice(self):
        return None

class animals(ABC):			#animals is base class
    def __init__(self, num=50):
        self.num = num
    def eats(self): 				#method overriding is implemented.. Derived classes have their own eats method 
        print("animals eat")
    def get_num(self, number):
        self.num = number
    def __add__(self, p): 			#Operator Overloading for polymorphism  -here the + is overloaded with __add__
        return self.num+p.num
    def __gt__(self, p):			#Operator Overloading for polymorphism  -here the > is overloaded with __gt__
        if(self.num > p.num):
            return True
        else :
            return False
    def __lt__(self, p):
        if(self.num > p.num):
            return False
        else :
            return True
    def __sub__(self, p):
        return (self.num-p.num)
        
class herb(animals): 	#derived class from animals
    def __init__(self, num=50):
        self.num = num
    def intestine(self, size=None): 
        if(size == None):
            print("large size intestine")
        else:
            print("size of intestine is", size)
    def eats(self):				#method overloading implemented. Because there is eats method in parents class - animals
        print("eat plants")
    def number(self):
        return self.num
    def get_num(self, number):
        self.num = number
    def __add__(self, p): 		#Operator Overloading for polymorphism..  + is polymorphed to __add__
        return self.num+p.num
    
        
class carni(animals):			 #derived class from animals
    def __init__(self, num=50):
        self.num = num
    def intestine(self, size=None): 
        if(size == None):
            print("small size intestine")
        else:
            print("size of intestine is", size)
    def eats(self):		#method overloading implemented. Because there is eats method in parents class - animals
        print("eat animals")
    def number(self):
        return self.num
    def get_num(self, number):
        self.num = number
    def __add__(self, p):
        return self.num+p.num
    
class equus(herb): 			
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        herb().eats()
        print("eats channa")
        
class horse(equus):			
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        equus().eats()
    def feature(self):
        print("Horse are muscular")

class zebra(equus):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        equus().eats()
    def feature(self):
        print("Have stripes")

class donkey(equus):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        equus().eats()
    def feature(self):
        print("Used for carrying load")

class panthera(carni):	
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        carni().eats()
        print("Eats deers")

class lion(panthera): 			
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        panthera().eats()
    def feature(self):
        print("King of Jungle")

class leopard(panthera):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        panthera().eats()
    def feature(self):
        print("Run Fast")

class cat(panthera, herb):		# multiple inheritence example
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        panthera().eats()
        herb().eats()
    def feature(self):
        print("Domastic animal")
    


a = animals()
b = animals()
h = herb()
d = carni()
m = herb()
n = leopard()
d.intestine(500)
b.get_num(100)
print('animals')
a.eats()
print('herbs')
m.eats()
print('leopard')
n.eats()
h.get_num(49)
if(h>d):
    print("More")
else:
    print("Less")
c = h+d
print(c)