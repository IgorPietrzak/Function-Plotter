import numpy as np
import matplotlib.pyplot as plt
def bounds():
    xaxis_lower_bound = float(input("Enter a lower bound for the domain of f(x): "))
    xaxis_upper_bound = float(input("Enter an uppper bound for the domain of f(x): "))
    if xaxis_lower_bound > xaxis_upper_bound:
                              print("Lower bound cannot be greater than upper bound, try again")
                              bounds()
def polynomial():
    sca = int(input("Your function is:\n" + "f(x) = ax^n + b, where a = "))
    exp = int(input("Your function is:\n" +"f(x) = " + str(sca) + "x^n + b, where n = "))
    const = int(input("Your function is:\n" +"f(x) = "+ str(sca) + "x^" + str(exp) + " +b, where b = "))
    xaxis_lower_bound = float(input("Enter a lower bound for the domain of f(x): "))
    xaxis_upper_bound = float(input("Enter an uppper bound for the domain of f(x): "))
    xaxis = np.linspace(xaxis_lower_bound,xaxis_upper_bound,100)
    polyaxis = []
    for i in xaxis:
        i = (sca)*i
        i = i**(exp)
        i = i + (const)
        polyaxis.append(i)

    plt.plot(xaxis, polyaxis)
    plt.title("Your function is: f(x)= " + str(sca) + "x^" + str(exp) + " + " + str(const) + "In the interval ["
              + str(xaxis_lower_bound) + "," + str(xaxis_upper_bound) + "]")
    plt.grid()
    plt.show()
    choice()

def sin():
    a = int(input("Your function is f(x) = asin(x) + b, where a = "))
    b = int(input("Your function is f(x) = " + str(a) + "sin(x) + b, where b = "))
    xaxis_lower_bound = float(input("Enter a lower bound for the domain of f(x): "))
    xaxis_upper_bound = float(input("Enter an uppper bound for the domain of f(x): "))
    
    xaxis = np.linspace(xaxis_lower_bound,xaxis_upper_bound,100)
    sin_yaxis = []

    for i in xaxis:
        i = (a)*(np.sin(i))+(b)
        sin_yaxis.append(i)

    plt.plot(xaxis, sin_yaxis)
    plt.title("Your function is f(x) = " + str(a) + "sin(x) + "+ str(b) +" In the interval ["
              + str(xaxis_lower_bound) + "," + str(xaxis_upper_bound) + "]")
    plt.grid()
    plt.show()
    choice()

def cos():
    a = int(input("Your function is f(x) = acos(x) + b, where a = "))
    b = int(input("Your function is f(x) = " + str(a) + "cos(x) + b, where b = "))
    xaxis_lower_bound = float(input("Enter a lower bound for the domain of f(x): "))
    xaxis_upper_bound = float(input("Enter an uppper bound for the domain of f(x): "))
    xaxis = np.linspace(xaxis_lower_bound,xaxis_upper_bound,100)
    cos_yaxis = []

    for i in xaxis:
        i = (a)*(np.cos(i))+(b)
        cos_yaxis.append(i)

    plt.plot(xaxis, cos_yaxis)
    plt.title("Your function is f(x) = " + str(a) + "cos(x) + "+ str(b)+" In the interval ["
              + str(xaxis_lower_bound) + "," + str(xaxis_upper_bound) + "]")
    plt.grid()
    plt.show()
    choice()

def e():
    a = int(input("Your function is f(x) = (a)e^bx, where a = "))
    b = int(input("Your function is f(x) = "+ str(a)+"e^bx, where b = "))
    xaxis_lower_bound = float(input("Enter a lower bound for the domain of f(x): "))
    xaxis_upper_bound = float(input("Enter an uppper bound for the domain of f(x): "))
    xaxis = np.linspace(xaxis_lower_bound,xaxis_upper_bound,100)
    e_yaxis = []

    for i in xaxis:
        i = (a)*(np.e)**((b)*(i))
        e_yaxis.append(i)

    plt.plot(xaxis, e_yaxis)
    plt.title("Your function is f(x) = " + str(a) + "e^" + str(b) + "x"+" In the interval ["
              + str(xaxis_lower_bound) + "," + str(xaxis_upper_bound) + "]")
    plt.grid()
    plt.show()
    choice()

def choice():
    ch = str(input("Pick a type of function you would like to plot\n"
                   + " (1) f(x) = ax^n + b\n" + "(2) f(x) = asin(x) +b\n"
                   + "(3) f(x) = acos(x) +b\n" + "(4) f(x) = (a)e^bx\n" + "Choose 1-4 or 'q' to quit: "))

    if ch == "1":
        polynomial()
    elif ch == "2":
        sin()
    elif ch == "3":
        cos()
    elif ch == "4":
        e()
    elif ch == "q":
        exit()
    else:
        print("Invalid input")
        choice()

choice()






    



    

    
