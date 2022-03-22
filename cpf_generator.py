from random import randint

def menu():
        print("""

            Menu:

            [F] - CPF Formatted.
            [W] - CPF without formatting.
            [E] - Exit.

        """)
        return str(input('Choose an option: '))    

format_cpf = 'f'
cpf_without_f = 'w'
exitm = 'e'

alternativies_menu = menu()

num = str(randint(100000000, 999999999))

ncpf = num
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(ncpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)

        if digit > 9:
            digit = 0
            
        total = 0
        ncpf += str(digit)

if alternativies_menu == 'w':
    print(ncpf)

if alternativies_menu == 'f':
        ncpf = str(ncpf) 
        print('{0}.{1}.{2}-{3}'.format(ncpf[0:3], ncpf[3:6], ncpf[6:9], ncpf[9:11]))

if alternativies_menu == 'e':
    exit()