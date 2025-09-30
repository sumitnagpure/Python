# add_num = lambda x,y : x * y
#
# print(add_num(5,2))
#
# students = [["Alice", 88], ["Bob", 95], ["Sid", 58]]
#
# sorted_by_grade = sorted(students, key = lambda x:x[1])
# print(sorted_by_grade)
#
# students.sort(key = lambda x:x[0])
# print(students)
#
# sorted_by_name = sorted(students, key = lambda x:x[0])
# print(sorted_by_name)


books = [['Python',500],['Java',750],['AI/ML',1000],['Data analytics',1500],['Statistics in ML',350]]

books.sort(reverse=True)
print(books)

soretd_books1 = sorted(books, key = lambda x:x[1],reverse = True)
print(soretd_books1)

books.sort(key = lambda item:item[1])
print(books)

filtered_books = list(filter(lambda x: x[1] > 700, books))
print(filtered_books)