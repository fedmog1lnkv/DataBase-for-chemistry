import openpyxl


class Parser:
    def __init__(self, filePath):
        self.DB = openpyxl.load_workbook(filePath)
        self.sheet = self.DB['Главная таблица']
        self.output = []
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
        self.output += [substance]
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
        self.output += [env]

        for i in range(len(self.aboutEnv)):
            if (len(self.aboutEnv) == 1) or (i == (len(self.aboutEnv) - 1)):
                pass
            elif len(self.aboutEnv) > 1:
                self.indexChoice[0] = max(self.indexChoice[0], self.aboutEnv[i][1])
                self.indexChoice[1] = min(self.indexChoice[1], str(int(self.aboutEnv[i + 1][1]) + 1))

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
                    self.presSameTemp += [
                        [str(self.sheet["D" + str(j)].value), str(self.sheet["E" + str(j)].value), str(j)]]
            self.tempDicti[str(self.allTemp[i])] = self.presSameTemp
        return self.allTemp

    def parse_press(self, temp):
        self.output += [temp]
        self.aboutPress = self.tempDicti[temp]
        self.allPress = []

        for i in range(len(self.aboutPress)):
            self.allPress += [self.aboutPress[i][0]]

        self.allPress = set(self.allPress)
        self.allPress = list(self.allPress)

        return self.allPress

    def parse_conc(self, press):
        self.output += [press]
        self.aboutConc = []
        self.allConc = []
        for i in range(len(self.tempDicti[self.output[2]])):
            if press == self.tempDicti[self.output[2]][i][0]:
                self.allConc += [self.tempDicti[self.output[2]][i][1]]
                self.aboutConc += [self.tempDicti[self.output[2]][i]]

        self.allConc = set(self.allConc)
        self.allConc = list(self.allConc)
        return self.allConc

    def output_table(self, conc):
        self.output += [conc]
        for i in range(len(self.aboutConc)):
            if self.output[4] == self.aboutConc[i][1]:
                self.output += [self.sheet["F" + str(self.aboutConc[i][2])].value]
                break

        return self.output

    def materials_text(self, materialNum):
        self.sheet = self.DB['Материалы']

        self.materials = materialNum.split(" ")
        self.materialsText = ""

        self.materialDicti = {}
        for i in range(2, 1000):
            if self.sheet["A" + str(i)].value != None:
                self.materialDicti[str(self.sheet["A" + str(i)].value)] = str(self.sheet["B" + str(i)].value)
            else:
                break
        for material in self.materials:
            for key in self.materialDicti:
                if material == key:
                    self.materialsText += self.materialDicti[key] + ", "

        return self.materialsText[:-2]
