numbers=[20,30,100,50,80,70]
largest=numbers[0]
for num in numbers:
    if num > largest:
        largest=num
print(f"The Largest number in the list is:{largest}")