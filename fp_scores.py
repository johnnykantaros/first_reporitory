"""
CS-150 Final Program #2

Name: Johnny Kantaros
Section: A

This program will open a text file with assignments
and their respective grade (including assignment name,
weight, maximum score, and your score), read the
data, and use said data to calculate a final score out of 100.
Finally, the last function will return a letter grade
depending on the score.

"""






def read_scores(file_name):
    """
    This function takes a file name as a parameter and
    returns a tuple with three important lists of
    data related to the scores (specified below).
    
    Parameter: file name of data
    Returns: A tuple containing the following lists:
            1) weights_list: list of all assignment weights
                (position 1 in data)
            2) max_scores: list of all possible maximum
               scores (position 2 in data)
            3) my_scores: list of earned scores
               (position 3 in data)
    """
            
    weights_list = []
    max_scores = []
    my_scores = []

    with open(file_name, 'r') as file_object:
        assignments = file_object.readlines()
        for data in assignments:
            new_data = data.split(',')
            weight = float(new_data[1])
            weights_list.append(weight)
            maximum = float(new_data[2])
            max_scores.append(maximum)
            scores = float(new_data[3].strip())
            my_scores.append(scores)
            
        return (weights_list, max_scores, my_scores)
  
  
  
  
  



def final_score(file_name):
    """
    This function takes a file name as a parameter
    and returns an integer representing the final
    accumulated score. The function will calculate
    a float and then round to the nearest integer
    and return.
    
    Parameter: file name of data
    Returns: Integer of final weighted grade
    """
    total_data = read_scores(file_name)
    weights_list = total_data[0]
    max_scores = total_data[1]
    my_scores = total_data[2]
    total_assignments = len(read_scores(file_name)[1])
    final_grade = 0
    for assignment in range(0,total_assignments):
        final_grade += (weights_list[assignment] * (my_scores[assignment] / max_scores[assignment]))
    return final_grade  # to round to nearest int









def letter_grade(integer):
    """
    This function takes an integer as a parameter
    and returns an appropriate letter grade for the
    score.
    
    Parameter: integer
    Returns: appropriate letter grade
    """
    
    if 90 <= integer <= 100:
        return "A"
    elif 86 <= integer <= 89:
        return "A-"
    elif 83 <= integer <= 85:
        return "B+"
    elif 80 <= integer <= 82:
        return "B"
    elif 76 <= integer <= 79:
        return "B-"
    elif 73 <= integer <= 75:
        return "C+"
    elif 70 <= integer <= 72:
        return "C"
    elif 66 <= integer <= 69:
        return "C-"
    elif 60 <= integer <= 65:
        return "D"
    else:
        return "F"





    
   
        
    




