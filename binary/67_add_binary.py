class Solution:
    def addBinary(self, a: str, b: str) -> str:
        last_a, last_b = len(a) - 1, len(b) - 1 # Start from indexable value
        carry = 0
        ans = [] # Least Signficant Bit (LSB) starts from left

        while last_a >= 0 or last_b >= 0 or carry > 0:
            total_bit_sum = carry
            if last_a >= 0:
                total_bit_sum += int(a[last_a])
                last_a -= 1
            if last_b >= 0:
                total_bit_sum += int(b[last_b])
                last_b -= 1

            # append value that will not carried over
            ans.append(str(total_bit_sum % 2))

            # get value that will be carried over
            carry = total_bit_sum // 2

        # reverse string so LSB starts from right
        return ''.join(ans[::-1])