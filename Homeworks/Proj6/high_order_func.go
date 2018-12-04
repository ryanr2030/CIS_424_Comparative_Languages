//declare the main package
package main


//Import the format package to utilize the print function
import "fmt"

//the make function is implemented to create slices or dynamic arrays implemented in the map and filter functions
//this is a built in function within go. Make achieves this by allocating A zeroed arras and returning A slice that
//refers ti that array
func main(){
    //declare a list to apply functions to
    myList:=[]float64{2.432, -2.324, 14.8989, 12.4142, 1, 3}

    //print the original list
    fmt.Printf("My List: %v\n", myList)

    //apply the halved function to each element of the list
    fmt.Printf("My List Halved: %v\n", Map(myList, Halve))

    //convert each element within the list to integers
    fmt.Printf("My List as Integers: %v\n", IntMap(myList, FtoInt))

    //use the filter function with the odd function to return only the odd numbers within the function 
    fmt.Printf("My List Only Odds: %v\n", Filter(myList, odd))

    //use the map and reduce functions to return the sum of all the squares of the list
    fmt.Printf("My List Sum of Square: %v\n", Reduce(Map(myList, Square), Sum))

    //use the map and reduce functions to return the sum of all the cubes in the list
    fmt.Printf("My List Sum of Cube: %v\n", Reduce(Map(myList, Cube), Sum))

    //use the reduce function to return the result of multiplying each element in the list together
    fmt.Printf("My List Elements Multiplied: %v\n", Reduce(myList, Multi))



}

//map function to apply a passed function to each element in a list of floats
func Map(s [] float64, f func(float64) float64) [] float64{
    sm := make([]float64, len(s))
    for i, v := range s {
        sm[i] = f(v)
    }
    return sm
}

//map function to apply a passed function to each element in a list of takes in an float returns an int
func IntMap(s [] float64, f func(float64) int) [] int{
    sm := make([]int, len(s))
    for i, v := range s {
        sm[i] = f(v)
    }
    return sm
}

//Filter function to return an element if it passes the boolean test
func Filter(s [] float64, f func(float64) bool) [] float64 {
    sf := make([]float64, 0)
    for _, v := range s {
        if f(v) {
            sf = append(sf, v)
    }
    }
    return sf
}

//Reduce function that applies a function to consecutive elements and returns the result
func Reduce(s [] float64, f func(float64, float64) float64) float64{
    sf:=s[0]
    for i:=1;i<len(s);i++ {
        sf=f(sf, s[i])
    }
    return sf
}
//sums two elements
func Sum(acum float64, x float64) float64{return acum+x}

//cubes an element
func Cube(x float64) float64{return x*x*x}

//squares an element
func Square(x float64) float64{return x*x}

//multiplies two elements
func Multi(acum float64, x float64) float64{return acum*x}

//divides each element by 2
func Halve(x float64) float64{return x/2}

//converts float to integer
func FtoInt(x float64) int{return int(x)}

//tests if an element is even or odd
func odd(x float64) bool{
    if int(x)%2!=0{
        return true
    }
    return false
}
