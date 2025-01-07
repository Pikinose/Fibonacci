'''fibbonacci numbers are those which are formed
by adding the previous numbers like 1 then 1+1=2 
then 2+1=3 then 3+2=5. it goes on..'''
#namaste i am pratyush saha from class 8
no1 = 0
no2 = 1
fibbon = no2
for fi in range(11):
    print()
    no1, no2 = no2, fibbon
    fibbon = no1+no2
    print(no1," + ", no2, " is ", fibbon)