#game_info_5

DESCRIPTION = 'description'
INFO = 'info'
PUZZLE = 'puzzle'
SOLVED = False
SIDE_UP = 'up', 'forward'
SIDE_DOWN = 'down', 'back'
SIDE_LEFT = 'left',
SIDE_RIGHT = 'right',

room_solved = {'top': False, 'north': False, 'ground': False, 'east': False, 'west': False, 'south': False,}

# dictionaries met scenes
# dictionary = {
# 	keys1: {
# 		keys2: Value
# 	}
# }


maze = {
	'top': {
		DESCRIPTION: "You find yourself standing on top of the maze, you have a clear view of the choas below you, strangely you dont move.",
		INFO: "Even more strange than standing on top of this is the\ncloud that begins speaking to you.\n",
		PUZZLE: "The cloud intimidatingly asks:\nI fly without wings. I see without eyes. I move without legs.\nI conjure more love than any lover and more fear than any beast.\nI am cunning, ruthless, and tall; in the end, I rule all.'\n'What am I?'",
		SOLVED: "imagination",
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'east',
		SIDE_RIGHT: 'west',
	},
	'north': {
		DESCRIPTION: "You went straight north and come across a stone that covers the maze's way.\n You try to move the stone but it suddenly rizes up from its position..",
		INFO: "You now stand face-to-face with a giant yeti.",
		PUZZLE: "The yeti asks you, 'What bites without teeth?'", 
		SOLVED: "frost",
		SIDE_UP: 'top',
		SIDE_DOWN: 'ground',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	},
	'ground': { 
		DESCRIPTION: "You're enjoying your stay in this maze? You're in the center and decide to sit down for a little while. \nSomething feels wrong though, as if everything relies on this part of the maze.",
		INFO: "When you sit down your hand hits a golden key\nit starts to move when you grab it, it floats in front of you.\nHow odd.",
		PUZZLE: "The key floats towards an respectively sized keyhole obscured\nby dirt and grass while you follow it. It doesn't seem to turn, you'll have to look for more.",
		SOLVED: False, # gaat naar True after alle puzzels 
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	},
	'east': {
		DESCRIPTION: "You decided to take a right and see someone around the corner. \nThe figure is feeding the birds and doesnt seem to notice you. ",
		INFO: "Coming closer you see its a rough-looking man.\nHis eyes are glued to his birds.",
		PUZZLE: "The rough-looking man asks,\n'What can you keep after giving to someone?'",
		SOLVED: "your word",
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'ground',
		SIDE_RIGHT: 'top',
	},
	'west': {
		DESCRIPTION: 'You tried to back by going west? While walking backwards you bump into someone.',
		INFO: 'A terrified looking man looks you straight in the eyes.',
		PUZZLE: "The fearful man asks,\n'What can measure time, while eventually, all crumbles to it?'",
		SOLVED: "sand",
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'top',
		SIDE_RIGHT: 'ground',
	},
	'south': {
		DESCRIPTION: "You went south and found a calmer area of the maze.\n An elderly woman is sitting down at a table, reading her book upside down.",
		INFO: "You greet the old lady.\nShe mumbles something about wisdom..",
		PUZZLE: "What can you break, even if you never pick it up or touch it?",
		SOLVED: "a promise",
		SIDE_UP: 'ground',
		SIDE_DOWN: 'top',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	}
}