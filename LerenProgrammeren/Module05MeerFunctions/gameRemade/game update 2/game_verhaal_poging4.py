#game verhaal poging 4 

scenarios = [ 
  { 
    'naam' : 'start',
    'story' : 'front of the maze, where do you want to go?',
    'options' : ['corner', 'forward', 'left'],
  },
  { 
    'naam' : 'corner',
    'story' : 'you see a tree, do you want to eat its apples?',
    'options' : ['yesapple', 'noapple'],
  },
  { 
    'naam' : 'yesapple',
    'story' : 'they were poisened, you died',
    'options' : 'badend',
  },
  { 
    'naam' : 'noapple',
    'story' : 'you ignored it and kept walking right into the exit, congrats you made it out of the maze',
    'options' : 'goodend',
  },
  { 
    'naam' : 'forward',
    'story' : 'you see a bridge, would you like to cross it?',
    'options' : ['yesbridge', 'nobridge'],
  },
  {  
    'naam' : 'yesbridge',
    'story' : 'the bridge wasnt able to carry, you fell off and died',
    'options' : 'badend',
  },
  { 
    'naam' : 'nobridge',
    'story' : 'you ignored it and kept walking right into the exit, congrats you made it out of the maze',
    'options' : 'goodend',
  },
  { 
    'naam' : 'left',
    'story' : 'theres an unstable bush, would you like to climb out of the maze?',
    'options' : ['yesclimb', 'noclimb'],
  },
  { 
    'naam' : 'yesclimb',
    'story' : 'you climbed over the bush and broke your leg',
    'options' : 'badend',
  },
  { 
    'naam' : 'noclimb',
    'story' : 'you ignored it and kept walking right into the exit, congrats you made it out of the maze',
    'options' : 'goodend',
  },
] 