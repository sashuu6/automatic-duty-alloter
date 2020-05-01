import csv
import datetime


# Definition to input csv data to variable
def inputCSV(fileName):
    studentName = []
    with open(fileName) as csvFile:
        name = csv.reader(csvFile, delimiter=',')
        for row in name:
            studentName.append(row[0])
    return studentName


# Definition to perform duty allotment
def seatAlloter(list1, list2, list3):
    finalList = []
    p = 0
    q = 0
    r = 0
    for i in range(0, 4):
        dayList = []
        for j in range(0, 7):
            if j % 3 == 0:
                if p != len(list1):
                    dayList.append(list1[p])
                    p += 1
            elif j % 3 == 1:
                if q != len(list2):
                    dayList.append(list2[q])
                    q += 1
            elif j % 3 == 2:
                if r != len(list3):
                    dayList.append(list3[r])
                    r += 1
            if p == len(list1):
                p = 0
            if q == len(list2):
                q = 0
            if r == len(list3):
                r = 0
        finalList.append(dayList)

    return finalList


# Definition to store allotment output to a file
def textFileOutput(data):
    file = open("./output/output.txt", 'w')
    file.write("Call Centre Duty Allotment for JPHN Trainees\n")
    date = datetime.datetime.now()
    sl = 1
    flag = 0
    for i in data:
        if (flag % 2 == 0):
            date += datetime.timedelta(days=1)
            file.write("\nDay - " + str(sl) +
                       " (" + str(date.strftime("%d %B %Y %A")) + ")\n")
            file.write("\nMorning Batch\n\n")
            sl += 1
        else:
            file.write("\nNoon Batch\n\n")
        sl1 = 1
        for j in i:
            file.write(str(sl1) + ". " + str(j) + "\n")
            sl1 += 1
        flag += 1


# Main definition
def main():
    studentList1 = inputCSV('./data-files/list1.csv')
    studentList2 = inputCSV('./data-files/list2.csv')
    studentList3 = inputCSV('./data-files/list3.csv')

    textFileOutput(seatAlloter(studentList1, studentList2, studentList3))


if __name__ == "__main__":
    main()
