"""

"""
def collatz(n):
    sequence = [n] #Create a list to store the Collatz sequence with the initial value.
    while n != 1: # Continue the loop until n reaches 1, as per the Collatz Conjecture.
        if n % 2 == 0:
            n = n // 2 #if n is even divide it by 2
        else:
            n = 3 * n + 1 #if is odd multiply it by 3 then add 1
        sequence.append(n)# Add the new value of n to the sequence list.
    return sequence # Return the complete Collatz sequence as a list.

#enter your initial number here
initial_number = int(input("Enter positive integer: "))

if initial_number <= 0:
    print("please enter a positive integer.")
else:
    collatz_sequence = collatz(initial_number)# Call the collatz function with the input.
    print("Collatz Sequence:")
    for number in collatz_sequence:# Loop through the Collatz sequence list.
        print(number) # Print each value in the sequence.
