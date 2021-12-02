# # day 2 solution from u/4HbQ - repeating to learn
# # only works in Python 3.10
#
# with open("input") as file:
#     lines = [str(line.rstrip()).split(" ") for line in file.readlines()]
#
# h, d, a = 0, 0, 0
#
# for x in lines:
#     match x.split():
#         case 'forward', n:
#             h += int(n)
#             d += int(n)*a
#         case 'up', n:
#             a -= int(n)
#         case 'down', n:
#             a += int(n)
#
# print(f"A: {h*a} B: {h*d}")