
class balloon:
    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self, Item, Col):
        self.__Health = 100
        self.__Colour = Col
        self.__DefenceItem = Item

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Change):
        self.__Health = self.__Health + Change

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

# Part (e) - Main Program
def main():
    item = input("Enter defence item: ")
    colour = input("Enter colour: ")
    balloon1 = balloon(item, colour)
    return balloon1 # Helpful for part (f)

# Part (f) - Global Function
def defend(myBalloon):
    strength = int(input("Enter opponent strength: "))
    # Subtract strength from health
    myBalloon.ChangeHealth(-strength)
    
    print("Defence item used:", myBalloon.GetDefenceItem())
    
    if myBalloon.CheckHealth():
        print("Balloon has no health remaining!")
    else:
        print("Balloon still has health.")
    
    return myBalloon

