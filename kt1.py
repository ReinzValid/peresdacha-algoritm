"""Поиск: функции возвращают индекс; счётчик доступен в .comparisons."""
def linear_search(arr, x):
    linear_search.comparisons = 0
    for i, value in enumerate(arr):
        linear_search.comparisons += 1  # сравнение value == x
        if value == x:
            return i
    return -1


def binary_search(arr, x):
    binary_search.comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        binary_search.comparisons += 1  # сравнение arr[mid] == x
        if arr[mid] == x:
            return mid
        binary_search.comparisons += 1  # сравнение arr[mid] < x
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    arr = [3, 7, 12, 19, 25, 31, 44, 56, 68, 79]
    for x in (31, 50):
        for search in (linear_search, binary_search):
            index = search(arr, x)
            print(f'x={x}, {search.__name__}: индекс={index}, '
                  f'сравнения={search.comparisons}')
    print('Двоичный поиск сделал меньше сравнений в обоих случаях.')
    print('Линейный: O(n); двоичный: O(log n), только для отсортированного массива.')
