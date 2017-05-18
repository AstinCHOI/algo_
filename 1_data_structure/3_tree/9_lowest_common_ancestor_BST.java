/* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
*/

// static Node lca(Node root, int v1, int v2)
// {
//     Node r2 = root;
//     Node lca_node = null;
    
//     while (root != null && r2 != null) {
//         if (root == r2) { // if the answer is (1)
//         // if the answer is (4) => if (root == r2 && root.data != v1 && root.data != v2)
//             lca_node = root;
//         }

//         if (v1 < root.data) {
//             root = root.left;
//         } else if (v1 > root.data){
//             root = root.right;
//         } else {
//             break;
//         }
        
//         if (v2 < r2.data) {
//             r2 = r2.left;
//         } else if (v2 > r2.data) {
//             r2 = r2.right;
//         } else {
//             break;
//         }
//     }

//     return lca_node;   
// }


// 8 4 9 1 2 3 6 5

//         8
//       /   \
//      4     9
//    /   \   
//  (1)    6   
//    \   /    
//     2 5  
//      \
//       3

// v=1, v=2


static Node lca(Node root, int v1, int v2)
{
    //Decide if you have to call recursively
    //Samller than both
    if(root.data < v1 && root.data < v2){
        return lca(root.right, v1, v2);
    }
    //Bigger than both
    if(root.data > v1 && root.data > v2){
        return lca(root.left, v1, v2);
    }

    //Else solution already found
    return root;
}