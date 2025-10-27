import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int i,j;
        int num=1;
        for(i=1;i<=n;i++){
            for(j=1;j<=i;j++){
                System.out.print(num+" ");
            }
            num++;
            System.out.println("");
        }
    }
}

// OUTPUT:
// n=5
// 1 
// 2 2 
// 3 3 3 
// 4 4 4 4 
// 5 5 5 5 5 
