class Solution:
    def longestAlmostUniqueSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict

        left = 0
        freq = defaultdict(int)
        repeated = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] == 2:
                repeated += 1

            while repeated > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 1:
                    repeated -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

