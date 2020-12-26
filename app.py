import random
name = input("Enter your name:")
print("Hello,",name)
txt = input()
if len(txt)== 0 or len(txt.split(",")) == 1:
    options = ["rock","paper","scissors"]
else:
    options = txt.split(",")
print("Okay, let's start")
while True:
    f = open("rating.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.split("\n")[0].split()
        if line[0] == name:
            rating = int(line[1])
    if rating is None:
        rating = 0
    f.close()
    f = open("rating.txt", "w")
    option = input()
    if option in options:
        choosen = options[int(random.random() * len(options))]
        L = options[options.index(option) + 1:] + options[:options.index(option)]
        if choosen == option:
            print(f"There is a draw {option}")
            rating += 50
        elif choosen in L[:int(len(L)/2)]:
            print(f"Sorry, but the computer chose {choosen}")
        elif choosen in L[int(len(L)/2):]:
            print(f"Well done. The computer chose {choosen} and failed")
            rating += 100
    elif option == "!rating":
        print(f"Your rating: {rating}")
    elif option == "!exit":
        print("Bye!")
        for x in lines:
            if x.split("\n")[0].split()[0] == name:
                print(f"{name} {rating}\n",file=f, flush=True)
            print(x,file=f,flush=True)
        f.close()
        break
    else:
        print("Invalid input")
