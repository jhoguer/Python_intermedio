def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Jhon", "Miguel", "Pepe", "Christian", "Lina"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
      for name in names:
        print("Writing...." + name)
        f.write(name + ";" + name + ";" + name + ";" + name + ";" + name + ";" + name + ";" + name)
        f.write("\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()
