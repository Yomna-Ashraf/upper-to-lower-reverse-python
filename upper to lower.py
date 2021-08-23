x = "yoMNa IS BeauTIfUL"
str1 = ""
x=x.split(" ")
x.reverse()
print(x)
for a in x:
    for i in a:
        if i.isupper():
            i=i.lower()
            str1 = str1+i
        elif i.islower():
            i=i.upper()
            str1 = str1 + i
    str1 = str1+" "            
print(str1)    




def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    str1 = ""
    list1 = sentence.split(" ")
    for a in list1:
        for i in a:
            if i.isupper():
                i = i.lower()
                str1=str1+i
            elif i.islower():
                i = i.upper()
                str1 = str1 + i
        str1 = str1 + " "  
    return str1              

