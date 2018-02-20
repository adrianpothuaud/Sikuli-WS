Example Werk1
========

Werk1 Test Framework for the www.werk1muenchen.de web site

## Prerequisites

1. Get Sikuli IDE and Sikuli Script from [Sikuli.org][1]
2. Check if you can run Sikuli IDE and Sikuli Script
	This can be a little bit tricky on Linux; Windows and Mac should work just fine
3. Download jepysi; Guess you already did this :-)
4. Copy the "runner.sikuli" folder to the Werk1 example test folder

## Running Tests

I only describe the mac desktop variant. Windows and Linux should be similar, when it comes to the parameters. Installing and finding the correct path depends on your installation.

If you need help to set up Jenkins and VM Agents to run JePySi tests, feel free to contact me.

* General call:

		<path to sikuli script>runScript -r runner [-f <logfile for sikuli>] -- <Environment> <feature oder feature path>

	`Important remark`: No wildcard support for feature files or folders
	 
### Run a single test

	/Applications/SikuliX-IDE.app/Contents/runScript -r runner -f debug.txt -- PROD features/extras.feature

1. **runScript**

		/Applications/SikuliX-IDE.app/Contents/runScript

	Obviously the first part of the line is the call to the Sikuli script.

2. Parameter **-r**

		-r runner
	
	Tells the Sikuli Script which sikuli project to run.
	
3. Optional parameter **-f**

		-f debug.txt 

	With this parameter the output from sikuli can be captured into a file. Combined with the **-d <#>** (# = 1-4) parameter you can get detailed information whats going on in sikuli.
	
4. Parameter **--**
	This parameter signals sikuli that the following parameters are for the running sikuli script.
	
5. Parameter **PROD**
	
		PROD
		
	This is a free Environment name, which corresponds with the definitions in the feature files. Usually I use LOCAL, DEV, STAGE, PROD. Unfortunately even if you don't use environment features, you have to provide a dummy parameter, since the parameter evaluation uses fixed positions. 
	
	In this example I only use the PROD environment, since I have no access to the DEV, STAGE or LOCAL environment.
	
6. Parameter **features/extras.feature**

		features/extras.feature

	With this parameter you specify exactly one feature in the "sikuli" feature file. The extension ".feature" is mandatory. The name, in this case "sikuli" is variable. There is one exception. Feature files starting with "_" are treated as special files.
	
	E.g. "_.feature" in the root feature folder is the place for all common definitions. 
	
	Or "_extras.feature" holds special definitions or overwrites for the "extra" feature.


### Run all tests in a folder

	/Applications/SikuliX-IDE.app/Contents/runScript -r runner -f debug.txt -- PROD features/

Most of the parameters are the same, except now the script runs all features in all feature files in the "features/" folder.


### Run all tests

	/Applications/SikuliX-IDE.app/Contents/runScript -r runner -f debug.txt -- LOCAL features/
	
As you might guessed, now all feature tests are run.

## Remarks

1. Logging and Reporting

	JePySi stores all screenshots and the logs CSV file in the "logs" folder within the "test" root folder. Same is done with the junit reports in the "reports" folder.
	
	The normal output from the sikuli runner script is not captured. It is only, on Mac and Linux with ASCII coloring, displayed on the Console. Within Jenkins it is only in B&W.
	
	If you don't specific the **-f** parameter you get the Sikuli specific messages mixed in. The amount of Sikuli messages depends on the **-d** option from Sikuli.
	
2. No deleting

	All files in the "logs" and the "reports" folder are persistet. Exception, the CSV file and the junit reports files are overwritten. There is an option for the "logs" folder to use a date formated subfolder.

3. No quarantee

	Since the content of the Werk1 web page is in constant change, the example may not work in full detail. Also the example was only tested on Mac OS X, so Windows or Linux might need some adjusted screen pattern files (images). 


[1]: http://sikuli.org