def csReverseIntegerBits(n: int) -> int:
   return int(bin(n)[2:][::-1], 2)

print(csReverseIntegerBits(417))