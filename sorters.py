class Sorters:
    def bubble_sort(self, arr):
        for a in range(len(arr) - 1, 0, -1):
            for b in range(a):
                if arr[b] > arr[b + 1]:
                    arr[b], arr[b + 1] = arr[b + 1], arr[b] 
    
    def selection_sort(self, arr):
        for i in range(len(arr)):
            index_min = i
            for a in range(i + 1, len(arr)):
                if arr[a] < arr[index_min]:
                    index_min = a

            (arr[i],arr[index_min]) = (arr[index_min],arr[i])

    def insertion_sort(self, arr):
        a = len(arr)

        if a <= 1:
            return

        for b in range(1, a):
            key = arr[b]
            c = b - 1
            while c >= 0 and key < arr[c]:
                arr[c + 1] = arr[c]
                c -=1
            arr[c + 1] = key


example = Sorters()
arr = [11,23,55,45,22]
print(arr)

example.insertion_sort(arr)
print(arr)


