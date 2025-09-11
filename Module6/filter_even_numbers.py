

def filter_even_numbers(numbers):
    list_with_even_numbers_only = []
    for n in numbers:
        if n % 2 == 0:
            list_with_even_numbers_only.append(n)
    return list_with_even_numbers_only


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(original_list)

print("Original list: ", original_list)
print("Even numbers only: ", evens)
