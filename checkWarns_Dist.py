# -*- coding: utf-8 -*-
import os, time, sys, msvcrt as m

while True:
    os.chdir(os.path.dirname(sys.argv[0]))
    try:
        check = open("run_checker.bat", 'r+')
    except:
        check = open("run_checker.bat", 'w')
        check.write("cd " + str(sys.executable)[0:str(sys.executable).rfind("\\")] + "\ncolor 2e\npython \"" + str(os.path.dirname(sys.argv[0])) + "\\checkWarns_Dist.py\"")
        check.close()
    
        
    try:
        source = open("Warns.txt", 'r+', encoding='utf-8')
    except:
        source = open("Warns.txt", "w")
        source.close()
        source = open("Warns.txt", "r+", encoding='utf-8')
    
    data = source.read()
    def clear():
        os.system('cls')
        print("=" * 120)
    
    def CheckWarn(ID):
        #print(data.split(" "))
        bigData = []
        for x in data.split(" "):
            #print(x)
            if x == ID:
                nuData = data.split("\n")
                for y in nuData:
                # print(y)
                    if ID in y:
                        foundData = nuData[nuData.index(y)].split(" ")
                       # print(foundData)
                        Name = foundData[0][2:]
                        #print(Name)
                        try: 
                            
                            Name = Name.split("_")
                           # print(Name, " split")
                            Name = " ".join(Name)
                            #print(Name, " joined")
                        except:
                            pass
                        #print(Name)
                        #print(foundData[1])
                        bigData.append((Name, foundData[1][1:len(foundData[1]) - 1], " ".join(foundData[3:])))
        if not bigData:
            bigData = [("NOT FOUND", "NOT FOUND", "NOT FOUND")]
        return(bigData[0:len(bigData) // 2] if len(bigData) > 1 else bigData)
       # return(("NOT FOUND", "NOT FOUND", "NOT FOUND"))
    # return False
    
    def NewWarn(Name, ID, Desc):
    # global data
    
        curSlot = "*\t" + Name + " (" + ID + ")" + " - " + Desc
        #curSlot = curSlot.decode("utf-8")
        return curSlot
        
    def quit():
        clear()
        tot = ""
        for x in "Goodbye...":
            tot += x
            print(tot)
            
            time.sleep(0.2)
            clear()
            
        time.sleep(0.3)
        sys.exit()
        
    #main body
    cont = 0
    def writeReadMe():
        readMe = open("ReadMe.txt", 'w')
        readMe.write("Hello, and welcome to my warning checker! \nThis warning checker is a free program and is not for commercial redistribution, so if I catch you selling it I will blacklist you.")
        readMe.write("\n\nThe program is really simple, the only thing I recommend doing is making a shortcut for it so that you can run it easily.\n")
        readMe.write("This can be done by right-clicking 'run_checker.bat' and then 'create shortcut'. One you've done this, right-click the shortcut and go to 'properties'")
        readMe.write("\nFrom properties, goto 'target' and add 'Explorer' in front of your target. This will look like:\n\n")
        readMe.write("Explorer \"[Path Name]\\run_checker.bat\\\"\n\n")
        readMe.write("You can then pin this to your taskbar or start menu for ease of use.\nThis program will also automatically restore missing files, except for the main .py file. \nEnjoy!")
        
    while cont == 0:
        clear()
        if "Here are you warns:" not in data:
            print("Hello, welcome to the warning checker!\nby Alex (Huey Emmerich)\nPlease read the readme!\n\nPress any key to continue...")
            writeReadMe()
            source.write("Here are you warns:\n")
            m.getch()
            clear()
        
        Choice = input("\n1: Check Warning \n2: New Warning\n3: Quit\n\n:: ")
        
        try:
            Choice = int(Choice)
            if Choice == 1 or Choice == 2 or Choice == 3:
                cont = 1
            else:
                print("Please choose a valid number.")
                time.sleep(1)
        except:
            print("Please choose a valid number.")
            time.sleep(1)
    
    if int(Choice) == 1:
        clear()
        
        output = CheckWarn("(" + input("Steam ID: ") + ")")
        clear()
        #print(output)
        for x in output:
            #print(output)
            print('Name: \n{0} \n\nID: \n{1} \n\nReason: \n{2}'.format(x[0], x[1], x[2]))
            print("=" * 120)
        m.getch()
    
    elif int(Choice == 2):
        clear()
        Name, SteamID, Desc = "_".join(input("\nName: ").split(" ")), input("\nSteam ID: "), input("\nDescription: ")
        output = NewWarn(Name, SteamID, Desc)
        PseudoName = NewWarn(" ".join(Name.split("_")), SteamID, Desc)
        clear()
        cont = 1
        while cont == 1:
            yourAnswer = input("\nIs this correct: \n" + PseudoName + "\n\n1: Yes\n2: No\n\n:: ")
            try:
                if int(yourAnswer) == 1:
                    cont = 0
                    source.write('\n' + output)
                    
                    print("\n\nWritten to file: \n" + PseudoName)
                    #print("\n\nWritten to file: \n" + output)
                    m.getch()
                else:
                    clear()
                    cont = 0
                    print("\nAction canceled")
                    
                    time.sleep(1)
            except:
                print("\n\nPlease give a valid response.")
                time.sleep(1)
                os.system('cls')
    else:
        quit()
        #print(output)
    source.close()
    os.system('cls')
    