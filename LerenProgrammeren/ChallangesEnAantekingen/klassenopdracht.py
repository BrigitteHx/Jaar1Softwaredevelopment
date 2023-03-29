print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

# leeftijd = (int(input("Houd oud ben je?")))

# if leeftijd <= 12: 
#   print('Je mag naar binnen')

# if leeftijd > 12 and leeftijd <= 14:
#   pasje = (input("Heb je een pasje?"))
#   if pasje == "ja":
#       print('Je mag naar binnen')
#   elif pasje == "nee": 
#       print("sorry, je mag niet naar binnen")

# if leeftijd > 14 and leeftijd < 20:
#   print('sorry, alleen voor de jonge kinderen')

# if leeftijd >= 20:
#   naam = (input("wat is de naam van de begeleider?"))
#   if naam == "Vladimir":
#     print('Je mag naar binnen')
#   else:
#     print("sorry, bent niet welkom")

#------------------------------------------------------------------------------------------------------------------------------------------------

age = 20
pasje = 'ja'
begeleider = 'ja'
age_begeleider = 20
naam_begeleider = 'Joseph'

age = 12

if age <= 12 and begeleider == "ja" and age_begeleider >= 20 and pasje == "ja" and naam_begeleider == "Vladimir":
  print('Je mag naar binnen')
else:
  print('sorry, niet welkom')
