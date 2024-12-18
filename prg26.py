def process(input_str):
    vowels='aeiouAEIOU'
    str=' '
    count=0
    for char in input_str:
        if char.lower() in vowels:
            str+=char.upper()
            count+=1
        else:
            str+=char
    return len(input_str),str,count
input_str=input("enter a string")
size,str,count=process(input_str)
print(f"input string:{input_str}")
print(f"processed string{str}")
print(f"size of string{size}")
print(f"number of vowels{count}")
