package main

import (
	"io/ioutil"
	"log"
)

func main() {
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	err = ioutil.WriteFile("output.txt", content, 0644)
	if err != nil {
		log.Fatal(err)
	}
}
