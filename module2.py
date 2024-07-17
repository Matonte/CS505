# CS505 Module 2 Critical Thinking 
#Implement the YourLastName class using Python, which will prompt the user to input the key elements of the diagram and return these objects in a well-formatted output.
# Michael Matonte 7.16.24

class Stage:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __repr__(self):
        return f"Person(name={self.name}, age={self.attributes})"


class Stages:
    
    Transaction = ['Contact','Requirements','Initiation','Verification']
    Planning = ['Estimating','Scheduling','Tracking','Resource Assesment']
    Modelling= ['Analysis','Design','Assigning']
    Construction = ['Programming','Unit Tests','Integration Tests','Deployment to Test']
    UserAcceptance= ['User Acceptance Testing','Dry Run','Focus Groups']
    Operations = ['Production','CustomerSuccess']
    
    transaction =  Stage('Transaction', Transaction)
    planning = Stage('Planning',Planning)
    modelling = Stage('Modelling',Modelling)
    construction = Stage('Construction',Construction)
    userAcceptance = Stage('UserAcceptance',UserAcceptance)
    operations = Stage('Operations',Operations)

    
    AllOfIt = [transaction,planning,modelling,construction,userAcceptance,operations]

def main():
    print("What do you want to know about Waterfall? Press 'x' to quit")
    while(True):
        res = input("information regarding: ")
        
        if res == "Waterfall":
            for a in Stages.AllOfIt:
                print("-"+a.name)
                for s in a.attributes:
                    print("   -"+ s)
            print("\n")
        if res == "Transaction":
            print("the features of Transaction are:")
            for s in Stages.Transaction:
                print("    -"+ s)
            print("\n")
        if res == "Planning":
            print("the features of Planning are:")
            for s in Stages.Planning:
                print("    -"+ s) 
            print("\n")
        if res == "Modelling":
            print("the features of Modelling are:")
            for s in Stages.Modelling:
                print("    -"+ s)
            print("\n")
        if res == "Construction":
            print("the features of Construction are:")
            for s in Stages.Construction:
                print("    -"+ s) 
            print("\n")
        if res == "UserAcceptance":
            print("the features of UserAcceptance are:")
            for s in Stages.UserAcceptance:
                print("    -"+ s)
            print("\n")
        if res == "Operations":
            print("the features of Operations are:")
            for s in Stages.Operations:
                print("    -"+ s)
            print("\n")
        elif res == 'x':
            break
        else:
            print("Anything else?")
            continue
        

if __name__ == "__main__": main()   
