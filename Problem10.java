import java.lang.Math;
 
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
