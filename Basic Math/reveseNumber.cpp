class Solution {
public:
    int reverse(int x) {
        long long int ans = 0;
        while(x != 0)
        {
            int digit = x % 10;
            ans = ans * 10 + digit;
            x /= 10;
        }
        return (ans > INT_MAX || ans < INT_MIN) ? 0 : ans;
    }
};
