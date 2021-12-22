

def multiply(number1, number2):
    """
    A function to multiply two large numbers.
    
    number1: input number can be int or string
    
    number2: input number can be int or string

    """
    if isinstance(number1, int):
        number1 = str(number1)
    if isinstance(number2, int):
        number2 = str(number2)
    len1 = len(number1)
    len2 = len(number2)
    if len1 == 0 or len2 == 0:
        return "0"

    result = [0] * (len1 + len2)
    i_n1 , i_n2 = 0, 0

    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = ord(number1[i]) - 48
        i_n2 = 0

        for j in range(len2 - 1, -1, -1):

            n2 = ord(number2[j]) - 48
            summ = n1 * n2 + result[i_n1 + i_n2] + carry
            carry = summ // 10
            result[i_n1 + i_n2] = summ % 10

            i_n2 += 1
        if (carry > 0):
            result[i_n1 + i_n2] += carry
        i_n1 += 1

    i = len(result) - 1
    while (i >= 0 and result[i] == 0):
        i -= 1

    if (i == -1):
        return "0"

    s = ""
    while (i >= 0):
        s += chr(result[i] + 48)
        i -= 1

    return s

str1 = "54"
str2 = "23"

if((str1[0] == '-' or str2[0] == '-') and
   (str1[0] != '-' or str2[0] != '-')):
    print("-", end= '')

if(str1[0] == '-' and str2[0] != '-'):
    str1 = str1[1:]
elif(str1[0] != '-' and str2[0] == '-'):
    str2 = str2[1:]
elif(str1[0] == '-' and str2[0] == '-'):
    str1 = str1[1:]
    str2 = str2[1:]
print(multiply(str1, str2))
