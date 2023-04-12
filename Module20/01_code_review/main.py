students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)


def get_interests_and_surnames_length(data):
    interests = set()
    surnames_length = 0
    for student_data in data.values():
        interests.update(student_data['interests'])
        surnames_length += len(student_data['surname'])
    return interests, surnames_length


def get_student_id_and_age(data):
    return [(k, v['age']) for k, v in data.items()]


pairs = get_student_id_and_age(students)
interests, surnames_length = get_interests_and_surnames_length(students)

print("Список пар \"ID студента — возраст\":", pairs)
print("Полный список интересов всех студентов:", interests)
print("Общая длина всех фамилий студентов:", surnames_length)
