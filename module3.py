# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Program: 
    
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    
    def getInfo(self):
        for p in self.pages:
            print(p.name)
            for pp in p.attributes:
                print("     -"+pp)
            print("      This page goes to:")
            for links in p.linkedTo:
                print("           -"+str(links.name))
                
            
    
    def __repr__(self):
        return f"program(name={self.name}, pages={self.pages})"


class Page:
    def __init__(self, name, attributes,linkedTo):
        self.name = name
        self.attributes = attributes
        self.linkedTo = linkedTo
        

      
    
def main():
    homeAttr = ["new","del","edit","listoflists"]
    homeLinked = []
    home = Page("home",homeAttr,homeLinked)

    viewAttr = ["item","qty","specs"]
    viewLinked = [home]
    view = Page("view",viewAttr,viewLinked)

    editAttr = ["edititem","editqty","editspecs","del"]
    editLinked = [home]
    edit = Page("edit",editAttr,editLinked)
    
    homeLinked = [view,edit]
    home = Page("home",homeAttr,homeLinked)

    ps = [home,view,edit]

    program = Program("theprogram",ps)

    program.getInfo()

    
if __name__ == "__main__": main()      
