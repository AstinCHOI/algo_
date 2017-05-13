/* 
class Node 
    int data;
    Node left;
    Node right;
*/

void LevelOrder(Node root) {
	Queue<Node> queue = new LinkedList<Node>();
	queue.add(root);
	while(!queue.isEmpty()) {
		Node temp = queue.poll();
		System.out.print(temp.data + " ");
		if(temp.left != null) {
			queue.add(temp.left);
		}
		if(temp.right != null) {
			queue.add(temp.right);
		}
	}
}

// Level 1:        3
//               /   \
// Level 2:     5     2
//             / \    /
// Level 3:   1   4  6

// Q: 3 5 2
// T: 3

// Q: 5 2 1 4
// T: 5

// Q: 2 1 4 6
// T: 2

// ...