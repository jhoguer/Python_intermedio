def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

    # divisors1 = [i for i in range(1, num + 1) if num % i == 0]

    # return divisors1


def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise Exception("Numero negativo")
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un numero")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
