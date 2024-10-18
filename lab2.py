a=[]
str1=a.split('')
int=[]
for string_num in str1:
    int.append(int(string_num))
    b=[]
for num in int:
    if num>100:
        b.append("over")
    else:
            b.append(str(num))
            for i in range (len(b)):
                if i==len(b)-1:
                    print(b[i],end="")
                else:
                    print(b[i],end="")
            
