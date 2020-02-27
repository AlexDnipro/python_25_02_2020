#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
#Is the string uppercase?
def is_uppercase(inp):
    return inp.isupper()

#https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python
#Sort My Textbooks
def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)

#https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e
#Remove the time
def shorten_to_date(long_date):
    return long_date.split(",")[0]