/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */

import java.math.BigInteger;

public class Problem3 {

  public static boolean checkPrime (BigInteger p, BigInteger increment) {
  
    BigInteger i = new BigInteger("2");

    while (i.compareTo(p) < 0) {
    
      if ((p.mod(i)).equals(0)) {
      
        return false;
      }

      i = i.add(increment);
    }
    
    return true;
  }

  public static void main(String[] args) {
  
    BigInteger number = new BigInteger("600851475143");
    BigInteger biggestPrime = new BigInteger ("-1");

    BigInteger i = new BigInteger("2");
    BigInteger increment = new BigInteger("1");
    
    while (i.compareTo(number) < 0) {
    
      if ((number.mod(i)).equals(0) && checkPrime(i, increment) == true) { 
      
        if (biggestPrime.compareTo(i) == -1) {
        
          biggestPrime = i;
        }
      }

      i = i.add(increment);
    }
    
    System.out.print(biggestPrime.toString());
  }
}
