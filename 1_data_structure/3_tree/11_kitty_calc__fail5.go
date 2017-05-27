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
		// fmt.Scanf("%d", &k)
		tmp, _ := in.ReadString('\n')
		k, _ = strconv.Atoi(strings.TrimSpace(tmp))
		node, _ := in.ReadString('\n')
		nodeS := strings.Split(node, " ")
		nodeI := []int{}
		for _, str := range nodeS {
			num, _ := strconv.Atoi(str)
			nodeI = append(nodeI, num)
		}

		sum := 0
		for x := 0; x < k; x++ {
			for y := x + 1; y < k; y++ {
				visited := []int{nodeI[x]}
				way := []int{nodeI[x]}
				sum += (nodeI[x] * nodeI[y] * dist(nodeI[x], nodeI[y], visited, way, 0, -1))
			}
		}
		kittyCal := sum % (int(math.Pow(10, float64(9))) + 7)
		fmt.Println(kittyCal)
	}
}

func dist(a, b int, visited, way []int, distance, up int) int {
	if a == b {
		treeMap[way[0]][b] = distance
		treeMap[b][way[0]] = distance
		return distance
	} else if val, ok := treeMap[a][b]; ok {
		if way[0] == a {
			return val
		}
	}

	for _, node := range treeDict[a] {
		if !contains(visited, node) {
			visited = append(visited, node)
			way = append(way, node)
			return dist(node, b, visited, way, distance+1, up)
		}
	}

	wayLen := len(way)
	treeMap[way[0]][way[wayLen-1]] = distance
	treeMap[way[wayLen-1]][way[0]] = distance
	way = way[:wayLen-1]
	return dist(visited[len(visited)+up-1], b, visited, way, distance-1, up-1)
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}
