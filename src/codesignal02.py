def csBinaryToASCII(binary: str) -> str:
  word = ""
  nums = [binary[i:i+8] for i in range(0, len(binary), 8)]
  for num in nums:
      word += chr(int(num, 2))
  return word 

print(csBinaryToASCII("011011000110000101101101011000100110010001100001"))