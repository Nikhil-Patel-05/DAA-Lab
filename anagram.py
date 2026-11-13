
from collections import Counter

def find_anagrams(s, p):
    n, m = len(s), len(p)

    if m > n:
        return []

    p_count = Counter(p)
    window_count = Counter()
    result = []

    for right in range(n):
        window_count[s[right]] += 1

        # Keep the window length equal to len(p)
        if right >= m:
            left_char = s[right - m]
            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]

        # Compare character frequencies
        if window_count == p_count:
            result.append(right - m + 1)

    return result


s = "cbaebabacd"
p = "abc"

print(find_anagrams(s, p))
