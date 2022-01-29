from random import randint
num = str(randint(100000000, 999999999))

new_cpf = num
reverse = 10
total = 0

# Loop
for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)

        if digit > 9:
            digit = 0
        total = 0
        new_cpf += str(digit)
        
print (new_cpf)