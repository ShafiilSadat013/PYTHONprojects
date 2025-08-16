import art
def add(n1, n2):
    return n1 + n2

def subt(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

ops = {
    "+" : add,
    "-" : subt,
    "*" : mult,
    "/" : div,
}
#print(ops["*"](4,8))
def calculator():
    print(art.logo)
    calculate = True
    n1 = float(input("first number ?: "))
    while calculate:
        for symbol in ops:
            print(symbol)

        ops_symbol = input("Which Ops ?: ")
        n2 = float(input("second number ?: "))
        ans = ops[ops_symbol](n1,n2)
        print(f"{n1} {ops_symbol} {n2} =  {ans} ")
        choice = input(f"'y' to continue with {ans} or type 'n' to start a new calculation  ")
        if choice == "y":
            n1 = ans
        else:
            calculate = False
            print("\n"* 20)
            calculator()  #recursion


calculator()
