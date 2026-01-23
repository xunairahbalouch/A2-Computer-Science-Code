#Declare File data in the array {0::10, 0::1} Of array
FileData = [[''] +2 for x in range(11)]

def ReadHighScore():
   File  = open("highscore.txt", "r" ) 
   for x in range(0, 10):
    FileData[x][0] = Flie.realine().strip()
    FileData[x][1] = Flie.realine().strip()

    #.stip to remove new line character
File.close()
