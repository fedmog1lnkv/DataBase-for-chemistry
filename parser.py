import openpyxl


class Parser:
    def __init__(self):
        self.file = "DB.xlsx"
        self.DB = openpyxl.load_workbook(self.file)
        self.sheet = self.DB['Лист1']
        self.parse_substance()


    def parse_substance(self):
        self.about_substance = []
        countOFF = 0
        for i in range(2, 100000):
            if self.sheet["A" + str(i)].value != None:
                #TODO: двумерный список для нахождения диапазонов температур и т.д.
                self.about_substance += [self.sheet["A" + str(i)].value, "A" + str(i)]
                countOFF = 0
            elif countOFF == 50:
                break
            else:
                countOFF += 1
        return self.about_substance

    def parse_temperature(self):
        pass