from sys import exit

knife = False
gun = False

class Game(object):

	def __init__(self, start):
		self.start = start
		
	def play(self):
		next_room_name = self.start
		
		while True:
			print "\n----------"
			room = getattr(self, next_room_name)
			next_room_name = room()

	def hallway(self):
		print "You are now in the hallway. There is a wardrobe to the left and the living room the the right."
		print "Where do you go?"
		
		next = raw_input("> ")
		
		if next == "left":
			return 'wardrobe'
		elif next == "right":
			return 'livingroom'
		else:
			print "Don't understand what you mean."
			
	def wardrobe(self):
		print "Do you really have to go to the wardrobe right now? y/n"
		
		action = raw_input("> ")
		
		if action == "y":
			print "walking"
			return 'hallway'
		elif action == "n":
			return 'hallway'
		else:
			print "Type 'y' or 'n'."
			
	def livingroom(self):
		print "You go into the bedroom, where you can smell something."
		print "scumbag is in your sofa!"
		print "You can avoid confrontation or assault this man."
		print "sneak/hit him"
		
		action = raw_input("> ")
		
		if action == "sneak":
			print "You sneak past the couch dweller."
			return 'hallway_two'
		elif action == "hit him":
			print "You shatter the lamp against his head."
			print "He wakes up!"
			print "His friend shoots and kills you."
			return 'dead'
		else:
			print "Don't understand what you mean."
			return 'livingroom'

	def hallway_two(self):
		print "You got safely past the couch dweller."
		print "Kitchen, basement or bedroom?"
			
		next = raw_input("> ")
		
		if next == "kitchen":
			return 'kitchen'
		elif next == "basement":
			return 'basement'
		elif next == "bedroom":
			return 'stairs'
		else:
			print "That's not a room."

	def kitchen(self):
		print "You dont see any bad guys."
		print "Could be wise to arm yourself.."
		print "A knife is in the drawer. Pick it up."
		print "take knife or head back?"
		global knife
		
		action = raw_input("> ")
		
		if action == "take knife":
			print "You pick up the knife!"
			knife = True
			return 'hallway_two'
		elif action == "go back":
			print "You're going back"
			return 'hallway_two'
		else:
			print "I don't understand what you mean."
			return 'kitchen'

	def stairs(self):
		print "On your way up, you hear someone speaking."
		print "They spot you! You are in trouble now!."
		
		if knife:
			print "You take your knife and kills them before they can kill you."
			return 'bedroom'
		elif not knife:
			print "The guards are storming towards you and pushes you backwards down the stairs. They kill both you and your daughter."
			return 'dead'
		else:
			return 'stairs'

	def bedroom(self):
		print "You are in your bedroom."
		print "You search around the room and finds a gun in the bedside drawer."
		print "take gun/go down"
		global gun
		
		action = raw_input("> ")
		
		if action == "take gun":
			print "You have a gun now."
			gun = True
			return 'hallway_two'
		elif action == "go down":
			print "Take the gun with you."
			return 'bedroom'
		else:
			print "Don't understand what you mean."
			return 'bedroom'
			
	def basement(self):
		print "You sneak down the stairs to the basement."
		global gun
		
		if gun:
			print "You open the basement door."
			print "You see two armed guards."
			print "You manage to kill them with your gun! You are a hero!"
			exit (0)
		elif not gun:
			print "You open the door, but the armed guards see you at once and kills you on the spot."
			return 'dead'
		else: return 'basement'

	def dead(self):
		print "Try again"
		return 'go'
		
	def go(self):
		print "John is a normal guy living in the city of Chicago." 
		print "John has a 16 year old daughter that he loves very much."
		print "At work John gets a phone call from a gang member, saying that"
		print "they have taken his daughter and will kill her if he don't pay"
		print "1 million dollars within 1 hour"
		print "They also say that if he calls the police they will kill her"
		print "John thinks for a moment wondering what he should do...."
		print "Do you want to save your daughters life? y/n"
		
		action = raw_input("> ")
		
		if action == "y":
			return 'hallway'
		elif action == "n":
			print "Coward"
			exit(0)
		else:
			print "Don't understand what you mean..."