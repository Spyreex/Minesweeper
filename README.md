Spyreex' Minesweeper version 1.4
-----


How to download 101

Method 1:
Go to the 'download' folder on github and download the latest version (might not be completely up to date)

Method 2:
Download the following files to get the most up to date version:

	-All the maps with numbers (these are the images for the numbers)

	-README.md (not needed)

	-minesweeperv2.py

	-records

	-where.exe

	-newgame.bat

-----

How to install 101

1. Open 'where.exe', this edits 'newgame.bat'.
2. Open 'newgame.bat'
-----

Using a grid with a multiplication of 5 will make nunmbers appear. This could significantly reduce game performance when too many images have to be loaded in
-----

Google Minesweeper modes:
Easy		10x8 1/8 (10)
Medium		18x14 1/6 (40)
Hard		24x20 1/5 (99)
-----

Press the '?' button for help about the options for the field.


records file explanation

	Example:
		.-----------------------.
		|20;15;5		|
		|~~~			|
		|Spyreex:0:0:44:850	|
		|~~~			|
		|			|
		|---			|
		.-----------------------.
	End of example
	
	Explanation:
		[20 	--> Width of field]	[15 	--> Height of field]	[5 	--> 1 out of 5 is a mine]
		[~~~	--> Break line, start of records]
		[Spyreex--> Name]		[0	--> Hours]		[0	--> Minutes]	[44	--> Seconds]	[850	--> Milliseconds]
		[~~~	--> Break line, end of records]
		[	--> Break for visibility sake]
		[---	--> End of catagory]
	End of explanation
-----


Patch notes 1.1

	Added
		-Ability to select Grid size that are not multiplacable by 5 and/or greater than 30.
	
	Removed
		-Some print statements
		-Herobrine
		
	Changed
		-Added extra lines in 'records' for better visibility?
		-Help button improved
			
	Bugfixes
		-Fixed recursion error for higher numbers, (still not enormous numbers).
-----

Patch notes 1.2
		
	Added
		-Executable file to install program
	
	Removed
		-Herobrine

	Bugfixes
		-Major bugfix for being unable to submit scores
-----

Patch notes 1.3

	Added
		-Button to see the records

	Removed
		-Herobrine
-----

Patch notes 1.4

	Changed
		-Changed how mines work, now has to be atleast 1/start2	amount of mines out of the total tiles

	Removed
		-Herobrine

-----

Patch notes 1.5
	
	Changed
		-Now removes the help and records button when a new game starts, to prevent the game from freezing when you click the buttons

-----

Future?

	-Online database for records