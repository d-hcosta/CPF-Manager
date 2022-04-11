while True:
    cpf = input('Enter a CPF:')
    format_cpf = cpf.replace(".", "").replace("-", "")
    new_cpf = format_cpf[:-2]
    reverse = 10
    total = 0

    try:
        if len(format_cpf) != 11:
            print('11 digits are required.')
            continue
        if not new_cpf.isnumeric():
            print('You need enter a number.')
            continue
    except Exception as e:
        print ('11 digits are required.')

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
    
    sequence = new_cpf == str(new_cpf[0]) * len(format_cpf)

    if format_cpf == new_cpf and not sequence:
        print('Valid.')
    else:
        print('Invalid.')
    exit()
