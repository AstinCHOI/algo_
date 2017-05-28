package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	treeMap := make(map[int]map[int]int)

	var n, q int
	fmt.Scanf("%d %d", &n, &q)

	var a, b, oldX, newX int
	for i := 0; i < n-1; i++ {
		fmt.Scanf("%d %d", &a, &b)
		flagA := false
		if _, ok := treeMap[a]; !ok {
			treeMap[a] = make(map[int]int)
			flagA = true
		}
		if _, ok := treeMap[b]; !ok {
			treeMap[b] = make(map[int]int)
		}
		treeMap[a][b] = 1
		treeMap[b][a] = 1

		if flagA {
			newX, oldX = a, b
		} else {
			newX, oldX = b, a
		}

		for key := range treeMap {
			if key != oldX && key != newX {
				dist := treeMap[key][oldX] + treeMap[oldX][newX]
				treeMap[key][newX] = dist
				treeMap[newX][key] = dist
			}
		}
	}

	var k int
	var nodeS []string
	var nodeI = []int{}
	in := bufio.NewReader(os.Stdin)
	for i := 0; i < q; i++ {
		tmp, _ := in.ReadString('\n')
		k, _ = strconv.Atoi(strings.TrimSpace(tmp))
		line, _ := in.ReadString('\n')
		nodeS = strings.Split(strings.TrimSpace(line), " ")

		for _, str := range nodeS {
			num, _ := strconv.Atoi(str)
			nodeI = append(nodeI, num)
		}

		sum := 0
		for x := 0; x < k-1; x++ {
			for y := x + 1; y < k; y++ {
				sum += nodeI[x] * nodeI[y] * treeMap[nodeI[x]][nodeI[y]]
			}
		}
		kittyCal := sum % (int(math.Pow10(9.0)) + 7)
		fmt.Println(kittyCal)
	}
}
