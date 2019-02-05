package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		another := target - nums[i]
		if _, ok := m[another]; ok {
			return []int{m[another], i}
		}
		m[nums[i]] = i
	}
	return nil
}

func main() {
	fmt.Println("vim-go")
	nums := []int{1, 2}
	var target int=3
	var result []int
	result = twoSum(nums, target)
	fmt.Println(result)
}
