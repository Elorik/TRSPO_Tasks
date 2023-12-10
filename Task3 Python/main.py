import concurrent.futures
import itertools


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def compute_average_steps(start, end, num_threads):
    numbers = itertools.islice(itertools.count(start), 0, end - start + 1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        steps = list(executor.map(collatz_steps, numbers))

    total_steps = sum(steps)
    average_steps = total_steps / (end - start + 1)

    return average_steps


if __name__ == "__main__":
    N = 200  # Замініть N на бажане число
    num_threads = 10  # Замініть на бажану кількість потоків

    average_steps = compute_average_steps(1, N, num_threads)

    print(f"Середня кількість кроків для чисел від 1 до {N}: {average_steps}")
