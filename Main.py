
class Brainfuck(object):

    def setMemory(self, memory):
        self.variables = memory

    KOMMA = ","
    BRACKET = "[]"

    oldCode = ""

    index = 0
    variables = []
    waitForCommand = ""

    extra = ""

    def executeCommand(self, command):
        self.oldCode += command
        if(self.waitForCommand != ""):
            if(self.waitForCommand == self.KOMMA):
                if(command.isdigit()):
                    self.extra += command
                else:
                    self.setCurrent(int(self.extra))
                    self.extra = ""
                    self.waitForCommand = ""
            elif(self.waitForCommand == self.BRACKET):
                if(command == ']'):
                    self.waitForCommand = ""

        elif(command == '<'):
            self.index -= 1
        elif(command == '>'):
            self.index += 1
        elif(command == '['):
            if(self.getCurrent() == 0):
                self.waitForCommand = self.BRACKET
        elif(command == ']'):
            print("[ " + str(self.getCurrent()))


            if(self.getCurrent() != 0):
                self.redoCode()
                print("well")
        elif(command == '+'):
            self.setCurrent(self.getCurrent() + 1)
        elif(command == '-'):
            self.setCurrent(self.getCurrent() - 1)
        elif(command == '.'):
            print(self.getCurrent())
        elif(command == ','):
            self.waitForCommand = self.KOMMA

    def executeCode(self, code):
        for c in code:
            self.executeCommand(c)


    def getIndex(self):
        while(self.index < 0):
            self.index += len(self.variables)
        self.index %= len(self.variables)
        return int(self.index)

    def getCurrent(self):
        return self.variables[self.getIndex()]


    def setCurrent(self, value):
         self.variables[self.getIndex()] = value


    def redoCode(self):
        redoIndex = len(self.oldCode) - 2
        loopsToPass = 1
        while(True):
            if(self.oldCode[redoIndex] == '['):
                loopsToPass -= 1
                if(loopsToPass <= 0):
                    self.executeCode(self.oldCode[redoIndex])
                    return
            elif(self.oldCode[redoIndex] == ']'):
                loopsToPass += 1

            redoIndex -= 1



brainfuck: Brainfuck = Brainfuck()

brainfuck.setMemory([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #Hello World!

print("{0}: {1}".format(str(brainfuck.index), str(brainfuck.variables)))


#brainfuck.executeCode("++++++++++[>+++++++>++++++++++>+++>+<<<<-]++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
#brainfuck.executeCode("+>>+++++[-.]<.")

brainfuck.executeCode("++++++++++[>+++++++>++++++++++>+++>+<<<<-
 ]                       Schleife zur Vorbereitung der Textausgabe
 >++.                    Ausgabe von
 >+.                     Ausgabe von
 +++++++.
 .
 +++.
 >++.                    Leerzeichen
 <<+++++++++++++++.
 >.
 +++.
 ------.
 --------.
 >+.
 >.                      Zeilenvorschub
 +++.")

print(str(brainfuck.index) + ": " + str(brainfuck.variables))



