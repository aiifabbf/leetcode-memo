// 数出 [0, n) 范围内素数的个数。
// 
// 用筛法挺好的，试着用Java写了一个。

class Solution {
    public int countPrimes(int n) {
        if (n == 0 || n == 1) {
            return 0;
        }

        boolean[] isPrime = new boolean[n];
        java.util.Arrays.fill(isPrime, true); // 先假设全是素数
        isPrime[0] = false;
        isPrime[1] = false; // 0和1不管
        int count = 0;

        for (int i = 2; i < n; i = i + 1) { // 从2开始筛
            // 上界其实是有优化空间的，其实不用遍历到n-1，遍历到ceiling(sqrt(n))就可以了。
            if (isPrime[i] == true) { // 如果发现i是素数
                // System.out.println(i);
                count = count + 1;
                for (int j = 1; j * i < n; j = j + 1) { // 就把2i, 3i, 4i, ...全部标记为非素数
                    // 这里也是有优化空间的，但是我不理解。
                    isPrime[j * i] = false;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) { // Java好方便啊，test直接写在这里就好了
        Solution s = new Solution();
        System.out.println(s.countPrimes(10)); // 4
        System.out.println(s.countPrimes(0)); // 0
        System.out.println(s.countPrimes(1)); // 0
        System.out.println(s.countPrimes(2)); // 0
    }
}