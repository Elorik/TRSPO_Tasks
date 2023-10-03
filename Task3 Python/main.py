import multiprocessing
import threading


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
    numbers = list(range(start, end + 1))
    results = []

    def worker():
        while True:
            try:
                number = numbers.pop()
            except IndexError:
                break
            steps = collatz_steps(number)
            results.append(steps)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_steps = sum(results)
    average_steps = total_steps / (end - start + 1)

    return average_steps


if __name__ == "__main__":
    N = 100  # Замініть N на бажане число
    num_threads = 5  # Замініть на бажану кількість потоків

    average_steps = compute_average_steps(1, N, num_threads)

    print(f"Середня кількість кроків для чисел від 1 до {N}: {average_steps}")
