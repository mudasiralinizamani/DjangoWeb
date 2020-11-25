package main


import "fmt"


func main() {


i := 2


switch i {

case 3:

fmt.Println("The value of i is = 3")

case 2:

fmt.Println("The value of i is = 2")

default:

fmt.Println("The value of i is = none")

}


i := 1


for i <= 5 {

fmt.Println("This is for test", i)


i++


if i == 3 {


continue


}

}


}