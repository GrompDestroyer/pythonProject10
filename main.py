def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]
    return (bubble_sort(list))


list = [3, 7, 5, 1]
print(bubble_sort)
