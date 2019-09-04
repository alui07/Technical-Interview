/* 374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
*/
public class GuessGame {
    public int guessNumber(int n) {
        int start = 1, mid = 0, guess = -2;
        while (guess != 0) {
            if (start % 2 == 1 && n % 2 == 1) mid = start/2 + n/2 + 1;
            else mid = start/2 + n/2; 
            
            guess = guess(mid);
            if (guess == -1) n = mid;
            else if (guess == 1) start = mid+1;
        }
        return mid;
    }
}