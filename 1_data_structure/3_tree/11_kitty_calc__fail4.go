package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
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
	in := bufio.NewReader(os.Stdin)
	for i := 0; i < q; i++ {
		tmp, _ := in.ReadString('\n')
		k, _ = strconv.Atoi(strings.TrimSpace(tmp))
		line, _ := in.ReadString('\n')
		nodeS := strings.Split(strings.TrimSpace(line), " ")
		nodeI := []int{}
		for _, str := range nodeS {
			num, _ := strconv.Atoi(str)
			nodeI = append(nodeI, num)
		}

		sum := 0
		for x := 0; x < k-1; x++ {
			visited := []int{nodeI[x]}
			sum += dist(nodeI[x], nodeI[x+1:], visited, 0, -1, 0)

		}
		kittyCal := sum % (int(math.Pow(10, float64(9))) + 7)
		fmt.Println(kittyCal)
	}
}

func dist(a int, b, visited []int, distance, up, sum int) int {
	if len(b) == 0 {
		return sum
	} else if i, ok := contains2(b, a); ok {
		sum += visited[0] * a * distance
		// b = append(b[:i], b[i+1:])
		b = b[:i+copy(b[i:], b[i+1:])]
	}

	for _, node := range treeDict[a] {
		if !contains(visited, node) {
			visited = append(visited, node)
			return dist(node, b, visited, distance+1, up, sum)
		}
	}

	return dist(visited[len(visited)+up-1], b, visited, distance-1, up-1, sum)
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func contains2(s []int, e int) (int, bool) {
	for i, a := range s {
		if a == e {
			return i, true
		}
	}
	return -1, false
}
