# Michael Matonte
# CS505 -FSA regarding project
# 8/14/24

class Program:
    
    def __init__(self, name,steps):
        self.name = name
        self.steps = steps

class Step: 
    
    def __init__(self, name,states,guard):
        self.name = name
        self.states = states
        self.guard = guard

class State:
    def __init__(self, name):
        self.name = name

            
class Builder: 
    
    def __init__(self):
        self.bulider = "builder"
    
    def buildProgram(self,name,steps):
        return Program(name,steps)
    
    def buildStep(self,name,states,guard):
        return Step(name,states,guard)
        
    def buildState(self,name):
        return State(name)
        
class Printer: 
     def __init__(self ):
        self.bulider = "printer"

     def printProgram(self,p):
        print(p.name+'s are the following:'+ '\n')
        
        for s in p.steps:
                print("\t\t\n"+s.name+"\t")
                print("\t Description:"+ s.guard)
                print("\t possible states to reach:")
                for ss in s.states:
                   print("\t\t *"+ss.name)
        print('\n')
        
def main():
    
    builder = Builder()
    printer = Printer()  
    
    start = builder.buildState("start")
    login = builder.buildState("login")
    pinPage= builder.buildState("pin page")
    account = builder.buildState("account landing")
    dead  = builder.buildState("dead/finished")
    
    begin = builder.buildStep("Step 0- Session Created, go to login", [start,login],"default guard")
    
    authorize = builder.buildStep("Step 1- Login with name and pw",[login,pinPage,dead], "succesful login advances the session, too many attempts kill the session")

    pinpage = builder.buildStep("Step 2- Put pin in",[pinPage,account,dead], "succesful login advances the session to account laning, too many attempts kills session")
    
    accountPage = builder.buildStep("Step 3- You are logged in",[dead,account], "session stays on account page until it dies, timesout, or associated account overdraws")

    program= builder.buildProgram("ATM machine",[begin,authorize,pinpage,accountPage])

    printer.printProgram(program)

if __name__ == "__main__": main()      


