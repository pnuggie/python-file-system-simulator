files = [] # hi i am at the start
from datetime import datetime

# fake storage simulator
storagelimit = 2000

# functions and that

# login + attempts although the password is set by ME
password = "1234"

def login(): 
    attempts = 3

    while attempts > 0:
        userinput = input("enter password: ")

        if userinput == password:
            print("access granted")
            print()
            return True

        else:
            attempts -= 1
            print("wrong password, attempts left: " , attempts,)

    print("access denied")
    return False

# fake storage
def storagesize():
    total = 0

    for f in files:
        total = total + len(f["content"])

    return total

# saving the files and making them readable in a document
def savefiles():
    with open("afileexplorersave.txt", "w") as file:
        for f in files:
            file.write(
                f["name"] + "|" +
                f["content"] + "|" +
                f["author"] + "|" +
                str(f["created"]) + "|" +
                str(f["modified"]) + "\n"
            )

# loading the files and making them accessable in variables
def loadfiles():
    try:
        with open("afileexplorersave.txt", "r") as file:
            for line in file:
                name, content, author, created, modified = line.strip().split("|")

                savedfile = {
                    "name": name,
                    "content": content,
                    "author": author,
                    "created": created,
                    "modified": modified
                }

                files.append(savedfile)

    except FileNotFoundError:
            print("no save file found yet, you are new!")

# main program

loadfiles()

if login():
    
    while True: # nice menu huh
        print("total files:", len(files))

        if storagesize() >= storagelimit * 0.9: # 90% of whatever storagelimit i decide to choose
            print("warning: storage almost full!")
        
        print("""1. add new file
        2. view all files
        3. search for a file
        4. delete file
        5. rewrite file
        6. view storage
        7. exit""")

        try:
            choice = int(input("choose 1-5: "))
            print()
        except ValueError:
            print("invalid input, please enter a number 1-5")
            continue

        if choice == 1: # asks for all the content info whatever needed
            name = input("file name: ")
            content = input("file content: ")
            author = input("file author: ")

            currenttime = datetime.now().strftime("%d/%m/%Y %H:%M")

            file = { #organises it nicely with the variables
                "name": name, # key for the files name
                "content": content,
                "author": author,
                "created": currenttime,
                "modified": currenttime
            }

            if storagesize() + len(content) > storagelimit: # if fake storage + new storage (characters) is bigger than storage limit
                print("not enough storage! file not added. :(")
                print()

            else:
                files.append(file) # appends it to my file (below)
                savefiles() #saves :D
                print("file added!") # confirmation
                print()

        elif choice == 2:
            if len(files) == 0:
                print("no files yet. :(")
                print()
            else:
                for f in files: # go through all files and print them all cause we want them all
                    print("file name:", f["name"])
                    print("file author:", f["author"])
                    print("created:", f["created"])
                    print("modified:", f["modified"])
                    print()

        elif choice == 3:
            filename = input("enter file name to search: ")

            found = False

            for f in files:  # below, the .lower() makes it so anything like Hello and hello can both appear as a search result
                if f["name"].lower() == filename.lower(): # the 'name' is a key/variable, as seen above. should match
                    print("\n--- file opened ---")
                    print("name:", f["name"])
                    print("content:", f["content"])
                    print("author:", f["author"])
                    print("created:", f["created"])
                    print("modified:", f["modified"]) # e.g name: 'file (f)' 'name of the file' 
                    print()
                    found = True
                    break

            if not found:
                print("file not found. :(")
                print()

        elif choice == 4:
            filename = input("enter file name to delete: ")

            found = False

            for f in files:
                if f["name"].lower() == filename.lower(): # is what user entered same as the found file wanted

                    confirm = input("are you sure? y/n: ")

                    if confirm.lower() != "y":
                        print("deletion cancelled")
                        print()
                        found = True
                        break

                    files.remove(f)
                    savefiles() #saves that the file is gone, else it will come back
                    print("file deleted successfully.")
                    print()
                    found = True
                    break

            if not found:
                print("file not found. :(")
                print()

        elif choice == 5:
            filename = input("enter file name to edit content of: ")

            found = False

            for f in files:
                if f["name"].lower() == filename.lower(): # if what is searched matches the files assigned 'name'

                    print("current content:", f["content"])
                    
                    newcontent = input("enter changes to content (complete change): ") #cant add little edits, maybe ill do append something later

                    oldsize = len(f["content"])  # original size
                    newsize = len(newcontent) # new size of file is by converting the new content to a length

                    difference = newsize - oldsize

                    if storagesize() + difference > storagelimit: # if the storage size + change in storage size is above limit
                        print("not enough storage! file not updated.")
                        print()

                    else:
                        currenttime = datetime.now().strftime("%d/%m/%Y %H:%M")
                        f["content"] = newcontent
                        f["modified"] = currenttime # gives it a nice new modified date
                        savefiles()
                        print("file updated!")
                        print()

                        found = True
                        break

                    if not found:
                        print("file not found. :(")
                        print()

        elif choice == 6:
            print("you have used:",  storagesize() , "bytes!")
            print()

        elif choice == 7:
            savefiles() # final backup
            print("goodbye")
            break

        else:
            print("invalid choice, please select 1-5")
            print()
