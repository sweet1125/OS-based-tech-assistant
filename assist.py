import os
import pyttsx3 

os.system("color fc")
os.system("cls")
pyttsx3.speak("Hello I am Jarvis,your text-cum-tech asssistant")
print("\n\n\t\t\tHello I am Jarvis,your 'text-cum-tech asssistant'")
pyttsx3.speak("Here is what I can do for you")
pyttsx3.speak("I can open or close OS based program you type here.   Try typing 'open chrome' and it will be open for you")
print("\n\tI can open or close OS based program you type here.")
print("\n\tTry typing 'open chrome' and it will be open for you :-)")
print("\n\tNOTE:You must type your request in lowercase letters")
pyttsx3.speak("Before getting started I recommend you to type 'help' to get familiar with my functionality.")
print("\n\tYou can type 'help' to get more familiar with me")
print("\n\tTo stop me anytime,you must type 'stop jarvis',that's it!\n")

while True:	
	print("\n\n\tPlease type in your requirement here",end="\n\n\t\t\t\t\t\t\t")
	p=input()
	if("stop jarvis" in p):
		pyttsx3.speak("Sure it's nice to meet you,have a marvellous day ahead ,it's jarvis signing off")
		print("\n\n\tSure,nice to meet you! Have a marvellous day ahead....!")
		os.system("color")
		exit()



	elif("n't"in p)or(" not "in p)or("never"in p):
		print("\n\tOkey!")	



	elif("open" in p)or("launch"in p)or("run"in p)or("start"in p)or("execute"in p)or("begin"in p)or("initiate"in p):
		if(" edge " in p):
			os.system("start msedge")
		elif("chrome" in p)or("browser"in p)or("web"in p):								
			os.system("start chrome")
		elif("notepad" in p)or(("text"in p )and("editor"in p))or("editor"in p):
			os.system("start notepad")
		elif("paint" in p)or("draw"in p)or("sketch"in p):
			os.system("start mspaint")		
		elif("music" in p)or("song"in p)or("audio"in p)or("wmplayer"in p)or((("music"in p)or("song"in p)or("audio"in p))and(" play"in p)):
			os.system("start wmplayer")
		elif("snip" in p):
			os.system("start SnippingTool")
		elif(("math" in p)and("input panel"in p))or("mip"in p):
			os.system("start mip")	
		elif("task manager"in p):
			os.system("start taskmgr")
		elif("wordpad" in p):
			os.system("start wordpad")							
		else:
			print("Don't support!")	



	elif("close"in p)or("end"in p)or("terminate"in p)or("halt"in p)or("kil"in p)or("cease"in p)or("finish"in p)or("conclude"in p)or("delete"in p)or("stop"in p)or("eliminate"in p):
		if("chrome"in p):
			os.system("taskkill /IM chrome.exe /F")
			print("\n\tClosed chrome successfully!Above is the details of your termination.")
		elif("edge" in p):
			os.system("taskkill /IM msedge.exe /F")
			print("\n\tClosed microsoft edge successfully!Above is the details of your termination.")
		elif("notepad"in p):
			os.system("taskkill /IM notepad.exe")
		elif("paint" in p)or("draw"in p)or("sketch"in p):
			os.system("taskkill /IM mspaint.exe")
		elif("snip" in p):
			os.system("taskkill /IM SnippingTool.exe")
		elif("wordpad" in p):
			os.system("taskkill /IM wordpad.exe")
		elif("music" in p)or("song"in p)or("audio"in p)or("wmplayer"in p)or((("music"in p)or("song"in p)or("audio"in p))and(" play"in p)):
			os.system("taskkill /IM wmplayer.exe /F")
			print("\n\tClosed window media player successfully!Above is the details of your termination.")			
		elif(("math" in p)and("input panel"in p))or("mip"in p):
			os.system("taskkill /IM mip /F")
			print("\n\tClosed math input panel successfully!Above is the details of your termination.")			
		elif("task manager"in p):
			os.system("taskkill /IM taskmgr.exe /F")
			print("\n\tClosed task manager successfully!Above is the details of your termination.")			
	
		else:
			print("Don't support!")			



	elif("help" in p):
		print("\n\n\t\t*******Hello user!here is your getting started guide*******\n\n\n")
		print("\t1.Please type your requirement in lowercase letter\n")
		print("\t2.To open a program you can use any of the following words with program name itself:-")
		print("\t'open','launch','run','start','execute','begin','initiate'\n")
		print("\t3.To close a program you can use any of the following words with program name itself:-")
		print("\t'close','stop','terminate','delete','eliminate','kill','end','finish','cease','halt','conclude'\n")
		print("\t4.To stop me anytime,please type 'stop jarvis'\n")
		print("\t5.Here's the list of program,I can help you with")
		print("\t  ->notepad\n\t  ->wordpad\n\t  ->chrome\n\t  ->microsoft edge")
		print("\t  ->paint\n\t  ->snipping tool\n\t  ->task managert\n\t  ->window media player\n\t  ->math input panel\n")
		print("\t6.Default program list:-")
		print("\t  ->browser:chrome\n\t  ->text-editor:notepad\n\t  ->music player:window media player\n")
       


	else:
		print("Don't support!")
