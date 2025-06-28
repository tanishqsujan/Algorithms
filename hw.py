import time

def rabin_karp(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    d = 256  
    h = pow(d, m-1) % prime
    p = 0  
    t = 0  
    result = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                result.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % prime
            if t < 0:
                t += prime
    return result

def kmp(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    result = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def compare_algorithms(text, pattern):
    print("Pattern:", pattern)

    start = time.time()
    rk_result = rabin_karp(text, pattern)
    rk_time = time.time() - start
    print("Rabin-Karp Result:", rk_result)
    print("Rabin-Karp Time:", rk_time, "seconds")

    start = time.time()
    kmp_result = kmp(text, pattern)
    kmp_time = time.time() - start
    print("KMP Result:", kmp_result)
    print("KMP Time:", kmp_time, "seconds")

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB" * 1000  
    pattern = "ABABCABAB"
    compare_algorithms(text, pattern)
