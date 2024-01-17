allBooks = [
                ["9780596007126","The Earth Inside Out","Mike B",2,["Ali"]],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]
borrowedISBN = []
#Defining the start function
def start():
    #Calling the printMenu function
    printMenu()
    #Prompting user to enter the selection of their choice
    choice = input("Your selection> ")
        #If the user enters '1', 'a' or 'A' then it runs the addBook function
    if choice == "1" or choice == "a" or choice == "A":
        addBook()
    #if the user enters '2', 'r', or 'R' then it runs the borrowBook function
    elif choice == "2" or choice == "r" or choice == "R":
        borrowBook()
    # if the user enters '3', 't', or 'T' then it runs the returnBook function
    elif choice == "3" or choice == "t" or choice == "T":
        returnBook()
     # if the user enters '4', 'l', or 'L' then it runs the listAllBooks function
    elif choice == "4" or choice == "l" or choice == "L":
        listAllBooks()
    # if the user enters '5', 'x', or 'X' then it runs the exit function
    elif choice == "5" or choice == "x" or choice == "X":
        exit_1()
    # if the user enters a different input the start function runs again, prompting the user to re-enter their selection
    else:
        print("Wrong Selection! Please select a valid option")
        start()
#Function that prints the menu for the users to view
def printMenu():
        print('\n######################')
        print('1: (A)dd a new book.')
        print('2: Bo(r)row books.')
        print('3: Re(t)urn a book.')
        print('4: (L)ist all books.')
        print('5: E(x)it.')
        print('######################\n')
#Function that adds a book to the already defined list
def addBook():
    #Prompts user to enter the name of the book they would like to enter
    bookName = input("Book name> ")
    #While '%' or '*' is in the books name, it displays an error and prompts the user to re-enter the book name
    while "%" in bookName or "*" in bookName:
        print("Invalid book name!")
        bookName = input("Book name> ")
    #Prompts user to enter the author
    author = input("Author name> ")
    while True:
        #Prompts user to enter the edition
        edition = input("Edition> ")
        #Program converts the variable to an integer to test if the variable is an integer
        try:
            edition = int(edition)
            break
        #If the try is not successful the following runs another try-except
        except ValueError:
            #Program converts variable to a float
            try:
                edition = float(edition)
                #If the variable is an integer then the leaves the try-except function
                if edition.is_integer():
                    break
                #If the variable is not an integer it prins an error message
                else:
                    print("Error: Please enter a valid integer for the edition.")
            except ValueError:
                print("Error: Please enter a valid integer for the edition.")
    #Prompts user to enter ISBN
    ISBN = input("ISBN> ")
    #If the length of the ISBN is less than 13, it prints a warning message and prompts the user to re-renter ISBN
    while len(ISBN) < 13:
        print("Invalid ISBN!")
        ISBN = input("ISBN> ")
    #If the length is equal to 13 and are only digits the program multiplies each digit by the multiplier list, then funds the sum of the digits
    if len(ISBN) == 13 and ISBN.isdigit():
        multiplier = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
        total = sum(int(ISBN[i]) * multiplier[i] for i in range(13))
        #if the total is divisible by 10 the for loop cycles through the allbooks list
        if total % 10 == 0:
            for x in allBooks:
                #If the ISBN already exists in allBooks, the program restarts
                if ISBN in x[0]:
                    print("Duplicate ISBN is found! Cannot add the book.")
                    start()
                else:
                    continue
            #New list with the new values is created
            oneNewBook = [ISBN, bookName, author, edition, []]
            #This new list is appended into the allBooks list
            allBooks.append(oneNewBook)
            print("A new book is added successfully.")
            #Program starts again
            start()
        #If the total is not divisible by 10 it displays a warning message and restarts the program
        else:
            print("Invalid ISBN!")
            start()
    #If the length of the ISBN is not 13 or is all digits, the program restarts
    else:
        start()

#Defining the borrowBook function
def borrowBook():
    #Prompts user to enter the borrowers name and search term
    borrower = input("Enter the name of the borrower> ")
    search = input("Search term> ").lower()
    #if '*' is entered at the end of the 'search' input and not already borrowed
    if "*" in search:
        searchResult = [book for book in allBooks if search[:-1] in book[1].lower() and book[0] not in borrowedISBN]
    # if '%' is entered at the end of the 'search' input and not already borrowed
    elif "%" in search:
        searchResult = [book for book in allBooks if book[1].lower().startswith(search[:-1]) and book[0] not in borrowedISBN]
    #If the user enters the exact book name
    else:
        searchResult = [book for book in allBooks if search == book[1].lower() and book[0] not in borrowedISBN]
        #searchResult = [book for book in allBooks if search == book[1].lower() and borrower not in book[4] and book[0] not in borrowedISBN]
    #If the length of the searchResult is 0 then it displats a warning message and restarts the program
    if len(searchResult) == 0:
        print("No books found!")
        start()
    #Empty list is created
    t = []
    #For loop cycling through the newly created searchResult list, the borrowers name is appended in the list and the ISBN is appended in the list
    for row in searchResult:
        row[4].append(borrower)
        t.append(row[0])
    borrowedISBN.extend(t)
    #Prints letting the user know the book has been borrowed, then restarts the program
    for i in range(0, len(searchResult)):
        print("-\"%s\" is borrowed!" %(searchResult[i][1]))
    start()

#Defining the returnBook function
def returnBook():
    #Prompts user to enter the ISBN of the book they would like to return
    returnISBN = input("ISBN> ")
    #for loop cycles through the borrowedISBN list
    for x in borrowedISBN:
        #If the users input is in the borrowedISBN list then it removes that variable from the list and restarts the program
        if returnISBN == x:
            borrowedISBN.remove(x)
            for i in allBooks:
                if x==i[0]:
                    print("\"%s\" is returned!" %(i[1]))
                    break
            start()
        #If the users input is not in the borrowedISBN list then it prints a warning message and restarts the function
        else:
            continue
    print("No book is found!")
    start()

#Defining the listAllBooks function
def listAllBooks():
    #for loop cycles through the allBooks list and searches for if the book is available or unavailable
    #then prints the known information for each book in allBooks. Then proceeds to restart the program
    for x in allBooks:
        print("---------------")
        if x[0] in borrowedISBN:
            print("[Unavailable]")
        else:
            print("[Available]")
        print([x[1]][0], "-", [x[2]][0])
        print("E:", [x[3]][0], "ISBN:", [x[0]][0])
        print("Borrowed by: ", [x[4]][0])
    start()
#Defining the exit function
def exit_1():
    #Prints the required message then prints all known information to display to user the last updated list
    print("")
    print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    # for loop cycles through the allBooks list and searches for if the book is available or unavailable
    # then prints the known information for each book in allBooks. Then proceeds to restart the program
    for x in allBooks:
        print("---------------")
        if x[0] in borrowedISBN:
            print("[Unavailable]")
        else:
            print("[Available]")
        print([x[1]][0], "-", [x[2]][0])
        print("E:", [x[3]][0], "ISBN:", [x[0]][0])
        print("Borrowed by: ", [x[4]][0])
    exit()
#Start function is called
start()