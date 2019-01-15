

class Brainfuck(object):

    def setMemory(self, memory):
        self.variables = memory

    KOMMA = ","
    BRACKET = "[]"

    oldCode = ""

    index = 1
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
                    self.setCurrent(self.extra)
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
            if(self.getCurrent() != 0):
                self.redoCode()
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


    def getIntex(self):
        while(self.index < 0):
            self.index += self.variables.lenth
        self.index %= self.variables.lenth
        return self.index

    def getCurrent(self):
        return self.variables[self.getIndex()]


    def setCurrent(self, value):
         self.variables[self.getIndex] = value


    def redoCode(self):
        redoIndex = self.oldCode.length - 1
        loopsToPass = 1
        while(True):
            if(self.oldCode[redoIndex] == '['):
                loopsToPass -= 1
                if(loopsToPass <= 0):
                    self.executeCode(self.oldCode[redoIndex:])
                    return
            elif(self.oldCode[redoIndex] == ']'):
                loopsToPass += 1


brainfuck = Brainfuck()

brainfuck.setMemory([0, 0, 0, 0, 0])

brainfuck.executeCode(">>++-.,")

print(brainfuck.index)



