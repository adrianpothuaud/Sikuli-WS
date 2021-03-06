Sikuli Tutorial n°1
===================

*A basic script for a basic scenario*
------------------------------------

Scenario: Search 'Sikuli' in Google
-------------------------

1. open web browser
2. go to 'http://www.google.com'
3. type 'Sikuli' in search bar
4. click search button
5. wait for first result (should be SikuliX website)

How to script
-------------

*note 1: you can use Sikuli IDE to take screenshots and use other features like similarity and offsets, but we'll focus on using script editor like Atom/Sublime Text/Notepad++.*

#### Prepare the scenario

###### Replay it manualy

1. open your webbrowser
2. navigate to google
3. type and search for Sikuli

###### Take screenshots
1. Identify images to be used
2. Take screenshots with any screen capture tool
    1. Snagit
    2. Windows Snipping tool
    3. Mac shortcut CMD+MAJ+4
    4. use any other tool at your convenience
3. Ensure you have

- google.png ![google.png](1_simple_script.sikuli/google.png)
- search.png ![search.png](1_simple_script.sikuli/search.png)
- sikuli-script-home.png ![sikuli-script-home.png](1_simple_script.sikuli/sikuli-script-home.png)

###### Prepare the script
1. Create 1_simple_script.sikuli folder in your workspace
2. Create 1_simple_script.sikuli/1_simple_script.py
3. Create 1_simple_script.sikuli/1_simple_script.html (not required on Windows)
4. Move images to 1_simple_script.sikuli folder
5. Document your script and write basic common elements


		# -*- coding:utf-8 -*-

		"""

		tutos/1_simple_script.sikuli/1_simple_script.py

		Sikuli first script
		===================

		see tutos/1_simple_script.md

		Scenario
		--------

		Open webbrowser
		Go to http://www.google.com
		search for 'Sikuli'
		wait first result

		Status
		------

		OK
		date: 2/19/2018

		.. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

		"""

		from sikuli import *            # sikuli features

		# write script below

###### Write the script

		import webbrowser               # python web browser automation


		# open google
		webbrowser.open("http://www.google.com")
		wait("google.png")
		# type 'Sikuli'
		click("google.png")
		paste("Sikuli")
		wait(0.5)
		# search
		Region(200, 200, 200, 200).getCenter().click()
		wait(1)
		click("search.png")
		# wait result
		wait("sikuli-script-home.png")

###### The Final script

		# -*- coding:utf-8 -*-

		"""

		tutos/1_simple_script.sikuli/1_simple_script.py

		Sikuli first script
		===================

		see tutos/1_simple_script.md

		Scenario
		--------

		Open webbrowser
		Go to http://www.google.com
		search for 'Sikuli'
		wait first result

		Status
		------

		OK
		date: 2/19/2018

		.. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

		"""

		from sikuli import *            # sikuli features

		# write script below

		import webbrowser               # python web browser automation


		# open google
		webbrowser.open("http://www.google.com")
		wait("google.png")
		# type 'Sikuli'
		click("google.png")
		paste("Sikuli")
		wait(0.5)
		# search
		Region(200, 200, 200, 200).getCenter().click()
		wait(1)
		click("search.png")
		# wait result
		wait("sikuli-script-home.png")

###### Run the script
in a shell write


	java -jar path_to_sikulix.jar -r path_to_script.sikuli


___


[Previous Tuto]() <-----------------------------> [Next Tuto]()

___


last update 2/19/2018

:sunglasses:
