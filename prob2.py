def stringBreakdown(str, dictArr):
    res = None
    for x in dictArr:
       index = str.find(x)
       if index != -1 or res != False:
           res=True
       else:
           res=False
    return res

str_input = "applecomputer"
dict_arr = ["apple", "computer"]
result = stringBreakdown(str_input, dict_arr)
print(result)
str_input = "python"
dict_arr = ["java", "javascript", "ruby"]
result = stringBreakdown(str_input, dict_arr)
print(result)
# Expected output: False

