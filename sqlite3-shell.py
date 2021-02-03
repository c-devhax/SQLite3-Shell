import sqlite3
import time
import os
import traceback
from sys import platform

clear_comm = "cls"
if platform in ["linux", "linux2"]:
    clear_comm = "clear"
elif platform == "darwin":
    clear_comm = "printf '\\33c\\e[3J'"

print("Booting Sqlite3 shell...")
print("------------------------")
print("The required version of Python is Python 3+")
os.system(clear_comm)
print("SQLite3-Shell, brought to you by GeorgeCY2 and c-devhax. Please enter the name of the database you want to connect to.")
print("-----------------------------------------------------------------------------")
dbname = input("sqlite-shell> ")
while dbname == "":
    print("Please enter a database name.")
    dbname = input("filename of db> ")

print("Please Wait...")
print("--------------")
try:
    db = sqlite3.connect(f"{dbname}.db")
    c = db.cursor()
except:
    print("something went wrong, or failed to load database!")
    print("Restart shell!")
    input()
    exit()
finally:
    print("Database loaded!")
    print("----------------")
    os.system(clear_comm)
    print("SQLite3 Shell v1.1 by GeorgeCY (Made in Python)")
    print("------------------------------")
    tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'")        
    if not tables:
        print(f"Database {dbname} is empty.")        
    else:
        print("Available tables:")            
        for row in tables:
            for val in row:                    
                print(val)

while True:
    try:  
        commands = input("sqlite> ")
        while commands == "":
            print("Please enter an sqlite3 command.")
            commands = input("sqlite> ")

        if commands == "close":
            c.close()
            db.close()
            print("Closing...")
            break
        
        if commands == "exit":
            print("Exitting...")
            break
        
        if commands == "whats-new":
            print("What's New in V1.1:")
            print("1. Minor improvements and better handling")
            print("2. Now you can use the 'SELECT' statement in any cases (like lowercase, capital etc.)[Recommended to use it in uppercase]")
            continue
        
        if commands == "help":
            print("Help:")
            print("Shell Commands:")
            print("exit: Exits the program (not recommended because it doesnt close the database).")
            print("close: Closes the database, then exits the shell.")
            print("whats-new: Prints what's new in the current update.")
            print("-------------------------------------------------")
            print("Database Commands:")
            print("commit: commits/saves the database (throws an error when the changes could not be made)")
            continue

        if commands == "commit":
            db.commit()
            print("database commited!")
            continue
        
        if commands.lower().startswith("info"):
            table_name = commands.split()[1]
            table_info = c.execute(f"pragma table_info({table_name})")
            for col in table_info:
                print(f"Name: {col[1]}; Data Type: {col[2].lower()}")
            continue

        output =  c.execute(f"{commands}")
        if not output:
            print("No output.")
        else:
            for line in output:
                print(line)

    except:
        print("Error Occured:")
        traceback.print_exc()
