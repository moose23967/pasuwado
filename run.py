from qsharp import eval

with open("src/Main.qs") as main:
    eval(main.read())

    print(eval("GeneratePassword(5)"))
