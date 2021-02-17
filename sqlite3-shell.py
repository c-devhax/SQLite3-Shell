import sqlite3
import time
import os
import traceback
from sys import platform

comm_prefix = "sqlite-shell"

clear_comm = "cls"
if platform in ["linux", "linux2"]:
	clear_comm = "clear"
elif platform == "darwin":
	clear_comm = "printf '\\33c\\e[3J'"

def db_connect_interface():
	dbname = input(f"{comm_prefix}> ")
	while dbname == "":
		print("Please enter a database name.")
		dbname = input(f"{comm_prefix}> ")

	print("Please Wait...")
	print("--------------")
	try:
		db = sqlite3.connect(f"{dbname}.db")
		c = db.cursor()
		print("Database loaded!")
		return db, c
	except:
		print("something went wrong, or failed to load database!")
		print("Restart shell!")
		input()
		exit()

def print_tables(c):
	tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'")
	if tables.rowcount in [-1, 0]:
		print(f"Database is empty.")
	else:
		print("Available tables:")
		for row in tables:
			for val in row:                    
				print(val)

def get_command():
	command = input(f"{comm_prefix}> ")
	while command == "":
		print("Please enter a sqlite3 command.")
		command = input(f"{comm_prefix}> ")
	return command

def print_help():
	print("Help:")
	print("Shell Commands:")
	print("exit: Exits the program (not recommended because it doesnt close the database).")
	print("close: Closes the database, then exits the shell.")
	print("whats-new: Prints what's new in the current update.")
	print("-------------------------------------------------")
	print("Database Commands:")
	print("commit: commits/saves the database (throws an error when the changes could not be made)")

if __name__ == "__main__":
	print("Booting Sqlite3 shell...")
	print("------------------------")
	print("The required version of Python is Python 3+")
	os.system(clear_comm)
	print("SQLite3-Shell, brought to you by GeorgeCY2 and c-devhax. Please enter the name of the database you want to connect to.")
	print("-----------------------------------------------------------------------------")
	
	db, c = db_connect_interface()
	print("----------------")
	
	os.system(clear_comm)
	print("SQLite3 Shell v1.1 by GeorgeCY (Made in Python)")
	print("------------------------------")

	print_tables(c)

	while True:
		try:  
			commands = get_command()

			if commands == "close":
				c.close()
				db.close()
				print("Closing...")
				break	
			elif commands == "exit":
				print("Exitting...")
				break
				
			elif commands == "help":
				print_help()

			elif commands == "commit":
				db.commit()
				print("database commited!")
							
			elif commands.lower().startswith("info"):
				table_name = commands.split()[1]
				table_info = c.execute(f"pragma table_info({table_name})")
				for col in table_info:
					print(f"Name: {col[1]}; Data Type: {col[2].lower()}")
			else:
				output =  c.execute(f"{commands}")
			
				if not output:
					print("No output.")
				else:
					for line in output:
						print(line)

		except:
			print("Error Occured:")
			traceback.print_exc()
