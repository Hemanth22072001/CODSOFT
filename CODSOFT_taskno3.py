import random

lower="abcdefghijklmnopqrstuvwxys"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="@$&*."

st= upper + lower + number + symbols
length= int(input("Enter the length of Password to Generate: "))
password="".join(random.sample(st, length))

print(f"Your New Generated Password is: {password}")