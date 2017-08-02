package main

// Python style imports because IDGAF
import "fmt"
import "math/rand"
import "time"

// function to seed random
func random(min, max int) int {
    rand.Seed( time.Now().Unix() )
    return rand.Intn( max - min ) + min
}

// roll the desired dice 
func roll (number int, sides int, bonus int) int {
	damage := 0	
	for i := 1; i <= number; i++ {
		damage += random(number, sides)
	}
	return damage + bonus
}

// main func
func main() {
    _1d20 := roll(2, 20, 0)
    fmt.Println(_1d20)
}
