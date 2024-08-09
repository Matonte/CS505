# Michael Matonte
# CS505 -Module 6 
# 8/9/24
class Program:
    
    def __init__(self, name,steps):
        self.name = name
        self.steps = steps

class Step: 
    
    def __init__(self, name,substep):
        self.name = name
        self.substep = substep

            
class Builder: 
    
    def __init__(self):
        self.bulider = "builder"
    
    def buildProgram(self,name,steps):
        return Program(name,steps)
    
    def buildStep(self,name,substeps):
        return Step(name,substeps)
        

class Printer: 
     def __init__(self ):
        self.bulider = "printer"

     def printProgram(self,p):
        print(p.name+'s are the following:'+ '\n')
        for s in p.steps:
                print("\t\t\n"+s.name+"\t")
                for ss in s.substep:
                   print("\t\t *"+ss.name)
        print('\n')
        
def main():
    
    builder = Builder()
    printer = Printer()  
    

    step1a = builder.buildStep("1a Import root solver from scipy.optimize",[])
    step1b = builder.buildStep("1b Import numpy for trig functions",[])
    
    step1 = builder.buildStep("Step 1- Declare needed librariesFor business logic and Formulas to define functions",[step1a,step1b])
    
    step2a = builder.buildStep("2a declare variables",[])
    step2b = builder.buildStep("2b declare list of one or more functions",[])
    step2c = builder.buildStep("2c return function list",[])
    
    step2 = builder.buildStep("Step 2- Define the functions that will declare the list of functions from which the root will be found",[step2a,step2b,step2c])
    
    step3a = builder.buildStep("3a Declare solution variable",[])
    step3b = builder.buildStep("3b create a list of constants",[])
    step3c = builder.buildStep("3c call root solver with function list and list of constants",[])
    
    step3 = builder.buildStep("Step 3- Declare a solution variable that will call the solver on the list of functions, with a list of constants",[step3a,step3b,step3c])
    
    step4a = builder.buildStep("4a print solution",[])
    step4 = builder.buildStep(" Step 4 - Generate output",[step4a])

    program= builder.buildProgram("Program to find roots of Transcendental Function in Python",[step1,step2,step3,step4])

    printer.printProgram(program)

if __name__ == "__main__": main()      


