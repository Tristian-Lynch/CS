# Tristian Lynch

from random import randint


def main():
    print("MCSS Module 6")

    # Create a list of numbers
    numbers = [randint(-100, 100) for i in range(100)]
    print(numbers)

    print(brute_force(numbers))
    print(efficient_method(numbers))


def brute_force(numbers):
    max_sum = 0
    max_sub = []

    # Print each possible substring
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sum = add_numbers(numbers[i : j + 1])

            if sum > max_sum:
                max_sum = sum
                max_sub = numbers[i : j + 1]

    return max_sum, max_sub


def efficient_method(numbers):
    


def add_numbers(numbers):
    sum = 0

    for number in numbers:
        sum += number

    return sum


if __name__ == "__main__":
    main()
