# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

JSONFILE = []
ObjectAllowence = False

def EmptyList():
    listL =[]
    return listL

def AddingList(val , listL):
    listL.append(val)
    return listL

def EmptyDiction():
    dic = {}
    return dic

def CreateDiction(key,pair):
    emptyDic ={}
    emptyDic.update({key:pair})
    return emptyDic
def AddDiction(key,pair,DICTION):

    DICTION.update({key:pair})
    return DICTION

def ObjectInObject(list):

    for



def ParsingJson(file):
    jsonInfo = EmptyDiction()
    listHolder = []
    for x in file.readlines():
        listHolder.append(x)
    print(listHolder)
    ObjectInObject(listHolder)

def main():
    DIR = "TestJson.json"
    file = open(DIR)
    ParsingJson(file)


main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
