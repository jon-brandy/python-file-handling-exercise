from sys import exit

def menu():
    print("==================================")
    print("| Chose 1 for Average            |")
    print("| Chose 2 for Max                |")
    print("| Chose 3 for Average and Max    |")
    print("| Chose 4 for Display All Data   |")
    print("==================================")
    print("")

def displayData():
    with open("data.txt") as f:
        a = f.readlines()
        s = a[idx].split()
        k = [int(a[idx]) for a[idx] in s[1:]]
        print(s[0], ":", k)

with open("data.txt") as f:
    a = f.readlines()  # tiap baris dalam file
    name = [i.split()[0] for i in a]
    print("Who do you want to search?")
    query = input("Enter Name : ")
    print("--------------------------")
    print("")

    idx = 0
    try:
        idx = name.index(query)
        menu()
    except:
        print("Name not found!")
        exit(0)  # berhasil = 0

    chose = int(input("Enter A Number: "))
    print("")
    s = a[idx].split()
    s = [int(i) for i in s[2:]]

    match chose:
        case 1:
            print("Average :", sum(s) / 4)
        case 2:  # default
            print("Max :", max(s))
        case 3:
            print("Average :", sum(s) / 4)
            print("Max :", max(s))
        case 4:
            displayData()
