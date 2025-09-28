# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.


define r = Character("???")
define me = Character("Sulivan")

# The game starts here.

label start:

   scene black
   with fade
   me "..."

   scene killer p1
   with fade
   me "what's happening?"

   scene killer p2
   with fade
   me "where am i?"

   scene killer p1
   with fade
   me "why am i handcuffed?"

   scene killer p2
   with fade
   r "Wake up, Billionaire."


   scene killer final


   r "I trust that you are enjoying the accomodation."


   menu:
         "Yes":
            r "Perfect"


         "No":
            r "Perfect"
      


   r "You've built your life on gold and silver..."


   r "Now you'll have to tear it apart if you want to leave..."


   r "Now you'll have to tear it apart if you want to leave... alive."


   pause
   scene killer p1
   with fade
   me "no..."
   scene killer p2
   with fade
   pause
   scene killer p1
   with fade
   pause
   scene black
   pause


label startwall1:


   scene wall1


   show killer sprite at left

   r "You need 2 keys to escape"
   r "Unlock the safe to get one key...."
   r "If you can"


label wall_menu:
   scene wall1
   menu:
         "Look at Poster One":
            jump poster1
         "Look at Poster Two":
            jump poster2
         "Look at Poster Three":
            jump poster3
         "Look at TV Screen":
            jump tvScreen
         "Look at Safe":
            jump safe


label wall1taker:
   scene wall1


label poster1:
   scene wall1pic1
   pause
   jump wall_menu


label poster2:
   scene wall1pic2
   pause
   jump wall_menu


label poster3:
   scene wall1pic3
   pause
   jump wall_menu


label tvScreen:
   scene wall1tv
   r "You're exposed, your power taken away from you."
   pause
   jump wall_menu


label safe:
   scene wall1safe
   menu:
         "Enter passcode:":
            jump safe_unlock
         "Go back to wall":
            jump wall_menu


label safe_unlock:
   scene wall1safe


   $ code = renpy.input("Enter the 5-digit number passcode:")
   $ code = code.strip()   # remove spaces


   if code == "18519":   #correct code
         r "You figured it out."
         r "You're one step closer to making it out here alive."
         me "One step closer..."
         jump startwall2   # go forward in your story
   else:
         r "Wrong code. Try again. Tick tick"
         jump safe         # loop back so they can retry

#wall2


label startwall2: #FIX TO STARTWALL2 LATER
   scene wall2
   pause


   show killer sprite at left
   r "Remember this?"
   hide killer sprite


   me "..."

   show killer sprite at left
   r "Let's dive in and remember"


   hide killer sprite
   me "I don't want to remember."


   show killer sprite at left
   r "You don't want to remember what you did?"
   r "You have to."


#show option 1 option 2
   menu:
         "Look towards the left":
            jump looktoleft
          
         "Look towards the right":
            jump looktoright


label looktoleft:
   scene wall2board
   pause
   r "These are the victims that you stole money from."
   r "My grandfather, my only guardian, was one of them."


   jump looktoright2




label looktoright:
   scene wall2shelf
   pause
   r "Do you know what these are?"
   menu:
         "Yes...":
            r "These are belongings from all of my victims."
         "No...":
            r "These are belongings from all of my victims."

   r "You'll be next."
   r "I have a special spot saved just for you."
   r "MUHAhahahhaha"


   jump looktoleft2
  
label looktoleft2:
   scene wall2board
   pause
   r "This is the victims that you stole money from"
   r "My grandfather, my only guardian was one of them."
   jump startwall3


label looktoright2:
   scene wall2shelf
   pause
   r "Do you know what these are?"
   menu:
         "Yes...":


            r "Well, these are belongings from all of my victims."
         "No...":
            r "Well, these are belongings from all of my victims."
   r "You'll be next."
   r "I have a special spot saved just for you."
   r "MUHAhahahhaha"
   jump wall3

label startwall3:
   scene wall3

   show killer sprite at left
   r "Welcome to Valx."
   r "Your lab."
   r "Remember?"
   r "My grandfather died in this very lab due to chemical exposure while working."
   r "All because of you Billionaire."
   r "Let's see if you can unlock the fridge and get the second key you need to escape."
   r "MUAHAHAHAHA"

   hide killer sprite

label wall3_menu:
   scene wall3
   menu:
         "Look at top shelf":
            jump topshelf
         "Look at middle shelf":
            jump middleshelf
         "Look at bottom shelf":
            jump bottomshelf
         "Look at note":
            jump note
         "Look at lock":
            jump lock


label topshelf:
   scene wall3glass-top
   jump wall3_menu


label middleshelf:
   scene wall3glass-middle
   pause
   jump wall3_menu


label bottomshelf:
   scene wall3glass-bottom
   pause
   jump wall3_menu


label note:
   scene wall3note
   pause
   jump wall3_menu


label lock:
   scene wall3lock
   menu:
         "Enter passcode:":
            jump lock_unlock
         "Go back to wall":
            jump wall3_menu



label lock_unlock:
   scene wall3lock


   $ code = renpy.input("Enter the number passcode:")
   $ code = code.strip()   # remove spaces


   if code == "21":   #correct code
         r "Huh, I'm surprised."
         r "You counted correctly."
         r "Now you have both keys..."
         jump foundkey2


   r "Wow, you have to sacrifice something and face one more thing to make it out here alive."
   r "Can you face it?"


   menu:
         "Of course I can":
            r "You better hope that you can..."
            r "For your own sake..."
            r "MUAHAHAHAHA"


         "No...":
            r "Then this is going to be fun"
            r "MUAHAHAHAHA"


   jump startwall4   # go forward in your story
         
# loop back so they can retry


label foundkey2:
   scene key

#wall4

label startwall4:
   scene wall4
 
   show killer sprite at left
   r "This is the mind mirror"
   r "It shows our true feelings and reveals our desires, intentions and makes us..."
   r "Confront our past and sacrifice our reputation..."
   r "among other things..."
   r "You go first."

   scene wall4billionaire

   me "I just wanted money."
   me "I just wanted power."
   me "What am I like this?"
   me "What didn't I steal, kill and destroy?"
   me "Why didn't I care about those around me?"
   scene wall4tear
   me "All of this..."
   me "to get what I wanted?"
   scene wall2board

   me "I'm sorry."
   me "I'm so sorry"


   scene wall4billionaire

   r "Good."


   scene wall4killer

   r "My turn."


   r "I kill people for fun."
   r "I dream about killing people."
   
   scene black

   r "I wanted to torture you."
    
   scene wall4killer

   r "I lied..."
   r "I never planned on making you walk out here alive."
   r "Bye, bye."

   scene black

   r "Go to sleep"

   scene wall4blood
   pause


return
#end













