// http://www.geeksforgeeks.org/avl-tree-set-1-insertion/

// Operation: O(height) - search, max, min, insert, delete
// Worst: O(n) - Skewed Binary Tree
// Best: O(log n) - if hight = log n

/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

// A utility function to get height of the tree
int height(node* N)
{
    if (N == NULL)
        return -1;
    return N->ht;
}
 
// A utility function to get maximum of two integers
int max(int a, int b)
{
    return (a > b)? a : b;
}
 
/* Helper function that allocates a new root with the given val and
    NULL left and right pointers. */
node* newNode(int val)
{
    node* pNode = new node();
    pNode->val   = val;
    pNode->left   = NULL;
    pNode->right  = NULL;
    pNode->ht = 0;  // new pNode is initially added at leaf
    return pNode;
}
 
// A utility function to right rotate subtree rooted with y
// See the diagram given above.
node* rightRotate(node* y)
{
    node* x = y->left;
    node* T2 = x->right;
 
    // Perform rotation
    x->right = y;
    y->left = T2;
 
    // Update heights
    y->ht = max(height(y->left), height(y->right))+1;
    x->ht = max(height(x->left), height(x->right))+1;
 
    // Return new root
    return x;
}
// a) Left Left Case
// T1, T2, T3 and T4 are subtrees.
//          y                                      x 
//         / \                                   /   \
//        x   T1      Right Rotate (y)          z      y
//       / \          - - - - - - - - ->      /  \    /  \ 
//      z   T2                               T3  T4  T2  T1
//     / \
//   T3   T4

 
// A utility function to left rotate subtree rooted with x
// See the diagram given above.
node* leftRotate(node* x)
{
    node* y = x->right;
    node* T2 = y->left;
 
    // Perform rotation
    y->left = x;
    x->right = T2;
 
    //  Update heights
    x->ht = max(height(x->left), height(x->right))+1;
    y->ht = max(height(y->left), height(y->right))+1;
 
    // Return new root
    return y;
}
// c) Right Right Case
//   x                                y
//  /  \                            /   \ 
// T1   y     Left Rotate(x)       x      z
//     /  \   - - - - - - - ->    / \    / \
//    T2   z                     T1  T2 T3  T4
//        / \
//      T3  T4
 
// Get Balance factor of root N
int getBalance(node* N)
{
    if (N == NULL)
        return -1;
    return height(N->left) - height(N->right);
}
 
// Recursive function to insert val in subtree rooted
// with root and returns new root of subtree.
node* avlTree(node* root, int val)
{
    /* 1.  Perform the normal BST insertion */
    if (root == NULL)
        return(newNode(val));
 
    if (val < root->val)
        root->left  = avlTree(root->left, val);
    else
        root->right = avlTree(root->right, val);

    /* 2. Update height of this ancestor root */
    root->ht = 1 + max(height(root->left),
                           height(root->right));
 
    /* 3. Get the balance factor of this ancestor
          root to check whether this root became
          unbalanced */
    int balance = getBalance(root);
 
    // If this root becomes unbalanced, then
    // there are 4 cases
 
    // Left Left Case
    if (balance > 1 && val < root->left->val)
        return rightRotate(root);
    // a) Left Left Case
    // T1, T2, T3 and T4 are subtrees.
    //          y                                      x 
    //         / \                                   /   \
    //        x   T1      Right Rotate (y)          z      y
    //       / \          - - - - - - - - ->      /  \    /  \ 
    //      z   T2                               T3  T4  T2  T1
    //     / \
    //   T3   T4
 
    // Right Right Case
    if (balance < -1 && val > root->right->val)
        return leftRotate(root);
    // c) Right Right Case
    //   x                                y
    //  /  \                            /   \ 
    // T1   y     Left Rotate(x)       x      z
    //     /  \   - - - - - - - ->    / \    / \
    //    T2   z                     T1  T2 T3  T4
    //        / \
    //      T3  T4
 
    // Left Right Case
    if (balance > 1 && val > root->left->val)
    {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    // b) Left Right Case
    //      z                               z                           x
    //     / \                            /   \                        /  \ 
    //    y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
    //   / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
    // T1   x                          y    T3                    T1  T2 T3  T4
    //     / \                        / \
    //   T2   T3                    T1   T2
 
    // Right Left Case
    if (balance < -1 && val < root->right->val)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    // d) Right Left Case
    //    z                            z                            x
    //   / \                          / \                          /  \ 
    // T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    //     / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
    //    x   T4                      T2   y                  T1  T2  T3  T4
    //   / \                              /  \
    // T2   T3                           T3   T4
 
    return root;
}
 
node* insert(node* root, int val) {
    node* temp = root;
    root = avlTree(temp, val);

    return root;
}







