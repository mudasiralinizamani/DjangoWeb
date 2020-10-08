package main


import "fmt"


func main () {


x := 50


a := &x


fmt.Println("The address of x is ", &x)

fmt.Println("The address of a is ", a)

fmt.Println("The value of x is ", *a)


}