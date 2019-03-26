inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')


class Student:
    nOne = ''
    nTwo = ''
    school = 0
    score = 0


def studentKey(student):
    return student.nOne


peopleList = []
for line in inFile:
    each = line.split(' ')
    stud = Student()
    stud.nOne = each[0]
    stud.nTwo = each[1]
    stud.school = int(each[2])
    stud.score = int(each[3])
    peopleList.append(stud)
peopleList.sort(key=studentKey)
for stud in peopleList:
    print(stud.nOne, stud.nTwo, stud.score)
