from tkinter import Tk , Label, Button, Frame, messagebox, Entry

import random as rnd

class Die:
    MIN_SIDES = 2
    MAX_SIDES = 120

    def __init__(self, numberOfSides):
        self.__numberOfSides = numberOfSides
        self.__value = 0
    # end method

    def setSides(self, numberOfSides):
        if numberOfSides >= self.MIN_SIDES and numberOfSides <= self.MAX_SIDES: 
            self.__numberOfSides = numberOfSides
        # end if
    # end method    

    def getSides(self):
        return self.__numberOfSides
    # end method
    def getValue(self):
        return self.__value
    # end method

    def roll(self):
        self.__value = rnd.randrange(self.__numberOfSides) + 1
    # end method

    def __str__(self):
        return str(self.getValue())
    # end method
# end class


class Dice:
    def __init__(self, numberOfDice, numberOfSides):
        self.__numberOfDice = numberOfDice
        self.__numberOfSides = numberOfSides
        self.__dice = []
        self.__buildDice()
    # end method

    def __buildDice(self):
        for _ in range(self.__numberOfDice):
            self.__dice.append(Die(self.__numberOfSides))
        # end for

        self.roll()
    # end method

    def roll(self):
        for die in self.__dice:
            die.roll()
        # end method
    # end method

    def getTotal(self):
        total = 0

        for die in self.__dice:
            total += die.getValue()
        # end for

        return total
    # end method

    def getValues(self):
        values = []

        for die in self.__dice:
            values.append(die.getValue())
        # end for

        return tuple(values)
    # end method

    def __str__(self):
        string = ""
        string = "Dice Total: " + str(self.getTotal()) + "\n\n"
        count = 0
        for die in self.__dice:
            count += 1

            if count == 1:
                string += "Die " + str(count) + ": " + str(die.getValue())
            else:
                string += "\nDie " + str(count) + ": " + str(die.getValue())
            # end if
        # end for

        return string
    # end method

# end class

class Form:
    def __init__(self, window):
        self.window = window
        self.window.title("First GUI program")
        self.window.geometry("250x100")
        #self.window.resizable(False, False)

        #frame
        self.fraTop = Frame(self.window)
        self.fraMid = Frame(self.window)
        self.fraBottom = Frame(self.window)
        self.fraBtn = Frame(self.window)
        #self.window.resizable(False, False)

        #controls
        self.lblNumberOfSides = Label(self.fraTop, text = "Number of sides: ")
        self.lblNumberOfDice = Label(self.fraMid, text = "Number of dice: ")

        #textbox
        self.txtNumberOfSides = Entry(self.fraTop, width = 5)
        self.txtNumberOfDice = Entry(self.fraMid, width = 5)

        #button
        self.btnClickMe = Button(self.fraBtn, text = "Roll", command = self.eventButtonClick)
        self.btnExit = Button(self.fraBtn, text = "Exit", command = self.window.destroy)

        #packs        
        self.lblNumberOfSides.pack(side = "left")
        self.txtNumberOfSides.pack(side = "right")
        self.lblNumberOfDice.pack(side = "left")
        self.txtNumberOfDice.pack(side = "right")
        self.btnClickMe.pack(side = "left")
        self.btnExit.pack(side = "right")
        

        #pack frames        
        self.fraTop.pack()
        self.fraMid.pack()
        self.fraBottom.pack()
        self.fraBtn.pack()

        # Create all widgets/controls below here
    # end method
    def eventButtonClick(self):
        #returns strings
        numberOfSides = self.txtNumberOfSides.get()
        numberOfDice = self.txtNumberOfDice.get()
        # if numberOfSides > 120:
        #     "Please enter a side value less than 120."

        if numberOfSides.isdigit() and numberOfDice.isdigit() and int(numberOfSides) < 120:
            numberOfDice = int(numberOfDice)
            numberOfSides = int(numberOfSides)
            myDice = Dice(numberOfDice, numberOfSides)
            myDice.roll()

            messagebox.showinfo("Dice Roller", str(myDice))
        
        else:
            messagebox.showerror("Dice Roller",
            "Please enter numberic values less than 120 for bother number of sides and number of dice")
        
# end class

def main():
    window = Tk()
    myForm = Form(window)
    window.mainloop()
# end method

# Call main method
main()