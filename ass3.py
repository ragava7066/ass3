print('program started')
print('enter marks obtained in 3 subjects :')
m1 = int(input('enter m1 : '))
m2 = int(input('enter m2 : '))
m3 = int(input('enter m3 : '))
average = ((m1+m2+m3)/3)
if average>=100 and average>=91 :
    print('your grade is : O')
elif average>=90 and average>81:
    print('your grade is : A')
elif average>=80 and average>71:
    print('your grade is : B')     
elif average>=70 and average>61:
    print('your grade is : C')      
else :
    print('you are failed!')    
print('program ended')    
