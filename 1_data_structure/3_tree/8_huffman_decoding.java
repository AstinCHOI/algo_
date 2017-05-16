
/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S, Node root)
{
    StringBuilder sb = new StringBuilder();
    Node temp = root;
    for (int i = 0; i < S.length(); i++) {
        temp = (S.charAt(i) == '0' ? temp.left : temp.right);
        if (temp.left == null && temp.right == null) {
            sb.append(temp.data);
            temp = root;
        }
    }
    System.out.print(sb);
}

//         {ϕ,5}
//      0 /     \ 1
//     {ϕ,2}   {A,3}
//    0/   \1
// {B,1}  {C,1}  

// A - 1
// B - 00
// C - 01

// Encoded String "1001011" represents the string "ABACA"