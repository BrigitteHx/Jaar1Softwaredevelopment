# challange examen

ScoreE = int(input("Hoeveel punten heeft uw kanidaat gescoordt in ScoreE? (0-6) "))
ScoreP = int(input("Hoeveel punten heeft uw kanidaat gescoordt in ScoreP? (0-8) "))
ScoreO = int(input("Hoeveel punten heeft uw kanidaat gescoordt in ScoreO? (0-5) "))
ScoreS = int(input("Hoeveel punten heeft uw kanidaat gescoordt in ScoreS? (0-2) "))

totalScore = ScoreE + ScoreP + ScoreO + ScoreS

if ScoreE == 4 and ScoreP == 8 and ScoreO == 0 and ScoreS == 0 :
    print("De student heeft GOED gescoord. ")

elif totalScore > 7 and totalScore < 13 and ScoreO == 0 or ScoreS == 1 and totalScore > 9 : 
    print("De student heeft VOLDOENDE gescoord.")

else :
    print("De student heeft ONVOLDOENDE gescoord. ")

