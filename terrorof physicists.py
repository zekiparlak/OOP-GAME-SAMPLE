import random

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def getHealth(self):
        return self.health

    def setHealth(self,health):
        self.health = health

    def getName(self):
        return self.name

class Physicist():
    def __init__(self,name,gameProbsList,health,quote):
        self.name = name
        self.gameProbsList = gameProbsList
        self.health = health
        self.quote = quote
        self.positions = []

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def setHealth(self,health):
        self.health = health

    def getSpockProb(self):
        return self.gameProbsList[0]

    def getLizardProb(self):
        return self.gameProbsList[1]

    def getRockProb(self):
        return self.gameProbsList[2]

    def getPaperProb(self):
        return self.gameProbsList[3]

    def getScissorsProb(self):
        return self.gameProbsList[4]

    def getQuote(self):
        return self.quote

    def setPositions(self,positions):
        self.positions = positions

    def getPositions(self):
        return self.positions

    def addPosition(self,position):
        self.positions.append(position)

    def getInfo(self):
        print("Health:",self.getHealth())
        print("Spock Probability:",self.getSpockProb())
        print("Lizard Probability:",self.getLizardProb())
        print("Rock Probability:",self.getRockProb())
        print("Paper Probability:",self.getPaperProb())
        print("Scissors Probability:",self.getScissorsProb())

class Game:
    def __init__(self):
        self.isGameover = False
        self.lengthmaze = 9
        self.maze = [["" for x in range(self.lengthmaze)] for y in range(self.lengthmaze)]
        self.startingPoints = []
        self.hero = None
        self.heroX = None
        self.heroY = None
        self.prevSym= None
        self.quotes = None
        self.fillQuotes()
        self.feynman = Physicist("Feynman",[20,20,20,20,20],100,self.quotes[0])
        self.curie = Physicist("Curie",[35,35,10,10,10],90,self.quotes[1])
        self.schrodinger = Physicist("Schrödinger",[10,35,35,10,10],80,self.quotes[2])
        self.dirac = Physicist("Dirac",[10,10,35,35,10],70,self.quotes[3])
        self.newton = Physicist("Newton",[10,10,10,35,35],60,self.quotes[4])
        self.pauli = Physicist("Pauli",[35,10,10,10,35],50,self.quotes[5])
        self.physicists = [self.feynman,self.curie,self.schrodinger,self.dirac,self.newton,self.pauli]

    def refresh(self):
        health = 100
        for physicist in self.physicists:
            physicist.setPositions([])
            physicist.setHealth(health)
            health -= 10
        self.hero.setHealth(200)
        self.isGameover = False

    def start(self):
        self.clearScreen()
        print("...Welcome Back Hacker\n")
        name = str(input("Enter your name:"))
        self.hero = Hero(name,200)
        print("\nMaze Information")
        print("S --> Possible Starting Points.")
        print("H --> Hero")
        print("X --> Reach Point")
        print("Others are first letters of physicists who you must beat.\n")
        print("       Move Keys\n\n         Up(8)\nLeft(4) Down(5) Right(6)\n")
        print("Let's start " + self.hero.getName())
        input("Press Enter...")
        self.fillMaze()
        self.coordsPhysicists()
        while(True):
            if(self.isGameover):
                self.refresh()
                break
            self.clearScreen()
            print("----------------------")
            print("<Terror of Physicists>")
            print("----------------------")
            print("Hero Status")
            print("Name:"+str(self.hero.getName()))
            print("Health:"+str(self.hero.getHealth()))
            print("Hero Position:"+"("+str(self.heroX)+","+str(self.heroY)+")")
            print("\n-------MAZE-------\n")
            self.printMaze()
            direction = str(input(">"))
            if(direction == "8"):
                self.move(-1,0)
            elif(direction == "4"):
                self.move(0,-1)
            elif(direction == "6"):
                self.move(0,1)
            elif(direction == "5"):
                self.move(1,0)
            if((self.heroX,self.heroY) == (4,4)):
                print("You Win")
                input("Press Enter to Back...")
                self.refresh()
                break
            for physicist in self.physicists:
                if((self.heroX,self.heroY) in physicist.getPositions()):
                    self.RockPaperScissorsLizardSpock(physicist)

    def move(self,x,y):
        newCoordX = self.heroX + x
        newCoordY = self.heroY + y
        districtPoints = [(0,0),(0,4),(0,8),(4,0),(4,8),(8,0),(8,4),(8,8)]
        if(0 <= newCoordX <= 8 and 0 <= newCoordY <= 8):
            if((newCoordX,newCoordY) not in districtPoints):
                tempPrev = self.prevSym
                self.prevSym = self.maze[newCoordX][newCoordY]
                self.maze[self.heroX][self.heroY] = tempPrev
                self.maze[newCoordX][newCoordY] = "H"
                self.heroX,self.heroY = newCoordX,newCoordY

    def fillMaze(self):
        for i in range(self.lengthmaze):
            for j in range(self.lengthmaze):
                if(i == 0 or j == 0 or i == self.lengthmaze - 1 or j == self.lengthmaze - 1):
                    self.maze[i][j] = "S"
                else:
                    self.maze[i][j] = "*"
        self.maze[4][4] = "X"
        self.maze[0][0] = " "
        self.maze[0][4] = " "
        self.maze[0][8] = " "
        self.maze[4][0] = " "
        self.maze[4][8] = " "
        self.maze[8][0] = " "
        self.maze[8][4] = " "
        self.maze[8][8] = " "
        for i in range(self.lengthmaze):
            for j in range(self.lengthmaze):
                if(self.maze[i][j] == "S"):
                    self.startingPoints.append((i,j))
                elif(self.maze[i][j] == "*"):
                    pys = random.choice(self.physicists)
                    fLetterPys = pys.getName()[0]
                    self.maze[i][j] = fLetterPys
        self.heroX,self.heroY = random.choice(self.startingPoints)
        self.prevSym = self.maze[self.heroX][self.heroY]
        self.maze[self.heroX][self.heroY] = "H"

    def coordsPhysicists(self):
        for i in range(1,8):
            for j in range(1,8):
                if(self.maze[i][j] == "F"):
                    self.feynman.addPosition((i,j))
                elif(self.maze[i][j] == "C"):
                    self.curie.addPosition((i,j))
                elif(self.maze[i][j] == "S"):
                    self.schrodinger.addPosition((i,j))
                elif(self.maze[i][j] == "D"):
                    self.dirac.addPosition((i,j))
                elif(self.maze[i][j] == "N"):
                    self.newton.addPosition((i,j))
                elif(self.maze[i][j] == "P"):
                    self.pauli.addPosition((i,j))

    def printMaze(self):
        for i in range(self.lengthmaze):
            for j in range(self.lengthmaze):
                print(self.maze[i][j],end=" ")
            print()

    def fillQuotes(self):
        q1 = "Physics is like sex: sure, it may give some practical results, but that's not why we do it."
        q2 = "Be less curious about people and more curious about ideas."
        q3 = "The present is the only things that has no end."
        q4 = "Pick a flower on Earth and you move the farthest star."
        q5 = "To every action there is always opposed an equal reaction."
        q6 = "This isn't right. This isn't even wrong."
        self.quotes = [q1,q2,q3,q4,q5,q6]

    def RockPaperScissorsLizardSpock(self,physicist):
        options = ["Rock","Paper","Scissors","Lizard","Spock"]
        win = 1
        while(True):
            self.clearScreen()
            print(physicist.getName())
            print("'"+physicist.getQuote()+"'")
            physicist.getInfo()
            print("Let's Play...")
            print("Rock-Paper-Scissors-Lizard-Spock")
            print("1)Rock\n2)Paper\n3)Scissors\n4)Lizard\n5)Spock\nChoose Wisely...")
            heroSelection = str(input(">"))
            if(heroSelection in ["1","2","3","4","5"]):
                break
        pysSelection = self.getPysSelection(physicist)
        print("My Selection:",pysSelection)
        if(heroSelection == "1" and pysSelection in ["Lizard","Scissors"]):
            print("You Win")
        elif(heroSelection == "2" and pysSelection in ["Rock","Spock"]):
            print("You Win")
        elif(heroSelection == "3" and pysSelection in ["Paper","Lizard"]):
            print("You Win")
        elif(heroSelection == "4" and pysSelection in ["Paper","Spock"]):
            print("You Win")
        elif(heroSelection == "5" and pysSelection in ["Rock","Scissors"]):
            print("You Win")
        elif(options[int(heroSelection) - 1] == pysSelection):
            print("Tie")
            win = 0
        else:
            print("You Lost")
            win = -1
        if(win == 1):
            physicist.setHealth(physicist.getHealth() - 50)
            if(physicist.getHealth() <= 0):
                self.hero.setHealth(self.hero.getHealth() - physicist.getHealth())
                for position in physicist.getPositions():
                    self.maze[position[0]][position[1]] = " "
                self.maze[self.heroX][self.heroY] = "H"
                self.prevSym = " "
                physicist.setPositions([])
        elif(win == -1):
            self.hero.setHealth(self.hero.getHealth() - 50)
            if(self.hero.getHealth() <= 0):
                self.isGameover = True
                print("Game Over...")
        input("Press Enter to Continue...")

    def getPysSelection(self,physicist):
        p = random.randint(1,100)
        p1 = 0
        p2 = p1 + physicist.getSpockProb()
        p3 = p2 + physicist.getLizardProb()
        p4 = p3 + physicist.getRockProb()
        p5 = p4 + physicist.getPaperProb()
        p6 = p5 + physicist.getScissorsProb()
        if(p1 < p <= p2):
            return "Spock"
        elif(p2 < p <= p3):
            return "Lizard"
        elif(p3 < p <= p4):
            return "Rock"
        elif(p4 < p <= p5):
            return "Paper"
        elif(p5 < p <= p6):
            return "Scissors"

    def clearScreen(self):
        print(100*"\n")

class Main:
    def __init__(self):
        self.game = Game()

    def startGame(self):
        options = """
        $$$$$$$$$$$$$$$$$$$$$$$$
        $                      $
        $ Terror of Physicists $
        $                      $
        $ 1)Play               $
        $ 2)About              $
        $ 0)Exit               $
        $                      $
        $$$$$$$$$$$$$$$$$$$$$$$$"""

        while(True):
            self.clearScreen()
            print(options)
            selection = str(input(">"))
            if(selection == "1"):
                self.game.start()
            elif(selection == "2"):
                print("A maze fill with physicists and they want to play a game :O...")
                input("Press enter to continue...")
            elif(selection == "0"):
                break

    def clearScreen(self):
        print(100*"\n")

def main():
    game = Main()
    game.startGame()

main()