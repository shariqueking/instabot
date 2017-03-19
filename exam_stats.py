grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print(grade)      # print all grade in grades list


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade       # totalling all the grade of grades list
    return total        # returns total of grade


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))   #doing the average of all grade
    return average                   # return the average of all grade score


def grades_variance(scores):     # function to find vaiance
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2

    return variance / float(len(scores))    # return variance of grade score

variance = grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

print(grades_variance(grades))
print(grades_std_deviation(variance))


