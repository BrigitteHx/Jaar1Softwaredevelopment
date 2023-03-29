#game verhaallijn poging 3:

# scenarios = [ 
#   {'key' : 'start',
#     'title' : 'start scene',
#     'story' : 'Alright then, youre standing in front of the maze and you can see the 3 ways right in front of you..',
#     'options' : [ 
#         {'key' : 'a', 'next' : 'corner' ,'story' : 'A. What might be laying around that corner? Im going right! ' },
#         {'key' : 'b', 'next' : 'forward', 'story' : 'B. Id like to see more of the Maze, Im going straight forward. '},
#         {'key' : 'c', 'next' : 'left', 'story': 'C. But what about left? What will I find there? Im going to find that out. '},
#     ]
#   },
  # {'key' : 'corner' or 'left',
  # 'title' : 'corner scene',
  # 'story' : 'On the way you come across another intersection..',
  # 'options' : [
  #       {'key' : 'a', 'next' : 'route', 'story' : 'A. You choose to ignore the other ways and follow the route, lets go!' },
  #       {'key' : 'b', 'next' : 'leftleft', 'story' : 'B. Youre going left, what will that way bring you to?'},
  #       {'key' : 'c', 'next' : 'bush', 'story' : 'C. That one bush doesnt look so stable, youre not liking this maze very much and decide to climb over it..'},
  #   ]
  # },
  # {'key' : 'bush', 
  # 'title' : 'you climbed over the bush', 
  # 'story' : 'Oh no! You while you climbed over the bush you hurt yourself, a sprained ankle is never nice. \n At least you made it out of the maze quickly, congrats! You earned the *semi-good* ending.',
  # },
  # {'key' : 'forward', 
  # 'title' : 'you went forward', 
  # 'story' : 'So youve decided to keep going?\n Thats great, while youre walking forward you notice something in the distance.\n Coming closer you realise its an apple tree!\n Those apples look really good, would you like to take a break and eat some? (y/n)', 
  # 'options' : [ 
  #       {'key' : 'y', 'next' : 'yesapple', 'story' : 'Y. '},
  #       {'key' : 'n', 'next' : 'noapple', 'story' : 'N. '},
  #   ]
  # },
  # {'key' : 'yesapple', 
  # 'title' : 'you ate the apple', 
  # 'story' : 'Didnt I mention that you should ever trust a maze?!\n The apples end up being poisened and you die.\n Congratulations, you unlocked the BAD ending.\n  Not that you should be proud of it.. Better luck next time!',
  # },
  # {'key': 'noapple',
  # 'title' : 'you didnt eat the apple',
  # 'story' : 'Nice decision to see through that, those apples were poisened!\n You kept walking and walked straight into victory\n Good job, you found the exit and unlocked the GOOD ENDING!',
  # },
  # {'key' : 'leftleft' or 'route',
  # 'title' : 'bridge scene',
  # 'story' : '"Youve been on your way a little while when you a bridge in the distance. You could also still follow the route but what are you going for?',
  # 'options' : [
  #       {'key' : 'a', 'next' : 'bridgeyes', 'story' : 'A. Im up for a risk and Im going for the bridge!' },
  #       {'key' : 'b', 'next' : 'followroute', 'story' : 'B. Im not so sure about that bridge and Id rather follow the route.'},
  #   ]
    # },
  #   {'key': 'bridgeyes',
  #   'title' : 'you chose the bridge as your way out',
  #   'story' : 'So youre a though one? Crossing a bridge in a maze, I havent seen a lot people do that before.\n Too bad for you, you shouldnt have done it either...\n CRACK! \n You fell through the bridge and earned the *bad ending*.', 
  #   },
  #   {'key': 'followroute',
  #   'title' : 'you kept walking',
  #   'story' : 'Very, very wise descision to follow the route, that bridge wasnt stable at all.\n You kept going straight to the exit and found the exit!\n Congrats, you unlocked the *good ending*! Have a wonderful rest of your day.',
  #   }
  # ]



# scenarios = [ 
#   { 
#     'title' : 'start',
#     'story' : 'Alright then, youre standing in front of the maze and you can see the 3 ways right in front of you..',
#     'options' : ['Around_corner', 'Forward', 'Left'],
#   },
#   {
#     'title' : 'second_choice',
#     'story' : 'On the way you come across another intersection..',
#     'options' : ['Follow_route', 'Left_again', 'Bush_climb'],
#   },
#   {
#     'title' : 'bush',
#     'story' : 'You climbed over the bush and broke your leg',
#     'options' : 'Bad_end',
#   },
#   {
#     'title' : 'apple_tree',
#     'story' : 'You see an apple tree in the distance',
#     'options' : ['Eat_apple', 'Dont_eat'],
#   },
#   {
#     'title' : 'ate_the_apple',
#     'story' : 'You ate an apple, they were poisened',
#     'options' : 'Bad_end',
#   },
#   {
#     'title' : 'didnt_eat',
#     'story' : 'You skipped the apples and now see a bridge in the distance',
#     'options' : ['Go_over', 'Dont_go'],
#   },
#   {
#     'title' : 'Over_bridge',
#     'story' : 'You set foot on a very unstable bridge and it crubles',
#     'options' : 'Bad_end',
#   },
#   {
#     'title' : 'Finish',
#     'story' : 'You ignored the bridge and kept going, congrats!',
#     'options' : 'Good_end',
#   },
# ]

