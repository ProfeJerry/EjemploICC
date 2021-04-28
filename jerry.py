class WeirdSortee:

    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"

valores = []
wd1 = WeirdSortee("Jerry", 42, False)
valores.append(wd1)
wd2 = WeirdSortee("Gaby", 13, False)
valores.append(wd2)
wd3 = WeirdSortee("Ximena", 5,True)
valores.append(wd3)
wd4 = WeirdSortee("Samuel", 0, False)
valores.append(wd4)
wd5 = WeirdSortee("Rincon", 3, False)
valores.append(wd5)

print(valores)
valores.sort()
print(valores)