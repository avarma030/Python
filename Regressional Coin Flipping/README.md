This code calculates count of Heads and Tails after applying regressional flipping on N number of coins.

Regressional flipping of coins:
  1. Consider there are N number of coins all facing 'Heads' initially
  2. Flip every alternate coin starting from 2nd coin, so that they are facing 'Tails' now (H, T, H, T, H, T,...)
  3. In the next regression, flip every third coin (H, T, T, T, H, H,...)
  4. In the next regression, flip every fourth coin and so on until you reach flipping Nth coin
  5. Count the number of Heads and Tails in the end
