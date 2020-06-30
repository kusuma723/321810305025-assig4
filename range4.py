def ran_check(num,low,high):
    for i in range(low,high+1):
        if num==i:
            print("Number is within the range")
            break
    else:
        print("Number is out of range")
ran_check(4,10,5)
