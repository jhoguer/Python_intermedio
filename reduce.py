from functools import reduce

def flatonacci(signature: list, n: int) -> list:
    if any(filter(lambda x: type(x) != int, signature)) or len(signature) != 3:
        raise Exception("Signature no valid")
    elif n < 0:
        raise Exception("'n' cannot be negative")

    result = signature

    while len(result) < n:
        result.append(sum(result[-3:]))

    return result[:n]



def run():
    my_lis = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_lis)
    print(all_multiplied)

    list = [1, 1, 1]

    res = flatonacci(list, 8)
    print(res)


if __name__ == '__main__':
    run()
