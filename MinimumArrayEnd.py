class Solution:
    # Getting TLE in Python
    def minEnd(self, n: int, x: int) -> int:
        res = x
        for _ in range(n - 1):
            res += 1
            res = res | x
        return res

# Same code in Java works fine
# class Solution {
#     public long minEnd(int n, int x) {
#         long res = x;
#         for (int i = 0; i < n - 1; i++) {
#             res += 1;
#             res = res | x;
#         }
#         return res;
#     }
# }
