totalsum = 0
for num in range(1,500):  				#range for 1 - 500
   if ( num % 3 == 0 or num % 5 == 0 ): #checking multiples of 3 or 5
       totalsum = totalsum + num;    	#adding them
print totalsum							#printing the totalsum
