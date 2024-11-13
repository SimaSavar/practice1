enter_number=input("enter a number:")
len_number=int(len(enter_number))
a=0
if enter_number.isdigit():
   for i in enter_number:
       i=int(i)
       a=i**len_number+a
   if a==int(enter_number):
      print(enter_number,"is an  Armstrong number")
   else:
      print(enter_number,"is not an Armstrong number")
else:
    print("It is an invalid entry.Don't use non-numeric,float,or negative values!")
   