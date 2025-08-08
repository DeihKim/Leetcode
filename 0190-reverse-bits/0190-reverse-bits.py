class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = []
        while n > 0:
            binary.append(n % 2)
            if n == 1:
                break
            n //= 2
        
        zeros = 32 - len(binary)
        binary.extend([0] * zeros)

        binary = binary[::-1]
        deci = 0
        for i in range(len(binary)):
            if binary[i] == 1:
                deci += 2 ** i
        return deci