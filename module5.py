
# Michael Matonte
# CS505 -Module 5 
# 8/6/24
class Case:
    
    def __init__(self, name,steps):
        self.name = name
        self.steps = steps

class Step: 
    
    def __init__(self, name, actor, actee , actions):
        self.name = name
        self.actor = actor
        self.actee = actee
        self.actions = actions
            
class Builder: 
    
    def __init__(self):
        self.bulider = "builder"
    
    def buildCase(self,name,steps):
        return Case(name,steps)
    
    def buildStep(self,name,actor,actee,actions):
        return Step(name,actor,actee,actions)
        

class Printer: 
     def __init__(self ):
        self.bulider = "printer"

     def printCase(self,case):
        print(case.name+' is when the program needs to'+ '\n')
        for a in case.steps:
                print(""+a.name+"\n \t"+ "*"+a.actor+" to "+a.actee+"\n \t \t"+"-"+a.actions)
        print('\n')
        
def main():
    
    builder = Builder()
    printer = Printer()  
    
    step1 = builder.buildStep("Step 1- User sends report through UI","User","Report Service","Send Information to Report Service for Processing")
    step2 = builder.buildStep("Step 2- Report Service adds info to report by calling Calculation Aervice","Report Service","Calculation Service","Send Information to Calculation Service Processing")
    step3 = builder.buildStep("Step 3- Calculation Service sends finished report to db","Calculation Service","Database","Send fininshed reports to database")
    case1= builder.buildCase("Case 1",[step1,step2,step3])

    printer.printCase(case1)

if __name__ == "__main__": main()      


