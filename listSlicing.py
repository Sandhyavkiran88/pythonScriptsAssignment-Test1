list=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {list}")
print(type(list))

first_five= list[0:5:1]
print(f"Extracted first five elements: {first_five}")

first_five.reverse()
print(f"Reverse extracted elements: {first_five}")
