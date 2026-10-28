from tkinter import *


def calculate(op):
    try:
        a = float(num1.get())
        b = float(num2.get())

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                answer.config(text="error")
                return
            result = a / b

        answer.config(text="result: " + str(result))

    except ValueError:
        answer.config(text="please enter numbers")


root = Tk()
root.title("Calculator")
root.geometry("300x300")

Label(root, text="calculator").pack(pady=10)

Label(root, text="number1").pack()
num1 = Entry(root)
num1.pack()

Label(root, text="number2").pack()
num2 = Entry(root)
num2.pack()

Button(root, text="+", width=15,
       command=lambda: calculate("+")).pack()

Button(root, text="-", width=15,
       command=lambda: calculate("-")).pack()

Button(root, text="*", width=15,
       command=lambda: calculate("*")).pack()

Button(root, text="/", width=15,
       command=lambda: calculate("/")).pack()

answer = Label(root, text="result:")
answer.pack(pady=10)

Button(root, text="exit", command=root.destroy).pack()

root.mainloop()
