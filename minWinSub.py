
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    window = {}

    left = 0
    required = len(need)
    formed = 0

    min_len = float("inf")
    start = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        # Shrink the window while it is valid
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            left_char = s[left]
            window[left_char] -= 1

            if (left_char in need and
                    window[left_char] < need[left_char]):
                formed -= 1

            left += 1

    if min_len == float("inf"):
        return ""

    return s[start:start + min_len]


s = "ADOBECODEBANC"
t = "ABC"

print("Minimum window substring:", min_window(s, t))
