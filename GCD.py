def GCD(A,B):
  if B==0:
    return A
  else:
    return GCD(B,A%B)
  print("check 1")
