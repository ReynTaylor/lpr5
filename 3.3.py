class Calculation:
    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, line):
        self.calculationLine = line

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        print("Значение calculationLine:", self.calculationLine)

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        return None

    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]

calc = Calculation()
calc.SetCalculationLine("5 + 3")
calc.SetLastSymbolCalculationLine("=")
calc.GetCalculationLine()
print("Последний символ:", calc.GetLastSymbol())
calc.DeleteLastSymbol()
calc.GetCalculationLine()