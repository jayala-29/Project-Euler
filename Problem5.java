/*
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */
 
public class Problem5 {

  public static void main(String[] args) {
  
    int n = 1;
  
    while(true) {
    
      for (int i = 1; i <= 20; i++) {
      
        if (n % i != 0) {
        
          break;
        }
        
        if (n % i == 0 && i == 20) {
        
          System.out.print(n);
          return;
        }
      }
      
      n++;
    }
  }
}
