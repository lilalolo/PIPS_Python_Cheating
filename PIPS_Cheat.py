#Assignments week 3, Python part (3.2P.9) - Loïs van 't Wout, 12103977

def cheat(exercise_nr):
    '''This function returns the correct answer for the exercise number provided as input
        exercise_nr: number of the exercise to cheat on (string from 1-8)'''
    #Open file containing the assignment answers
    with open(r"PIPS_Week3_Assignments3.2P.py", 'r') as fp:
        #Find solution for exercise number provided
        if exercise_nr == "1":
            solution = fp.readlines()[10:21] #Lines 11-22 = solution exercise 1
        elif exercise_nr == "2":
            solution = fp.readlines()[23:32] #Lines 24-33 = solution exercise 2
        elif exercise_nr == "3":
            solution = fp.readlines()[34:42] #Etc
        elif exercise_nr == "4":
            solution = fp.readlines()[46:58]
        elif exercise_nr == "5":
            solution = fp.readlines()[60:82]
        elif exercise_nr == "6":
            solution = fp.readlines()[84:131]
        elif exercise_nr == "7":
            solution = fp.readlines()[134:141]
        elif exercise_nr == "8":
            solution = fp.readlines()[143:146]
        else: #if exercise number is not a string from 1 to 8
            print("No valid exercise number was provided, try again")
    #Return solution to user
    if solution: #Reformats the solution from a list to formatted text with indents
        solution_to_return = '\n'.join(solution)
    return(print(f"The solution is: \n {solution_to_return}"))
