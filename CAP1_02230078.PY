################################
# Tandin Tshering Norbu
# 1YEAR ELECTRICAL ENG
# Student number:02230078
################################
# REFERENCES
# CHAT_GPT
# https://docs.python.org/3/reference/index.html
#https://www.w3schools.com/python/python_reference.asp
#https://realpython.com/tutorials/gamedev/
#https://www.youtube.com/watch?v=waY3LfJhQLY
#https://www.youtube.com/watch?v=H09PmP5tsy8
#https://www.w3schools.com/python/python_exercises.asp
################################
# Results of the program
# Program Score Iintegrate:49843
# Put your number here
# input_8_cap1.txt()
################################

# Read the input.txt file
def read_input(The_Rock_Paper_Scissors): # The def keyword defines a function in Python
    # read_input is the name of the function.
    #(The_Rock_Paper_Scissors) parentheses contain arguments that the function accepts
    Nobzs = [] #A new variable named Nobzs is created, and it refers to an empty list
    with open(The_Rock_Paper_Scissors, 'r') as games: # This line would allow you to read the contents of that file
        for Kellz in games:
            other_player_turn, final_Product = Kellz.split()
            Nobzs.append((other_player_turn, final_Product))
    return Nobzs #Returning list Nobzs

# Now Calculating the final_Product i.e the result for each turns
def calculate_score(All_Eleminations):
    Summation_result = 0
    for other_player_turn, final_Product in All_Eleminations:
        if final_Product == 'X':  # According to the given condition in the question, we lose when the final_Product is "X"
            if other_player_turn == 'A': 
                Summation_result += 3  # You lose since scissor is annihilated by rock
            elif other_player_turn == 'B':
                Summation_result += 1  # You lose since rock is annihilated by paper
            elif other_player_turn == 'C':
                Summation_result += 2  # You lose since paper is annihilated by scissors
        elif final_Product == 'Y':  # According to the given condition in the question, it is draw when the final_Product is "Y"
            if other_player_turn == 'A':
                Summation_result += 4  # It is draw since the two playes selected rock
            elif other_player_turn == 'B':
                Summation_result += 5  #  It is draw since the two playes selected paper
            elif other_player_turn == 'C':
                Summation_result += 6  #  It is draw since the two playes selected scissor
        elif final_Product == 'Z':  # According to the given condition in the question, we win when the final_product is "Z"
            if other_player_turn == 'A':
                Summation_result += 8  # You win since rock is victorious over scissor
            elif other_player_turn == 'B':
                Summation_result += 9  # You win since paper is victorious over rock
            elif other_player_turn == 'C':
                Summation_result += 7  # You win since scissor is victorious over paper
    print(f"The total score is:{Summation_result}") #final_Product : The tallied result is Summation_result

# Now to proceed with the program for the necessary output
The_Rock_Paper_Scissors= "CSF101-CAP/input_8_cap1.txt" # This provides the specific information of the file
calculate_score(read_input(The_Rock_Paper_Scissors))