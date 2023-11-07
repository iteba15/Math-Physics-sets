
from matplotlib import pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main(limit):
    input_numbers = list(range(1, limit + 1))
    filename = input("Enter file name: ")
    steps_to_reach_one = [collatz_steps(n) for n in input_numbers]

    plt.scatter(input_numbers, steps_to_reach_one, s=5)
    plt.xlabel("Initial Integer")
    plt.ylabel("Steps to Reach 1")
    plt.title(f"Collatz Conjecture Analysis (Up to {limit})")
    # Replace plt.show() with saving the plot to a file
    plt.savefig(filename)


if __name__ == "__main__":
    limit = int(input("Enter the upper limit for initial integers: "))
    main(limit)
