# start of script
''' function definition section '''
def hotline(): # function 1
	print ("If you know someone who is suffering from depression, act now!")
	print ("Do something before it is too late!")
	print ("Suicide hotline number: 1-800-273-8255")
def progmeaning(): # function 2
	print ("Think of this program as a happy thing. Like saying Goodbye to the world to go visit another planet. It isn't about suicide, it is about new experiences")
	print ("This is a spinoff of the HelloWorld program, it is the opposite of Hello world.")
	print ("Differences include:\n(*)More complexity for higher-end python users\n(*)Different message\n(*)Different formatting")
	print ("However, there is a build-in HelloWorld script. You can modify the program to implement it")
	'''#===
	Implement guide
	Add this script:
	print (helloWorld()) # runs function 3
	To the program section wherever you want!
	'''#===
	print ("You are free to remix this project as you please")
def helloWorld(): # function 3
	print ("Hello, world") # main helloWorld script
def statistics(): # function 4
	print ("Program statistics")
	print ("Program version: 1.04 Build 5")
	print ("Build date: April 30th 2019 ")
	print ("Production cost: $0.00 ")
	print ("Made by: Sean P. Myrick")
	print ("Written in: Python 3.7.3")
	print ("Line count: 150")
	print ("Size: 6,536 bytes (6.53 Kilobytes)")
def updateLog(): # function 5
	print ("Goodbye World update log")
	print ("Enter an ID for an entry")
	print ("First version [0]")
	print ("1.01 [1]")
	print ("1.02 [2]")
	print ("1.03 [3]")
	print ("1.04 [4]")
	ufyn = str(input("Use float? (Y/N)"))
	input1 = str(ufyn.upper())
	if (input1 == "N"):
		collectID_UL = int(input("Enter an ID to start: "))
		if (collectID_UL == 0): # version 1.00 update documentation
			print ("Goodbye world script\t\tVersion 1.00")
			print ("* Added the goodbye world script")
			print ("* Added brief documentation")
			print ("* Added hotline")
			print ("* Added program meaning")
			noMore = input("Press [ENTER] key to close")
		elif (collectID_UL == 1): # version 1.01 update documentation
			print ("Goodbye world script\t\tVersion 1.01")
			print ("* Added statistics")
			print ("* Added comments")
			noMore = input("Press [ENTER] key to close")
		elif (collectID_UL == 2): # version 1.02 update documentation
			print ("Goodbye world script\t\tVersion 1.02")
			print ("* Updated documentation")
			print ("* Organized statistics")
			print ("* Added update log")
			noMore = input("Press [ENTER] key to close")
		elif (collectID_UL == 3): # Version 1.03 update documentation 
			print ("Goodbye world script\t\tVersion 1.03")
			print ("* Updated and added feature list")
			print ("* Updated existing documentation")
		elif (collectID_UL == 4): # Version 1.04 update documentation 
			print ("Goodbye world script\t\tVersion 1.04")
			print ("* Incorporated File I/O (Reading from files) into the congratulations page")
			print ("* Updated existing documentation")
			print ("* Added an array")
	if (input1 == "Y"): # float version (as an option to include how to use float) (making this program use as many Python features as possible)
		collectID = float(input("Enter a version number to start: "))
		if (collectID == 1.00): # Version 1.00 update documentation 
			print ("Goodbye world script\t\tVersion 1.00")
			print ("* Added the goodbye world script")
			print ("* Added brief documentation")
			print ("* Added hotline")
			print ("* Added program meaning")
			noMore = input("Press [ENTER] key to close")
		elif (collectID == 1.01): # Version 1.01 update documentation 
			print ("Goodbye world script\t\tVersion 1.01")
			print ("* Added statistics")
			print ("* Added comments")
		elif (collectID == 1.02): # Version 1.02 update documentation 
			print ("Goodbye world script\t\tVersion 1.02")
			print ("* Updated documentation")
			print ("* Organized statistics")
			print ("* Added update log")	
		elif (collectID == 1.03): # Version 1.03 update documentation 
			print ("Goodbye world script\t\tVersion 1.03")
			print ("* Updated and added feature list")
			print ("* Updated existing documentation")
		elif (collectID == 1.04): # Version 1.04 update documentation 
			print ("Goodbye world script\t\tVersion 1.04")
			print ("* Incorporated File I/O (Reading from files) into the congratulations page")
			print ("* Updated existing documentation")
			print ("* Added an array")			
def arrayList(): # function 6
	array1 = [] # defines the array 
	array1.append("Good") # element 1 of the array
	array1.append("job") # element 2 of the array
	array1.append("on") # element 3 of the array
	array1.append("learning") # element 4 of the array
	array1.append("the") # element 5 of the array
	array1.append("Python") # element 6 of the array
	array1.append("Programming") # element 7 of the array
	array1.append("Language!") # element 8 of the array
	print (array1) # prints the newly created array
''' end of function definition section '''
# start of program
print ("Goodbye, world") # main goodbye world script
con1 = input("") # new line input field
print (progmeaning()) # runs function 2
con2 = input("") # new line input field
print (hotline()) # runs function 1
exit1 = str(input("Press [ENTER] key to quit (press 1 for update log, press 2 for statistics, press 3 for a special message, or just press [ENTER] key to quit)")) # confirm quit command (added in for Python Console users, since the console closes too fast without it)
if (exit1 == "1"): # update log & update log index
	print (updateLog()) # prints the update log 
	noMore = input("Press [ENTER] key to quit")
elif (exit1 == "2"): # statistics page
	print (statistics()) # prints the program statistics
	noMore = input("Press [ENTER] key to quit")
elif (exit1 == "3"): # congratulations page
	print (arrayList()) # prints the array list
	f = open("[CONGRATS].txt", "r") # opens the [CONGRATS] ASCII art text file
	print (f.read()) # prints the [CONGRATS] ASCII art text file
	noMore = input("Press [ENTER] key to quit")
else: # final else statement
	print ("Program terminated!") # final termination
# end of program
''' divider '''
"""
Used features of Python:
1. print 
2. if 
3. elif 
4. else 
5. def 
6. float 
7. int 
8. str 
9. input 
10. Comments 
11. variable1 = input 
12. function() 
13. Defining an array 
14. append
15. open 
16. .read 
"""
''' last divider '''
# end of script