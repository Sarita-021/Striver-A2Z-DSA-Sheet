class Solution {
public:
    bool isPalindrome(int x) {
        long int rev = 0;
        long int n = x;
        
        while (n) {
            int r = n%10;
            rev = rev*10 + r;
            n = n/10;
        }
        
        if (rev==x && rev>=0) return true;
        return false;
    }
};
