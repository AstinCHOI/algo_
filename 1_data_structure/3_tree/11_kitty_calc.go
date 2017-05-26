package main

import (
	"fmt"
	"strconv"
	"strings"
)

var treeDict map[int][]int
var treeMap map[int]map[int]int

func main() {
	treeDict = make(map[int][]int)
	treeMap = make(map[int]map[int]int)

	var n, q int
	fmt.Scanf("%d %d", &n, &q)

	var a, b int
	for i := 0; i < n-1; i++ {
		fmt.Scanf("%d %d", &a, &b)

		treeDict[a] = append(treeDict[a], b)
		if _, ok := treeMap[a]; !ok {
			treeMap[a] = make(map[int]int)
		}

		treeDict[b] = append(treeDict[b], a)
		if _, ok := treeMap[b]; !ok {
			treeMap[b] = make(map[int]int)
		}
	}

	var k int
	var node string
	for i := 0; i < q; i++ {
		fmt.Scanf("%d", &k)

		fmt.Scanf("%s", &node)
		nodeS := strings.Split(node, " ")
		nodeI := []int{}
		for _, str := range nodeS {
			num, _ := strconv.Atoi(str)
			nodeI = append(nodeI, num)
		}

		sum := 0
		for x := 0; x < k; x++ {
			for y := x + 1; y < k; y++ {
				sum += 0
			}
		}
		kittyCal := 0
		fmt.Println(kittyCal)
	}
}
