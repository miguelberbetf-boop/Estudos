while True:
    t = int(input(": "))
    print('-'*32)
    if t < 0:
        print('é negativo')
        break
    else:
        for i in range(1, 10+1):
            print(f'{t} X {i} = {t*i}')
            if i == 10:
                print('-'*32)
                break