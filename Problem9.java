/* 
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 * a2 + b2 = c2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */

import java.lang.Math;
 
public class Problem9 {

  public static void main(String[] args) {
  
    double c = -1;
    
    for (int a = 1; a < 1000; a++) {
    
      for (int b = 1; b < 1000; b++) {
      
        c = Math.sqrt(a * a + b * b);
        
        if (a + b + c == 1000 && c == (int) c) {
        
          System.out.print(a * b * c);
          return;
        }
      }
    }
  }
}
