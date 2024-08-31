
def reverse_string(stack, input_string):

    #Looping through the string
    for i in range(len(input_string)):
        stack.push(input_string[i])

        reverse_string = ""

        while not stack.is_empty():
            reverse_string += stack.pop()

            return reverse_string
        
    stack = stack()
    input_string = "Hello"

    print(str)
    print(reverse_string(stack, input_string))
