import pickle

Students={'John':'95','Alice': '85','Carol':'75','Nick':'88'}
print(Students)
print(type(Students))

user_name = input("Enter the student's name: ").strip()

if user_name in Students.keys():
   print(f"{user_name}'s marks: {Students[user_name]}")

else:
   print("Student not found.")




