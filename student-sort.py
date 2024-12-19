import random

# 학생 정보 생성 함수
def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬
def selection_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if data[j][key] < data[least][key]:
                least = j
        data[i], data[least] = data[least], data[i]

# 삽입 정렬
def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j][key] > current[key]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

# 개선된 퀵 정렬
def quick_sort(A, left, right, key):
    if left < right:
        pivot = median_of_three(A, left, right, key)
        q = partition(A, left, right, pivot, key)
        quick_sort(A, left, q - 1, key)
        quick_sort(A, q + 1, right, key)

def median_of_three(A, left, right, key):
    mid = (left + right) // 2
    if A[left][key] > A[mid][key]:
        A[left], A[mid] = A[mid], A[left]
    if A[left][key] > A[right][key]:
        A[left], A[right] = A[right], A[left]
    if A[mid][key] > A[right][key]:
        A[mid], A[right] = A[right], A[mid]
    A[left], A[mid] = A[mid], A[left]
    return A[left][key]

def partition(A, left, right, pivot, key):
    low = left + 1
    high = right
    while True:
        while low <= high and A[low][key] <= pivot:
            low += 1
        while low <= high and A[high][key] > pivot:
            high -= 1
        if low > high:
            break
        A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high

# 원형 큐 클래스와 기수 정렬
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            raise OverflowError("Queue is full.")

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None
            return item
        else:
            raise IndexError("Queue is empty.")

def radix_sort(A, key):
    BUCKETS = 10
    max_val = max(A, key=lambda x: x[key])[key]
    DIGITS = len(str(max_val))
    factor = 1
    for _ in range(DIGITS):
        queues_list = [ArrayQueue(len(A)) for _ in range(BUCKETS)]
        for item in A:
            digit = (item[key] // factor) % BUCKETS
            queues_list[digit].enqueue(item)
        i = 0
        for queue in queues_list:
            while not queue.is_empty():
                A[i] = queue.dequeue()
                i += 1
        factor *= BUCKETS

# 메뉴 기반 실행
def main():
    students = generate_students()
    print("생성된 학생 목록:")
    for student in students:
        print(student)

    while True:
        print("\n메뉴:")
        print("1. 이름 기준 정렬")
        print("2. 나이 기준 정렬")
        print("3. 성적 기준 정렬")
        print("4. 프로그램 종료")
        field_choice = input("정렬 기준을 선택하세요 (1-4): ")

        if field_choice == "4":
            print("프로그램을 종료합니다.")
            break

        field = None
        if field_choice == "1":
            field = "이름"
        elif field_choice == "2":
            field = "나이"
        elif field_choice == "3":
            field = "성적"
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        print("\n정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if field == "성적":
            print("4. 기수 정렬 (성적 전용)")
        algorithm_choice = input("정렬 알고리즘을 선택하세요 (1-4): ")

        print("\n정렬 전 데이터:")
        for student in students:
            print(student)

        if algorithm_choice == "1":
            selection_sort(students, field)
        elif algorithm_choice == "2":
            insertion_sort(students, field)
        elif algorithm_choice == "3":
            quick_sort(students, 0, len(students) - 1, field)
        elif algorithm_choice == "4" and field == "성적":
            radix_sort(students, field)
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        print("\n정렬 후 데이터:")
        for student in students:
            print(student)

# 프로그램 실행
if __name__ == "__main__":
    main()
