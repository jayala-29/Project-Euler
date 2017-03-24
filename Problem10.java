/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million.
 */
 
public class Problem10 {

  public static boolean checkPrime(int n) {
    
    if (n == 2) {
    
      return true;
    }
    
    if (n % 2 == 0) {
    
      return false;
    }
    
    for(int i = 3; i * i <= n; i += 2) {
    
      if(n % i == 0) {
      
        return false;
      }
    }
    
    return true;
  }

  public static void main(String[] args) {
  
    long sum = 0;
    
    for (int i = 2; i < 2000000; i++) {
    
      if (checkPrime(i) == true) {
      
        sum += i;
      }
    }
    
    System.out.print(sum);
  }
}
