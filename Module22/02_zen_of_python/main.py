with open('zen.txt', 'r') as f:
    print(*f.readlines()[::-1])
