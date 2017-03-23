/* 
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
 
public class Problem4 {

  public static boolean isPalin (int compare) {
  
    String s = Integer.toString(compare);
    int j = s.length();
    
    for (int i = 0; i < (s.length() / 2); i++) {
      
      if (s.charAt(i) != s.charAt(j-1)) {
        
        return false;
      }
        
      j--;
    }
    
    return true;
  }   

  public static void main(String[] args) {
  
    int a = 100;
    int b = 100;
    
    int compare = -1;
    int max = -1;
    
    for (int i = a; i < 1000; i++) {
    
      for (int j = b; j < 1000; j++) {
      
        compare = i * j;
        
        if (max < compare && isPalin(compare) == true) {
        
          max = compare;
        }
      }
    }
    
    System.out.print(max);
  }
}
