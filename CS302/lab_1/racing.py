import timeit
import matplotlib.pyplot as plt
from mcss import brute_force_mcss, \
    better_brute_force_mcss, linear_mcss, \
    get_random_list

# Measure execution time of each function
def measure_time(func, arg, repetitions=3):
    return timeit.timeit(lambda: func(arg), number=repetitions)


if __name__ == '__main__':
    # List of functions and labels
    functions = [brute_force_mcss, better_brute_force_mcss, linear_mcss]
    labels = ['Cubic', 'Quadratic', 'Linear']
    fn_names = ['Brute Force', 'Better Brute Force', 'Linear']

    # List of different arguments to pass to the functions
    lengths = range(50, 850, 50)
    args = [get_random_list(k) for k in lengths]

    # Measure execution times for each argument and each function
    results = {label: [] for label in labels}

    for func, label, name in zip(functions, labels, fn_names):
        print("+-------------------------------------------------+")
        for arg in args:
            print(f"Running {name} for length: {len(arg)}")
            time_taken = measure_time(func, arg)
            results[label].append(time_taken)
        print("+-------------------------------------------------+")

    # get the figure for side by side plots
    _, (ax1, ax2, slax) = plt.subplots(1, 3, figsize=(18, 6))

    # Plot the results
    for label in labels:
        ax1.plot(lengths, results[label], label=label)
    ax1.set_xlabel('Sequence length (n)')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('MCSS Execution for Different Approaches')
    ax1.legend()

    for label in labels[1:]:
        ax2.plot(lengths, results[label], label=label)
    ax2.set_xlabel('Sequence length (n)')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('MCSS Execution for Linear and Quadratic Approaches')
    ax2.legend()

    for label in labels:
        slax.semilogy(lengths, results[label], label=label)
    slax.set_xlabel('Sequence length (n)')
    slax.set_ylabel('Time (seconds)')
    slax.set_title('Semi-Log MCSS Execution for Different Approaches')
    slax.legend()

    plt.tight_layout()
    plt.show()

