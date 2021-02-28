import time

def num_max_continue_string(n, k=5):
    def _num_max_continue_string(n, ans, k):
        if n < k:
            return 0
        if n == k:
            return 1
        if ans[n] != 0:
            return ans[n]
        cnt = 0
        d = n - (k + 1)
        cnt += 1 << (n - k)
        for c in range(0, d + 1):
            cnt += ((1 << c) - _num_max_continue_string(c, ans, k)) * (1 << (d - c))
        ans[n] = cnt
        return cnt
    return _num_max_continue_string(n, [0 for _ in range(n + 1)], k)

def dfs(n, k=5, s=0, c=0):
    if c == k:
        return 1 << (n - s)
    if s == n:
        return 0
    else:
        cnt = 0
        cnt += dfs(n, k, s + 1, 0)
        cnt += dfs(n, k, s + 1, c + 1)
        return cnt

def solve(n, k):
    print(dfs(n, k)) # dfs对拍
    print(num_max_continue_string(n, k))


start = time.time()
solve(24, 5)
print('cost: {}ms'.format((time.time() - start) * 1000))
