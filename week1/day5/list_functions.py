# def biggest_number(num):
#     biggest_num = 0
#     for n in num:
#         if biggest_num < n:
#             biggest_num = n
#     return biggest_num

# print(biggest_number([3, 7, 2, 9, 5]))

# ##Using max()
# def biggest_number(num):
#     biggest_num = max(num)
#     return biggest_num

# print(biggest_number([3, 7, 2, 9, 5]))


## Some error handling


def biggest_number(num):
    if len(num) == 0:
        return 'Empty list'
    return max(num)

print(biggest_number([]))
