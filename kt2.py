"""Каждая сортировка возвращает новый массив и число сравнений элементов."""
from timeit import repeat


def bubble_sort(data):
    a, comparisons = data.copy(), 0
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(end):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, comparisons


def shell_sort(data):
    a, comparisons = data.copy(), 0
    gap = len(a) // 2
    while gap:
        for i in range(gap, len(a)):
            value, j = a[i], i
            while j >= gap:
                comparisons += 1
                if a[j - gap] <= value:
                    break
                a[j] = a[j - gap]
                j -= gap
            a[j] = value
        gap //= 2
    return a, comparisons


def quick_sort(data):
    a, comparisons = data.copy(), 0

    def sort(left, right):
        nonlocal comparisons
        if left >= right:
            return
        pivot, i = a[right], left
        for j in range(left, right):
            comparisons += 1
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[right] = a[right], a[i]
        sort(left, i - 1)
        sort(i + 1, right)

    sort(0, len(a) - 1)
    return a, comparisons


if __name__ == '__main__':
    data = [5, 2, 9, 1, 5, 6, 3, 8, 4, 7]
    timings = []
    for function in (bubble_sort, shell_sort, quick_sort):
        result, comparisons = function(data)
        # Минимум из пяти серий; каждая содержит 10 000 вызовов.
        elapsed = min(repeat(lambda: function(data), number=10000, repeat=5)) / 10000
        timings.append((elapsed, function.__name__))
        print(f'{function.__name__}: {result}, сравнений={comparisons}, '
              f'время={elapsed * 1e6:.3f} мкс/вызов')
    print('Быстрее в этом запуске:', min(timings)[1])
    print('Для 10 элементов результат зависит от среды и накладных расходов Python.')
