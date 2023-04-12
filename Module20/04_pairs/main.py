original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def first_solution(data):
  result_dict = dict()
  for i_index, i_value in enumerate(original_list):
    if i_index % 2 == 0:
      result_dict[i_index] = i_value
  result = [(i_key, i_value + 1) for i_key, i_value in result_dict.items()]
  return result

print(f"Оригинальный список: {original_list}")
print(f"Новый список: {first_solution(original_list)}")
