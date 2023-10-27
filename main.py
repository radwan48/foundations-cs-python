#Question 1
print("a. 10*(90+2)-5 = 915") # Solved by hand
print("b. 10*90+2-5 = 897")
print("c. 10*90+(2-5) = 897")
print("d. 10.0*(90+2)-5 = 915")
print("e. 120/(20+40)-(6-2)/4 = 1")
print("f. 5.0/2 = 2.5")
print("g. 5/2 = 2.5")
print("h. 5.0/2.0 = 2.5")
print("i. 5/2.0 = 2.5")
print("j. 678%3*(8-(9/4)) = 0")
#verifying
print("a.", 10*(90+2)-5)
print("b.", 10*90+2-5)
print("c.", 10*90+(2-5))
print("d.", 10.0*(90+2)-5)
print("e.", 120/(20+40)-(6-2)/4)
print("f.", 5.0/2)
print("g.", 5/2)
print("h.", 5.0/2.0)
print("i.", 5/2.0)
print("j", 678 % 3*(8-(9/4)))

#--------------------------------------- ASSIGNMENT -----------------------------------------------------------#
# Question 2
id_add0 = "0" # this will be added to id input
id_input = input("ID :")
id_input = id_input.strip()
id_input = id_add0 + id_input
name_input = str.upper(input("name :")) # change string to uppercase
name_input = name_input.strip() #remove all unneeded spaces
dob_input = input("Date of Birth (DD/MM/YYY):")
dob_input = dob_input.replace("-", "/") #if user type "-" it will replace it to "/"
dob_input = dob_input.strip()
address_input = str.lower(input("Address :")) # change string to lowercase
address_input = address_input.strip()
print(f"Your profile - ID: [{id_input}], name: [{name_input}], DOB: [{dob_input}], Address:[{address_input}]")
#----------------------------------------------------------------------------------------------------------------
# Question 3
ask_number = input("Type a number :")
print(f"{ask_number} has {len(ask_number)} digits")
#-----------------------------------------------------------------------------------------------
#Question 4---------------------------------------------------------------

numeric_grade = eval(input("What is your numeric grade :"))
letter_grade = ""
if numeric_grade >= 97:
    letter_grade = "A+"
elif 93 <= numeric_grade < 97:
    letter_grade = "A"
elif 90 <= numeric_grade < 93:
    letter_grade = "A-"
elif 87 <= numeric_grade < 90:
    letter_grade = "B+"
elif 83 <= numeric_grade < 87:
    letter_grade = "B"
elif  80 <= numeric_grade < 83:
    letter_grade = "B-"
elif 77 <= numeric_grade < 80:
    letter_grade = "C+"
elif 73 <= numeric_grade < 77:
    letter_grade = "C"
elif 70 <= numeric_grade < 73:
    letter_grade = "C-"
elif 67 <= numeric_grade < 70:
    letter_grade = "D+"
elif 63 <= numeric_grade < 67:
    letter_grade = "D"
elif 60 <= numeric_grade < 63:
    letter_grade = "D-"
elif numeric_grade < 60:
    letter_grade = "F"
print(f"{numeric_grade} is equivalent to a {letter_grade}.")
#---------------------------------------------------------------------------------------------------------
# Question 5

n_input = int(input("Choose a Number :"))
for i in range(1, n_input + 1): # it increases one step until n
    print(i * "*")
for i in range(n_input - 1, 0, -1): # starting from n and subtracting by 1,in reverse
    print(i * "*")
#--------------------------------------------------------------------------------------------------
first_number_input = int(input("First Number :"))
while True:

    second_number_input = int(input("Second Number :"))
    if second_number_input < first_number_input:
        print("Choose a number greater than first number ")
    else:
        break
for num in range(first_number_input, second_number_input, +1): # in range of two input numbers
    if num % 2 == 0: # "if num is even"
     print(num)

def function(s,i):
  reversed_string = s[::-1]
  print(reversed_string * i)



function("hello",5)