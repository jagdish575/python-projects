Hindi = int(input("enter Hindi Number :"))
English= int(input("enter English Number :"))
Mathes =int(input("enter Mathers NUmber :"))
Science = int(input("Enter Science Number: "))
Social_Science = int(input("Enter Social Studies Number: "))
total_maks=Hindi+English+Mathes+Science+Social_Science
average=(Hindi + English + Mathes + Science + Social_Science)/5
print ("The total marks are",total_maks)
if average>=90 and average<=100:
    print("Grade is A")
elif average>=60 and average<=90:
    print("Grade is B")
elif average>40 and average<=60:
    print('Grade is c')
else:
    print("fail")
