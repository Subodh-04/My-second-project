while(True):
    work = input("Square or Cube of a number:")

    if work=="Square":
            number = int(input("Enter a number----->"))
            square = number*number
            print(square)
            continue

    if work=="Cube":
            number = int(input("Enter a number----->"))
            cube = number*number*number
            print(cube)
            continue
