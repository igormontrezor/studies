def students_grades(quantity):
    students = dict()
    grades_list = list()

    for q in range(quantity):
        name = input('Enter with name: ').title()
        for g in range(1,4):
            grades = float(input(f'Enter with {g}° grade of {name}: '))
            grades_list.append(grades)
            students[name] = grades_list.copy()
        grades_list.clear()
    return students


def average(students, quantity):
    sum_avarege = 0
    average_class_count = 0
    for indx, g in enumerate(students.values()):
        for n in g:
            sum_avarege += n
        average = (sum_avarege/len(g))
        average_class_count += average
        g.append(float('%.2f' % average))
        sum_avarege = 0
    average_class_count = float('%.2f' % (average_class_count/quantity))
    students['average_class'] = [average_class_count]
    return students


def bigger_small_grades(students):
    bigger_small = list()
    bigger = max(students, key=lambda k: students[k][-1])
    bigger_value = students[bigger][-1]
    small = min(students, key=lambda k: students[k][-1])
    small_value = students[small][-1]
    bigger_small += [bigger, bigger_value, small, small_value]
    return bigger_small
    

def situation(students):
    for grade in students.items():
        if list(grade)[0] == 'average_class':
            break
        elif list(grade)[1][-1] > 7:
            list(grade)[1].append('passed')
        else:
            list(grade)[1].append('not passed')
    return students

def  print_data(quantity):
    students = students_grades(quantity)
    average_students_class = average(students, quantity)
    bigger_small = bigger_small_grades(students)
    situation_at = situation(students)
    print(f'Total: {quantity}')
    print(f'The Bigger Average is {bigger_small[0]}: {bigger_small[1]}\nThe Smaller Average is {bigger_small[2]}: {bigger_small[3]}')
    print(f'The Average Classe: {average_students_class['average_class']}')
    
    name = 'in'
    while name != 'Out':
        name = input('Enter with name (Out): ').title()
        if name in situation_at.keys():
            print(f'{name}: {situation_at[name][-1]}')
        elif name == 'Out':
            break
        else:
            print(f'{name} not is in database.')
        
quantity = (int(input('Enter quantity of students: ')))
print_data(quantity)