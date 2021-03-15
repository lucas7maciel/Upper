import pyperclip

class tClass():
    def capitalize(self):
        textStr = ""
        upperTxt = "" 
        lastChar = " "
        
        print("Type the text, when you're done, type an 'end' line:")
        #This loop will turn all the text into a string (textStr)
        while 0 != 1:
            addTxt = input()
            
            if (addTxt == "end"):
                break
        
            textStr += addTxt + "\n"
        textStr = textStr[:-1] #Removes the last line break
                
        #Then, all letters are analyzed
        #If its predecessor is a space or line break, it will become capitalized
        for a in textStr:
            if (lastChar == " " or lastChar == "\n"):
                upperTxt += a.upper()
            else:
                upperTxt += a
        
            lastChar = a
            
        pyperclip.copy(upperTxt)
        print("")
        print(upperTxt, "\nText copied to the clipboard")
        
        
t = tClass()
t.capitalize()

e = input("Press enter to exit")