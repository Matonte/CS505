# Michael Matonte
# CS505 -Module 4 
# 8/1/24
class Attribute:
    
    def __init__(self, name,features):
        self.name = name
        self.features = features

class Programmer: 
    
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
            
    def __repr__(self):
        return f"programmer(name={self.name}, pages={self.attributes})"

class Builder: 
    
    def __init__(self):
        self.bulider = "builder"
    
    def buildAttribute(self,name,features):
        return Attribute(name,features)
    
    def buildProgrammer(self,name,attributes):
        return Programmer(name,attributes)
        

class Printer: 
     def __init__(self ):
        self.bulider = "printer"

     def printPerson(self,programmer):
        print(programmer.name+'s personality that makes him a good programmer are:'+ '\n')
        for a in programmer.attributes:
            print(programmer.name+"'s "+a.name + " which is: ")
            for aa in a.features: 
                print("    -"+ aa)
            print('\n')
        
def main():
  
    builder = Builder()
    printer = Printer()
   
    intelligence = builder.buildAttribute("intelligence",["can find solutions","understands problems"])
    conscientious = builder.buildAttribute("conscientious",["doesn't give up","doesn't get frustrated"])
    agreeableness = builder.buildAttribute("agreeableness",["works well with people", "communicates accurately"])
    
    Jack = builder.buildProgrammer("Jack",[intelligence,conscientious,agreeableness])
    
    printer.printPerson(Jack)

if __name__ == "__main__": main()      
