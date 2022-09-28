# python_homework1
homework of python
def check_parentheses_right(str):
    temp = []
    flag = True
    for i in str:
        if i!="(" and i!="[" and i!="]" and i!=")":
            continue
        if i == "[" or i == "(":
            temp.append(i)
        elif i == "]":
            if len(temp) == 0 or temp.pop() != "[":
               return False
        elif i == ")":
            if len(temp) == 0 or temp.pop() != "(":
               return False
    if  len(temp)!=0:
        flag = False
    return flag


a = "{[{()}]()}"
print(check_parentheses_right(a))
b = "({[{()}]()}"
print(check_parentheses_right(b))
c = "{[{()}]()}]"
print(check_parentheses_right(c))
d = "(hello)"
print(check_parentheses_right(d))
e = "(22+3)*(21/[34+1)]"
print(check_parentheses_right(e))
