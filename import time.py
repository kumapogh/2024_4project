import time
import random
import csv

# データファイル作成関数
def create_data_file(filename, num_digits, num_elements):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_elements):
            writer.writerow([random.randint(10**(num_digits-1), 10**num_digits - 1)])

# ソートアルゴリズムの実装

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return comparisons, swaps

def quicksort(arr):
    comparisons = 0
    swaps = 0

    def _quicksort(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi, comp, swp = partition(arr, low, high)
            comparisons += comp
            swaps += swp
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    def partition(arr, low, high):
        comparisons = 0
        swaps = 0
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1, comparisons, swaps

    _quicksort(arr, 0, len(arr) - 1)
    return comparisons, swaps

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return comparisons, swaps

def merge_sort(arr):
    comparisons = 0
    swaps = 0

    def _merge_sort(arr):
        nonlocal comparisons, swaps
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            _merge_sort(L)
            _merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                comparisons += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                swaps += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                swaps += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                swaps += 1

    _merge_sort(arr)
    return comparisons, swaps

# ソートアルゴリズムのテストと計測
def test_sorting_algorithm(algorithm, data):
    start_time = time.time()
    comparisons, swaps = algorithm(data.copy())
    end_time = time.time()
    return comparisons, swaps, end_time - start_time

# メイン関数
def main():
    # データファイルの作成
    create_data_file('data_3_digits.csv', 3, 1000)
    create_data_file('data_4_digits.csv', 4, 10000)
    create_data_file('data_5_digits.csv', 5, 100000)

    # データの読み込み
    def load_data(filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            return [int(row[0]) for row in reader]

    data_files = ['data_3_digits.csv', 'data_4_digits.csv', 'data_5_digits.csv']
    algorithms = {
        "Selection Sort": selection_sort,
        "Quick Sort": quicksort,
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort
    }

    results = []

    for data_file in data_files:
        data = load_data(data_file)
        for name, algorithm in algorithms.items():
            comparisons, swaps, duration = test_sorting_algorithm(algorithm, data)
            results.append({
                "Data File": data_file,
                "Algorithm": name,
                "Comparisons": comparisons,
                "Swaps": swaps,
                "Duration": duration
            })

    # 結果を表示
    for result in results:
        print(result)

if __name__ == "__main__":
    main()