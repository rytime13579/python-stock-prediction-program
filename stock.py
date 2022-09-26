import time
try:
    import os
except:
    print("please import OS modual for auto installer to work")
    print("(pip install os)")
    input("press enter to continue....")
    exit()
try:
    import datetime,keyboard,sys,csv
    from yahoo_fin.stock_info import *
    import yahoo_fin.stock_info as si
except:
    print('installing moduals...')
    time.sleep(1)
    os.system("pip install --upgarde pip")
    os.system("pip install datetime")
    os.system("pip install yahoo_fin")
    os.system("pip install keyboard")
    os.system("pip install pandas")
    os.system("pip install requests_html")
try:
    import datetime,keyboard,sys,csv
    from yahoo_fin.stock_info import *
    import yahoo_fin.stock_info as si
except:
    print('something went wrong, check your environment variables')
    input('press any enter to continue... ')
    sys.exit()
monthdays = {
1 : 31,
2 : 28,
3 : 31,
4 : 30,
5 : 30,
6 : 31,
7 : 31,
8 : 31,
9 : 30,
10 : 31,
11 : 30,
12 : 31
}
def getDate(time, operator):
    date = datetime.datetime.now()
    year = int(date.year)
    month = int(date.month)
    day = int(date.day)
    if operator == "+":
        day = day + time
        while day > monthdays[month]:
            day = day - monthdays[month]
            month += 1
            if month == 12:
                month = 1
                year += 1
    elif operator == "-":
        day = day - time
        while day < 0:
            day = day + monthdays[month]
            month -= 1
            if month == 0:
                month = 12
                year -= 1
    return [month, day, year]
companies = []
try:
    with open('save.txt', 'r') as text_file:
        for line in text_file:
            currentPlace = line[:-1]
            companies.append(currentPlace)
except:
    pass
companiesNoDupe = []
x = None
while True:
    keyboard.press_and_release("ENTER")
    input()
    companiesNoDupe.clear()
    for i in companies:
        if i not in companiesNoDupe:
            companiesNoDupe.append(i)
    print('\n'*1000)
    print("Companies you've looked at before: " + str(companiesNoDupe))
    print('Hello! Navigate the menue below by pressing the keys.')
    print("""
    A: Get live price on any stock
    B: Get Price of stock now VS. # of days you before today you specify
    C: Predict the future of your stock based on how many days you alow
    D: Save and exit
    """)
    if x == 2:
        break
    choice = None
    x = 0
    while x == 0:
        if keyboard.is_pressed('a'):
            print(choice, x)
            choice = 'a'
            x = 1
        elif keyboard.is_pressed('b'):
            print(choice, x)
            choice = 'b'
            x = 1
        elif keyboard.is_pressed('c'):
            print(choice, x)
            choice = 'c'
            x = 1
        elif keyboard.is_pressed('d'):
            print(choice, x)
            choice = 'd'
            x = 1
        else:
            pass
    while x == 1:
        if choice == None:
            x = 0
            break
        if choice == 'a':
            keyboard.press_and_release("ENTER")
            input()
            print('\n'*1000)
            while True:
                print("Companies you've looked at before: " + str(companiesNoDupe))
                print("Example: AAPL, GOOG, NFLX....")
                companny = input("What companny would you like to get the current price of?: ")
                try:
                    get_live_price(companny)
                    companies.append(companny)
                    break
                except:
                    print('\n'*1000)
                    print('please enter a valid companny')
            print('\n'*1000)
            currentprice = ''
            while True:
                print("hold q to escape")
                if keyboard.is_pressed('q'):
                    x = 0
                    break
                else:
                    print(currentprice)
                    currentprice = si.get_live_price(companny)
                    time.sleep(1)
                    print('\n'*1000)
        if choice == 'b':
            keyboard.press_and_release("ENTER")
            input()
            print('\n'*1000)
            while True:
                print("Companies you've looked at before: " + str(companiesNoDupe))
                print("Example: AAPL, GOOG, NFLX....")
                companny = input("What companny would you like to see change in?: ")
                try:
                    get_live_price(companny)
                    companies.append(companny)
                    break
                except:
                    print('\n'*1000)
                    print('please enter a valid companny')
            while True:
                days = input("How long would you like to go back (#of days): ")
                if days.isdigit():
                    date = getDate(int(days), "-")
                    date1 = str(date[0])+'/'+str(date[1])+'/'+str(date[2])
                    try:
                        get_data(companny, start_date = date1)
                        break
                    except:
                        try:
                            startdate = str(get_data(companny, start_date = None, end_date = None, index_as_date = False, interval = "1d")["date"][0]).split(' ')
                            print("No available data for the given date you inputed ("+date1+"). The earliest known date for this companny is: " + str(startdate[0]))
                        except:
                            print("Error retrieving data for this company.. aborting")
                            time.sleep(2)
                            companies.remove(companny)
                            x = 0
                            break
                else:
                    print('\n'*1000)
                    print('Please input a number')
            if x == 0:
                x = 0
                choice = None
                break
            print('\n'*1000)
            print("press q to escape")
            currentprice = si.get_live_price(companny)
            date = getDate(int(days), "-")
            date1 = str(date[0])+'/'+str(date[1])+'/'+str(date[2])
            oldpriceraw = get_data(companny, start_date = date1, end_date = None, index_as_date = True, interval = "1d")
            oldprice = oldpriceraw["close"].values[0]
            print("Current Live Price for", companny, "is: ", currentprice)
            print("During", date1, "the stock was worth: "+ str(oldprice))
            while True:
                if keyboard.is_pressed('q'):
                    choice = None
                    x = 0
                    break
                else:
                    pass
        if choice == 'c':
            keyboard.press_and_release("ENTER")
            input()
            print('\n'*1000)
            while True:
                print("Companies you've looked at before: " + str(companiesNoDupe))
                print("Example: AAPL, GOOG, NFLX....")
                companny = input('What Companny would you like me to predict? ')
                try:
                    get_live_price(companny)
                    companies.append(companny)
                    break
                except:
                    print('\n'*1000)
                    print('please enter a valid companny')
            print('\n'*1000)
            while True:
                days = input('How many days would you like me to make my prediction off of? ')
                if days.isdigit():
                    date = getDate(int(days), "-")
                    date1 = str(date[0])+'/'+str(date[1])+'/'+str(date[2])
                    try:
                        get_data(companny, start_date = date1)
                        break
                    except:
                        try:
                            startdate = str(get_data(companny, start_date = None, end_date = None, index_as_date = False, interval = "1d")["date"][0]).split(' ')
                            print('\n'*1000)
                            print("No available data for the given date you inputed ("+date1+"). The earliest known date for this companny is: " + str(startdate[0]))
                        except:
                            print("Error retrieving data for this company.. aborting")
                            time.sleep(2)
                            companies.remove(companny)
                            x = 0
                            break
                else:
                    print('\n'*1000)
                    print('Please input a number')
            if x == 0:
                x = 0
                choice = None
                break
            print("One Moment... this may take a while...")
            date = getDate(int(days), '-')
            date1 = str(date[0])+'/'+str(date[1])+'/'+str(date[2])
            #get prices and dates
            trends = []
            dates = []
            trend = get_data(companny, start_date = date1, index_as_date = False)
            for i in range(0, len(trend), 1):
                trends.append(trend['close'][i])
                dates.append(trend['date'][i])
            incDec = []
            change = []
            totalInc = 0
            totalDec = 0
            #get when theres an increase and when theres a decrease, the amount of that increase/decrease and add it into a total
            for i in range(0, len(trends), 1):
                temp =  0
                try:
                    if trends[i] > trends[i+1]:
                        incDec.append('decrease')
                        change.append(trends[i] - trends[i+1])
                        temp = trends[i+1] - trends[i]
                        totalDec += temp
                    elif trends[i] < trends[i+1]:
                        incDec.append('increase')
                        change.append(trends[i+1] - trends[i])
                        temp = trends[i+1] - trends[i]
                        totalInc += temp
                except:
                    break
            dates1 = []
            incDecFinal = []
            incCount = 0
            decCount = 0
            # get the date for when the decrease/increase in price happend
            for i in range(0, len(incDec), 1):
                if i+2 > len(incDec):
                    break
                if incDec[i] == incDec[i+1]:
                    if incDec[i] == "increase":
                        incCount+=1
                        dates1.append(dates[i])
                        incDecFinal.append("increase")
                    elif incDec[i] == "decrease":
                        decCount+=1
                        dates1.append(dates[i])
                        incDecFinal.append("decrease")
            final = {}
            #concatinate output
            for i in range(0, incCount+decCount, 1):
                final[incDecFinal[i] + " on " + str(dates1[i])] = "amount = " + str(change[i])
            #net change in price
            netOut = totalInc + totalDec
            #begin printing data
            print('\n'*1000)
            for key, value in final.items():
                print(key, ' : ', value)
            print('\n')
            print("Your stock increased a total of " +str(incCount) + " times for a total amount of: $" + str(totalInc))
            print("Your stock decreased a total of " +str(decCount) + " times for a total amount of: $" + str(totalDec))
            print("The net change was: $"+str(netOut))
            print('\n')
            #make a simple prediction based on trends
            if netOut > 0:
                print("Prediction: The stock will continue to increase")
            elif netOut < 0:
                print("Prediction: The stock will continue to decrease")
            print('\n')
            print('Save Data to csv? (press y/n)')
            while True:
                if keyboard.is_pressed('y'):
                    datenow = str(datetime.datetime.now()).split(' ')
                    datenow1 = datenow[1].split(':')
                    filename = companny+'_save_'+datenow[0]+'_'+datenow1[0]+'_'+datenow1[1]+'_'+datenow1[2]+'.csv'
                    with open(filename, mode = 'w+') as csv_file:
                        header = ['date', 'increase/decrease', 'amount', 'Net Change', 'Increase', 'Decrease']
                        writer = csv.DictWriter(csv_file, fieldnames=header)
                        writer.writeheader()
                        writer.writerow({'Net Change' : netOut, "Increase" : totalInc, "Decrease" : totalDec})
                        for i in range(0, incCount+decCount, 1):
                            writer.writerow({'date' : dates1[i], 'increase/decrease': incDecFinal[i], 'amount' : change[i]})
                    print("Saved to " + str(filename))
                    print("press q to escape")
                    break

                elif keyboard.is_pressed('n'):
                    print("press q to escape")
                    break
                else:
                    pass
            while True:
                if keyboard.is_pressed('q'):
                    choice = None
                    x = 0
                    break
                else:
                    pass
        if choice == 'd':
            with open('save.txt', 'w+') as text_file:
                 for listitem in companies:
                    text_file.write('%s\n' % listitem)
            sys.exit()
            x = 0
            break
