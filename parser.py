import openpyxl


class Parser:
    def __init__(self):
        self.file = "DB.xlsx"
        self.DB = openpyxl.load_workbook(self.file)
        self.sheet = self.DB['Лист1']
        self.parse_substance()

    def parse_substance(self):
        self.aboutSubstance = []
        countOFF = 0
        for i in range(2, 100000):
            if self.sheet["A" + str(i)].value != None:
                # TODO: двумерный список для нахождения диапазонов температур и т.д.
                self.aboutSubstance += [[self.sheet["A" + str(i)].value, str(i)]]
                countOFF = 0
            elif countOFF == 50:
                break
            else:
                countOFF += 1
        self.allSubstance = []
        for i in range(len(self.aboutSubstance)):
            self.allSubstance += [self.aboutSubstance[i][0]]
        return self.allSubstance

    def parse_env(self, substance):

        self.indexChoice = []
        for i in range(len(self.aboutSubstance)):
            if self.aboutSubstance[i][0] == substance:
                # self.allEnv += [self.sheet["B" + self.aboutSubstance[i][1]].value]
                self.indexChoice += [self.aboutSubstance[i][1], self.aboutSubstance[i + 1][1]]
                break

        self.aboutEnv = []

        for i in range(int(self.indexChoice[0]), int(self.indexChoice[1])):
            if self.sheet["B" + str(i)].value != None:
                self.aboutEnv += [[self.sheet["B" + str(i)].value, str(i)]]

        self.allEnv = []
        for i in range(len(self.aboutEnv)):
            self.allEnv += [self.aboutEnv[i][0]]
        return self.allEnv

    def parse_temp(self, env):

        for i in range(len(self.allEnv)):
            if self.allEnv[i] == env:
                start = int(self.aboutEnv[i][1])

        j = start + 1
        stop = start + 1
        while self.sheet["B" + str(j)].value == None:
            stop += 1
            j += 1

        self.aboutTemp = []
        for i in range(start, stop):
            if self.sheet["C" + str(i)].value != None:
                self.aboutTemp += [[self.sheet["C" + str(i)].value, str(i)]]
        self.allTemp = []
        for i in range(len(self.aboutTemp)):
            self.allTemp += [self.aboutTemp[i][0]]
        return self.allTemp

    def parse_press(self, temp):

        for i in range(len(self.allTemp)):
            if self.allTemp[i] == temp:
                start = int(self.aboutTemp[i][1])

        j = start + 1
        stop = start + 1
        while self.sheet["C" + str(j)].value == None:
            stop += 1
            j += 1

        self.aboutPress = []
        print(stop)
        for i in range(start, stop):
            if self.sheet["D" + str(i)].value != None:
                self.aboutPress += [[self.sheet["D" + str(i)].value, str(i)]]
        self.allPress = []
        for i in range(len(self.aboutPress)):
            self.allPress += [self.aboutPress[i][0]]
        return self.allPress