#THE THREE DICTIONARIES
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0], #ARRAY WITH 4 VALUES
    "quizzes": [88.0, 40.0, 94.0],        #ARRAY WITH 3 VALUES
    "tests": [75.0, 90.0]                 #ARRAY WITH 2 VALUES
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],  #ARRAY WITH 4 VALUES
    "quizzes": [82.0, 83.0, 91.0],           #ARRAY WITH 3 VALUES
    "tests": [89.0, 97.0]                    #ARRAY WITH 2 VALUES
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],     #ARRAY WITH 4 VALUES
    "quizzes": [0.0, 75.0, 78.0],            #ARRAY WITH 3 VALUES
    "tests": [100.0, 100.0]                  #ARRAY WITH 4 VALUES
}
students=[lloyd,alice,tyler]           #ARRAY CONTAIN 3 DICTIONARIES AS ELEMENTS

# ALL THE FUNCTIONS ARE BELOW:-

def average(numbers):                  #FUNCTION  THAT ACCEPT THE ARRAY NUMBERS
    total=sum(numbers)
    total=float(total)
    result=total/len(numbers)
    return result                      #RETURNING AVERAGE OF ELEMENTS

def get_average(student):              #FUNTION ACCEPT A SINGLE STUDENT DICTIONARY
    homework=sum(student["homework"])/len(student["homework"])
    quizzes=sum(student["quizzes"])/len(student["quizzes"])
    tests=sum(student["tests"])/len(student["tests"])
    return .1*homework+.3*quizzes+.6*tests  #RETURN THE SUM OF WEIGHTED AVERAGES OF KEYS

def get_letter_grade(score):               #ACCEPT THE SCORE OF STUDENT AND RETURN GRADE ACHEIVED BY THEM
        if score>=90:
            return "A"
        elif score>=80:
            return "B"
        elif score>=70:
            return "C"
        elif score>=60:
            return "D"
        else:
            return "F"
def class_average(students):   #FUNCTION ACEEPT ALL STUDENT ARRAY
    results = []
    for student in students:
        r = get_average(student)
        results.append(r)
    return average(results)    #RETURN THE AVERAGE OF ALL STUDENT SCORES


print (class_average(students),get_letter_grade(class_average(students))) # PRINTS THE CLASS AVERAGE OF ALL STUDENTS AND GRADE FOR THE CLASS'S AVERAGE