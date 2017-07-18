"""
------------------------------------------------------
Program to manipulate data using searching and sorting
Created by: Roberto A. Ruiz
Created on: 2017-02-10
------------------------------------------------------
"""

import urllib.request    #this loads a library you will need.  Put this line at the top of your file.

def main():

    def readWordList():
    #Pull the list of lists from the website and format it
        dataStruc = []
        response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/data121.txt")
        for eachLine in response:
            data = eachLine.decode('utf-8').split()
            dataStruc.append(data)
        return dataStruc

    def classify(data):
        #Turn all the data into ints or floats
        for index in range(len(data)):
            
            data[index][0] = int(data[index][0])
            data[index][1] = float(data[index][1])
            data[index][2] = int(data[index][2])

        return data


    def insertionSort(data, index):
        for i in range(1, len(data)):
            #Take the first element, make a small list
            actList = data[i]
            listIndex = i - 1
            #Inside the data find the list you want to manipulate [j]
            while listIndex >= 0 and float(data[listIndex][index]) > float(actList[index]):
                data[listIndex + 1] = data[listIndex]
                listIndex = listIndex - 1
            data[listIndex + 1] = actList
        return data

        

    def binarySearch(sortedList,keyword,index):
        #Set two values to be the upper and lower limits initially
        #These limits are of the lists inside the list of lists as index values
        low = 0
        high = len(sortedList) - 1

        #Loop until the low is higher than the high which means it went through the whole list
        while low <= high:
            #Get an index value of what the middle would be
            mid = (low + high) // 2
            #Directly compare the element with the amount specified by the user and go up or down depending on how much bigger or smaller it is
            if (sortedList[mid][index] > keyword):
                high = mid - 1
            elif (sortedList[mid][index] < keyword):
                low = mid + 1
            #Once cut down all the way to a center value, return it and exit the function
            elif (sortedList[mid][index] == keyword):
                return mid
        return -1
    
    def approxDownBinarySearch(sortedList,keyword,index):
    #Set two values to be the upper and lower limits initially
    #These limits are of the lists inside the list of lists as index values
        low = 0
        high = len(sortedList) - 1

        #Loop until the low is higher than the high which means it went through the whole list
        while low <= high:
            #Get an index value of what the middle would be
            mid = (low + high) // 2
            #Directly compare the element with the amount specified by the user and go up or down depending on how much bigger or smaller it is
            if (sortedList[mid][index] > keyword):
                high = mid - 1
            elif (sortedList[mid][index] < keyword):
                low = mid + 1
            #Once cut down all the way to a center value, return it and exit the function
            elif (sortedList[mid][index] == keyword):
                return mid
        #Give the value that it got closest to before it couldn't find the actual value
        return mid

            
    def top5prices(data):
        
        #Output 5 most expencive items in data set
        data = insertionSort(data, 1)
        return [data[len(data)-1], data[len(data)-2], data[len(data)-3], data[len(data)-4], data[len(data)-5]]
    
    def leastStock(data):

        #Check the stock by accessing the second index value
        data = insertionSort(data,2)
        return [data[0],data[1],data[2],data[3],data[4]]

    def searchByID(data):
        condition = False
        data = insertionSort(data,1)
        #Checking if it gave the right input
        while condition == False:
            
            ID = input("What is the user ID you wish to search for? This must be 4 characters long and a number:\n\n")
            try:
                #If it can perform this then it can continue with the code
                ID = int(ID)
                if len(str(ID)) == len(str(data[0][0])):
                    condition = True
                else:
                    condition = False
            except:
                condition = False

        location = int(binarySearch(data, ID, 0))
        
        #If it can't find an exact value
        if location == -1:
            return "That value was not found in the database."
        return data[location]

    def printPrices(data):
        
        finalList = [] #Get it? its the last list with all nearby numbers
        #Print the prices between 5 and 10 bucks
        #start by sorting the data by price
        
        data = insertionSort(data,1)
        
        #we search for the value that is nearest to 10 since its inclusive
        maxPrice = int(approxDownBinarySearch(data,10,1))

        #we need to get the prices below the maxPrice
        uptoTenList = data[:maxPrice:]
        fromFiveToTen = uptoTenList[approxDownBinarySearch(uptoTenList,5,1)::]
        
        print(fromFiveToTen)
        
        for i in range(len(fromFiveToTen)-1):
            
            if fromFiveToTen[i][1] > 5 and fromFiveToTen [i][1] < 10:
                finalList.append(fromFiveToTen[i])
                
        return finalList

    def menu():

        #Clean and access the data
        data = classify(readWordList())
        overall = True
        
        while overall:
            
            condition = False
            #Checking if it gave the right input
            while condition == False:
        
                userInput = input("Press a letter on your keyboard that matches with the action you wish to perform.\n1. Output the 5 most expencive items in the data.\n2. Output the items with the least number of units in stock.\n3. Type in item ID to find more information on that item.\n4. Print the ids with prices between $5.00 and $10.00.\n5. Quit.\n\n")
                try:
                    #If it can perform this then it can continue with the code
                    userInput = int(userInput)
                    if len(str(userInput)) == 1:
                        condition = True
                    else:
                        condition = False
                except:
                    condition = False
            if userInput == 1:
                print("The following are the top 5 prices:\n")
                print(top5prices(data),"\n")
                
            elif userInput == 2:
                print("\n","The following are the 5 items with the least number of units:\n")
                print(leastStock(data),"\n")
                
            elif userInput == 3:
                print("\n",searchByID(data),"\n")
                
            elif userInput == 4:
                print("The following are the IDs with prices between $5.00 and $10.00:\n")
                print(printPrices(data),"\n")
                
            elif userInput == 5:
                overall = False

    menu()
main()

        

