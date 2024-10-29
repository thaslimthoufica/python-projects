
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    def run():
        operation=input("choose the operation:")
        n2=int(input("Enter the next number:"))
        output=dict[operation](n1,n2)
        print(f"{n1}{operation}{n2}={output}")
        return output
    n1=int(input("enter your first number:"))
    print("+\n-\n*\n/\n")
    output=run()
    running=True
    while running:
        another=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation:")
        if another=="y":
            n1=output
            output=run()
        elif another=='n':
            print(f"your result is {output}")
            running=False
            print("\n" * 20)
            calculator()


calculator()
