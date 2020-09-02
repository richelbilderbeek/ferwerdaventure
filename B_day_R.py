# Author: Kirsten
# Date: 25/08/20
# Purpose: Text adventure pub crawl
from __future__ import print_function
import sys
import os 
# os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
# import vlc
import time

import time
import sys

try:
    import winsound
except ImportError:
    import os

def exit_game():
    print("Exiting game")
    sys.exit()

#Get player data
print("Welcome to Kirsten's No Way Near Text Adventure Pub Crawl!")

print("What's your name?")
player_name = input("Name: ").lower()

if  player_name == "richel":
    # sound_file = vlc.MediaPlayer(r'file:///C:/Users/kirst/Music/go_shawty.mp3') 
    # sound_file.play()
    time.sleep(5)

    print("Go shawty, it's your birthday. We're gonna party like it's ya birthday...Choose your preferred brand of beer", player_name)
    
else:
    print("Choose your preferred brand of beer", player_name)
    

beer = input("Type 'G' (Guinness)  or 'HJ (Hertog Jan) to guide you through: ")#.lower()


#Set player stats
player_health = 10
player_money = 5
if beer == "G":
    player_damage = -2
elif beer == "HJ":
    player_damage = -1
else:
    exit_game()
print()
#Begin adventure
print("Welcome",player_name,"; you're out for a night on the town.\
You were dropped off at the Muurstraat to make your way into town. Do you want to go left or right?")
choice = input("(Type 'left' or 'right' to) choose a direction: ")

if choice == "left": #fight path
    print("Out of bloody nowhere a guy jumps out and attacks you!")
    time.sleep(5)

    #Create attacker
    attacker_health = 5
    attacker_damage = 1

    #Combat
    while attacker_health > 0 and player_health > 0:
        print("The guy swings at you and hits you for", str(attacker_damage), "damage!")
        player_health = player_health - attacker_damage
        if beer == "G":
            print("You swing your Guinness at him, dealing", str(player_damage), "damage!")
        if beer == "HJ":
            print("You swing your Hertog Jan at him, dealing", str(player_damage), "damage!")
        attacker_health = attacker_health - player_damage

elif choice == "right": #loot path
        print("A few steps down the road you find some coins laying on the side of the road and all of a sudden you hear something.")   
        time.sleep(5)

if player_name != "richel":
    print("You're dead man. Thanks for playing")
    time.sleep(5)
    exit_game()
else:
    player_health <= 0
    player_name == "richel"
    print("Enjoy your birthday!")




input == player_name
if player_name == "Richel":
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("		 										   ")
    print("		 ==========================================")
    print("		    									   ")
    print("         										   ")
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if not player_name == "Richel":
        sys.exit() 
try:
	winsound.Beep(264, 250)
	sys.stdout.write('Ha')	
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(297, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(264, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(352, 1000)
	time.sleep(250/2000.0)
	print('you')
	winsound.Beep(330, 2000)
	time.sleep(500/2000.0)

	sys.stdout.write('Ha')
	winsound.Beep(264, 250)
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(297, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(264, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(396, 1000)
	time.sleep(250/2000.0)
	print('you')
	winsound.Beep(352, 2000)
	time.sleep(500/2000.0)

	sys.stdout.write('Ha')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 500)
	time.sleep(250/1000.0)
	sys.stdout.write('birth')
	winsound.Beep(440, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(352, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('dear ')
	winsound.Beep(330, 1000)
	print(player_name)
	time.sleep(250/2000.0)
	winsound.Beep(297, 1000)

	winsound.Beep(440, 1000)
	time.sleep(250/2000.0)

	time.sleep(500/2000.0)
	sys.stdout.write('Ha')
	winsound.Beep(466, 250)
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(466, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(440, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(352, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(396, 1000)
	time.sleep(250/2000.0)
	print('you!')
	winsound.Beep(352, 2000)
	time.sleep(250/2000.0)
except:
	os.system('beep -f 264 -l 250')
	sys.stdout.write('Ha')
	sys.stdout.flush()
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()	
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 297 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	print ('you')
	os.system('beep -f 330 -l 2000')
	time.sleep(500/2000.0)
	
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 297 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 396 -l 1000')
	time.sleep(250/2000.0)
	print ('you')
	os.system('beep -f 352 -l 2000')
	time.sleep(500/2000.0)
	
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 500')
	time.sleep(250/1000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('dear ')
	sys.stdout.flush()
	os.system('beep -f 330 -l 1000')
	print (player_name)
	time.sleep(250/2000.0)
	os.system('beep -f 297 -l 1000')
	
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	
	time.sleep(500/2000.0)
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 466 -l 250')
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 466 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 396 -l 1000')
	time.sleep(250/2000.0)
	print ('you!')
	os.system('beep -f 352 -l 2000')
	time.sleep(250/2000.0)

print ('HAPPY BIRTHDAY ' + player_name)

print ("  --------------------------------------------------------------------------------------------------------")

print ("  | |  | |    /\    |  __ \ |  __ \ \ \   / / |  _ \|_   _||  __ \|__   __|| |  | ||  __ \    /\ \ \   / /")

print ("  | |__| |   /  \   | |__) || |__) | \ \_/ /  | |_) | | |  | |__) |  | |   | |__| || |  | |  /  \ \ \_/ /  ")

print ("  |  __  |  / /\ \  |  ___/ |  ___/   \   /   |  _ <  | |  |  _  /   | |   |  __  || |  | | / /\ \ \   /  ")

print ("  | |  | | / ____ \ | |     | |        | |    | |_) |_| |_ | | \ \   | |   | |  | || |__| |/ ____ \ | |   ")

print ("  |_|  |_|/_/    \_\|_|     |_|        |_|    |____/|_____||_|  \_\  |_|   |_|  |_||_____//_/    \_\|_|   ")
