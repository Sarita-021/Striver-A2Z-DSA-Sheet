bool isArmstrong(int num) {
    int k = to_string(num).length();
    int sum = 0;
    int n = num;
    while(n > 0){
        int ld = n % 10;
        sum += pow(ld, k); 
        n = n / 10;
    }
    return sum == num ? true : false;
}
