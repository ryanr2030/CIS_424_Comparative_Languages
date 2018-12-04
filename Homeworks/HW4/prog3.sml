(*Krishaun Bartlet 2696531 and Ryan Reynolds 2693018*)

(*Problem 1: Return the second element of a list*)
print("\nQuestion 1 \n");
exception ListTooShort;
val L1=[3,4,5,8,10];
fun secondEle(nil)=raise ListTooShort
|secondEle(x::nil)=raise ListTooShort
|secondEle(x::xr)=hd(xr);
secondEle(L1);

(*Problem 2: Remove the third element within a list of integers*)
print("\nQuestion 2 \n");
val L2=[1,2,3,4,5,6];

fun rmv3(nil)=raise ListTooShort
    |rmv3(x::nil)=raise ListTooShort
    |rmv3(x::y::nil)=raise ListTooShort
    |rmv3(x::y::z::zr)=[x]@[y]@zr;
rmv3(L2);

(*Problem 3: Use a max of three comparisons to find the max and min of three integers*)
print("\nQuestion 3 \n");
fun MaxMin(a,b,c) =
        if a > b then MaxMin(b, a, c)
    	else if b < c then MaxMin(a, c, b)
    	else if a < c then MaxMin(c, b, a)
    	else (b, c);
print("Passed 1, 2, 3 to MaxMin");
MaxMin(1,2,3);
print("Passed 2, 1, 3 to MaxMin");
MaxMin(2,1,3);
print("Passed 3, 2, 1 to MaxMin");
MaxMin(3,2,1);
print("Passed 2, 3, 1 to MaxMin");
MaxMin(2,3,1);
print("Passed 1, 3, 2 to MaxMin");
MaxMin(1,3,2);
print("Passed 3, 1, 2 to MaxMin");
MaxMin(3,1,2);






(*Problem 4: Flips alternate elements of a list, if list has an odd number*)
(*of elements the last is simply added to the end of the list*)
print("\nQuestion 4 \n");
val L4odd=[1,2,3,4,5,6,7];
val L4even=[1,2,3,4,5,6];
fun alternate(nil)=nil |alternate(x::nil)=[x] |alternate(x::y::xr)=[y]@[x]@alternate(xr);
alternate(L4odd);
alternate(L4even);


(*Problem 5: Uses an anonymous function within the map function to replace all*)
(*negative numbers with 0.0 in a list of reals*)
print("\n*****For Q5-Q7 List [1.0, 2.0, -1.0, 3.0, 25.0, -3.0, 2.5, 2.8] is passed to the anon function*****\n");
print("\nQuestion 5 \n");
fun map (func, nil) = nil
         |map(func, x::xr) = func(x) :: map(func,xr) ;

map(fn x => if x < 0.0 then 0.0 else x, [1.0, 2.0, ~1.0, 3.0, 25.0, ~3.0, 2.5, 2.8]) ;

(*Problem 6: Uses the reduce function and an anonymous function to find the min in a list of reals*)
print("\nQuestion 6 \n");
exception EmptyList;
fun reduce(func, nil) = raise EmptyList
	|reduce(func,[a]) = a
    |reduce(func,x::xr) = func(x,reduce(func,xr)) ;

reduce(fn (x,y) => if y >= x then x else y, [1.0, 2.0, ~1.0, 3.0, 25.0, ~3.0, 2.5, 2.8]);

(*Problem 7: uses the filter function and an anonymous function to find elements*)
(*between 2.0 and 3.0 inclusive in a list of reals*)

print("\nQuestion 7 \n");
 fun filter(func,nil) = nil
       |   filter(func,x::xr) =
       if func(x) then x::filter(func,xr)
       else filter(func,xr) ;
filter(fn x => x >=2.0 andalso x <=3.0, [1.0, 2.0, ~1.0, 3.0, 25.0, ~3.0, 2.5, 2.8]);



