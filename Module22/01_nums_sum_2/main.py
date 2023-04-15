with open('numbers.txt', 'r') as input_file:
  numbers = [int(num) for line in input_file for num in line.split()]
  total_sum = sum(numbers)

# Открытие выходного файла и запись результата
with open('answer.txt', 'w') as output_file:
  output_file.write(str(total_sum))

print('Содержимое файла numbers.txt', numbers)
print('Содержимое файла answer.txt', total_sum)