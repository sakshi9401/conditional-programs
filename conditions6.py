#to find no. is multiple of 4 and leaves remender 6 after dividing by 8
num = int(input())

if num%4==0 and num%8==6 :

    print(" yes ,no. is multiple of 4 and leaves remender 6 after dividing by 8")

elif num%4==0 or num%8==6 :

    print(" no. is either multiple of 4 or leaves remender 5 after dividing by 8")

else :

    print("no. is neither multiple of 4 nor leaves remender 5 after dividing by 8")