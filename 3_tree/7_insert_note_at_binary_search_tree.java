
/* Node is defined as :
class Node 
    int data;
    Node left;
    Node right;
*/

static Node Insert(Node root, int value) {
    if (root == null) {
        Node node = new Node();
        node.data = value;
        root = node;
    } else if (value < root.data) {
        root.left = Insert(root.left, value);
    } else {
        root.right = Insert(root.right, value);
    }

    return root;
}

// static Node Insert(Node root, int value)
// {
//     Node node = new Node();
//     node.data = value;
    
//     if (root == null) {
//         return node;
//     }
    
//     Node temp = root;
//     Node pre = null;
//     boolean isLeft = true;
    
//     while (temp != null) {
//         pre = temp;
//         if (value < temp.data) {
//             temp = temp.left;
//             isLeft = true;
//         } else {
//             temp = temp.right;
//             isLeft = false;
//         }
//     }
    
//     if (isLeft) {
//         pre.left = node;
//     } else {
//         pre.right = node;
//     }
    
//     return root;
// }

