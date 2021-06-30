students = {}

number = input("studenets number : ")
name = input("student name: ")
surName = input("student surname:")
phoneNumber = input("phone nuber :")

students[number] = {
    'name':name,
    'surNume':surName,
    'phoneNumber':phoneNumber
}

print(students)

## 2nd solution way 

students.update({
    number:{
      'name':name,
      'surNume':surName,
      'phoneNumber':phoneNumber
    }
})

print(students)
