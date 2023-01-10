We found the solution for improving the accuracy.



So the earlier issue with smoothing was that, when we were mutliplying the terms in the numerator directly, then even if one of the pixel had probability as zero for corresponding label and pixel value (which obviously be true for some pixel in each rwo of data for a particular value and particular label) then the whole product goes to 0.

Then we tried taking the log and converting multiplication to addition, but then the log was getting 0 as input and that was wrong too. So we addded one in each probability value at this statement 

prob=prob+math.log(float(Xi_dict[((i),int(x[i]),k)] +1))

But that didn't help with the accuracy either because its mathematically incorrect, because adding 1 to a smaller than 1 number increases the error significantly. 

So what we tried to do is that instead of adding 1 here, we added one to the value given by the counter(i,j,k) function before calculating its probability in the probability function used for Xi_dict. So adding 1 here was useful because here even if counter is 0 adding 1 will make the probability non-zero. 

And since denominator, after division the error would be negligible. 

So this is the solution to the error. 
