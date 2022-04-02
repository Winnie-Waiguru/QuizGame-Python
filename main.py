print("Welcome to my computer quiz")

playing= input("Do you want to play the game? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")
score=0

question1= input("Who created python? ") 
if question1.lower()== "guido van rossum" :
   print ("correct :)")
   score += 1
else:
    print("Incorrect :(") 

question2= input("Which year was python created? ") 
if question2 == "1991":
   print ("correct :)")
   score += 1
else:
    print("Incorrect :(") 
    
question3= input("Can it be used to create websites? ") 
if question3.lower() == "yes" :
   print ("correct :)")
   score += 1
else:
    print("Incorrect :(") 
    
question4= input("Can it be used in data visualization? ") 
if question4.lower() == "yes" :
   print ("correct :)")
   score += 1
else:
    print("Incorrect :(") 
    

print("You got " + str(score) +" number of correct questions.")  
print("You got " + str((score/4) * 100) +"%")  
            