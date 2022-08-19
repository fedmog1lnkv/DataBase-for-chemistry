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
                self.aboutSubstance += [[self.sheet["A" + str(i)].value, str(i)]]
                countOFF = 0
            elif countOFF == 50:
                break
            else:
                countOFF += 1
        self.allSubstance = []
        for i in range(len(self.aboutSubstance)):
            self.allSubstance += [self.aboutSubstance[i][0]]

        # для последнего элемента добавляется индекс его конца
        self.aboutSubstance[-1] = [self.aboutSubstance[-1][0], self.aboutSubstance[-1][1],
                                   int(self.aboutSubstance[-1][1])]
        while self.sheet["F" + str(self.aboutSubstance[-1][2])].value != None:
            self.aboutSubstance[-1][2] += 1
        return self.allSubstance

    def parse_env(self, substance):
        # indexChoice ищет границы элемента
        self.indexChoice = []
        for i in range(len(self.aboutSubstance)):
            if (self.aboutSubstance[i][0] == substance) and (i == (len(self.aboutSubstance) - 1)):
                self.indexChoice += [self.aboutSubstance[i][1], str(self.aboutSubstance[i][2])]
                break
            elif self.aboutSubstance[i][0] == substance:
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
        print(self.aboutEnv)

        for i in range(len(self.aboutEnv)):
            if (len(self.aboutEnv) == 1) or (i == (len(self.aboutEnv) - 1)):
                pass
            elif len(self.aboutEnv) > 1:
                self.indexChoice[0] = max(self.indexChoice[0], self.aboutEnv[i][1])
                self.indexChoice[1] = min(self.indexChoice[1], str(int(self.aboutEnv[i + 1][1])+1))

        self.aboutTemp = []
        for i in range(int(self.indexChoice[0]), int(self.indexChoice[1])):
            if self.sheet["C" + str(i)].value != None:
                self.aboutTemp += [[self.sheet["C" + str(i)].value, str(i)]]

        self.allTemp = []
        for i in range(len(self.aboutTemp)):
            self.allTemp += [self.aboutTemp[i][0]]

        self.allTemp = set(self.allTemp)

        try:
            self.allTemp = sorted(self.allTemp)
        except:
            self.allTemp = list(self.allTemp)

        self.tempDicti = {}
        for i in range(len(self.allTemp)):
            # давление для одинаковой температуры
            self.presSameTemp = []
            for j in range(int(self.indexChoice[0]), int(self.indexChoice[1])):
                if self.allTemp[i] == self.sheet["C" + str(j)].value:
                    self.presSameTemp += [[self.sheet["D" + str(j)].value, str(j)]]
            self.tempDicti[self.allTemp[i]] = self.presSameTemp

        return self.allTemp

    def parse_press(self, temp):
        self.aboutPress = self.tempDicti[temp]
        self.allPress = []

        for i in range(len(self.aboutPress)):
            self.allPress += [self.aboutPress[i][0]]

        self.allPress = set(self.allPress)
        self.allPress = list(self.allPress)

        return self.allPress

    def parse_conc(self, press):

        pass

# dicti = {"<250": [["<1,6", "4"], ["<30", "11"]]}
# {'< 200': [['< 30', '8']], '< 225': [['< 5', '5']], '< 230': [['< 10', '7']], '< 250': [['< 1,6', '4'], ['< 30', '11']], '< 290': [['< 1,6', '6']], '< 345': [['< 10', '10']], '< 475': [['< 1,6', '9']], '< 550': [['< 30', '12']], '< 600': [['Не ограничено', '13']]}
