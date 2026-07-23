rows=int(input("enter tha number:"))
for i in range(1,rows + 1):
    print(""*(rows - i),end ="")
    print("* "*i)


start = int(input(" start : "))
end = int(input(" end : "))
total_sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        print(f"Number {num} is Even") 
        total_sum+=num
    else:
        print(f"Number {num} is Odd")
        total_sum += num

print("total is",total_sum)