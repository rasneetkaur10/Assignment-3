#Question 1

print('Question 1','\n')

string=input("enter string:")
character=input("enter character:")
i=0
count=0
while(i<len(string)):
   if(string[i]==character):
      count=count+1
   i=i+1
print("The word,", character, "has occured", count, "number of times")


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')


#Question 2

print('Question 2','\n')

#input of year from user and checking if it is a leap year or not
year=int(input("input year:"))
if(year%4==0):
   leapyear=True
elif(year%400==0):
     leapyear=True
elif(year%100==0):
     leapyear=False
else:
    leapyear=False

#input of month and checking the number of days it has
month=int(input("input month[1-12]:"))
if month in(1, 3, 5, 7, 8, 10, 12):
   monthlength=31
elif month==2:
   if leapyear:
      monthlength=29
   else:
      monthlength=28
else:
   monthlength=30    

#printing next date if input date

#input of day
day=int(input("input day[1-31]:"))
if day<monthlength:
   day+=1
else:
   day=1
   if month==12:
       month=1
       year+=1
   else:
       month+=1

print("the next date is [DD/MM/YYYY] %d-%d-%d. "%(day,month,year))


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')



#Question 3

print('Question 3','\n')

first_element=[3, 9, 10]
second_element=[(val, pow(val, 2)) for val in first_element]
print(second_element)


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')


#Question 4

print('Question 4','\n')

Dict={10:"Outstanding", 9:"Excellent", 8:"Very Good", 7:"Good", 6:"Average", 5:"Below Average", 4:"Poor"}
grade=int(input("enter grade:"))

if(grade<4):
    print("Error")
else:
    print("YOUR GRADE IS ", grade, " and ", Dict.get(grade), " Performance")


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')
    

#Question 5
    
print('Question 5','\n')

i=0
x="ABCDEFGHIJK"

#FOR HAVING ITERATIONS TO PRINT THE GIVEN PATTERN
for i in range(6):
    j=i
    while(j>0):
        print(" ",end="")
        j=j-1
    k=0
    for k in range(len(x)-2*i):
        print(x[k],end="")

    print("")


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')
    

#Question 6
    
print('Question 6','\n')

SID=int(input("enter SID:"))
name=input("enter name:")
students={SID:name}

while True:
    option=input("do you want to enter another entry(Y or N):").upper()
    if option=="Y":
        SID=int(input("enter SID:"))
        name=input("enter name:")
        students[SID]=name
    elif option=="N":
        break
    else:
        print("Invalid Input")
#Part a
print(students)
#Part b
print({k:v for k,v in sorted(students.items(),key=lambda x:x[1])})
#part c
print({k:v for k,v in sorted(students.items())})
#Part d
print(students[SID])


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')


#Question 7

print('Question 7','\n')

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("enter a number for number of terms of fibonacci sequence:"))
#CHECK IF THE NUMBER OF TERMS IS VALID.
if nterms<=0:
    print("enter a positive integer")
else:
    print("fibonacci sequence:")
    sum=0
    for i in range(nterms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/nterms)
print("the average of the fibonacci sequence is:",avg)


print(end='\n''\n')
print("*" * 80)
print(end='\n''\n')


#Question 8

print('Question 8','\n')

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}


#PART a
Set_union=set1.union(set2)
Set_intersection=set1.intersection(set2)
a=Set_union-Set_intersection
print(">\n",a)

#PART b
b=set1.union(set2.union(set3))-set1.intersection(set2)-set2.intersection(set3)-set3.intersection(set1)
print("b\n",b)

#PART c
c=((set1.intersection(set2)).union((set1.intersection(set3)).union(set2.intersection(set3))))-set1.intersection(set2.intersection(set3))
print("c\n",c)

#PART d
d=set()
for i in range(1,11):
    if i not in set1:
        d.add(i)
    print("d\n",d)

#PART e

e=set()
if i in range(1,11):
  if i not in set1 and i not in set2 and i not in set3:
    e.add(i)
print("e\n",e)
