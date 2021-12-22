""" 1st way to implement Stack using builtin List data structure """

stack = []

# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(10)

#print(stack)


def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)


def pop_element():
    if not stack:
        print("The stack is empty ! ")
    else:
        e = stack.pop()
        print(f"remove element {e}")
        print(stack)


# it will prompt until the condition is false
while True:
    print("Select the operation 1.push 2.pop 3.quit")
    try:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            push()
        elif choice == 2:
            pop_element()
        elif choice == 3:
            break
        else:
            print("Enter the correct operation please !")
    except ValueError:
        print("Please Enter the number")



