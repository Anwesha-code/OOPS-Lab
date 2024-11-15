while(True):
 try:
  num = int(input("Enter any value in 10 to 50 range: "))
  if num < 10:
   raise ValueTooSmallError
  elif num > 50:
   raise ValueTooLargeError
  break
 except ValueTooSmallError :
  print("Value is below range..try again")
 except ValueTooLargeError :
  print("value out of range...try again")
  print("Great! value in correct range.")
