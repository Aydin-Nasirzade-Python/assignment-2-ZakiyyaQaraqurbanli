#import libraries here

def main():
  a=input("Enter name of the month [ex. June]: ")
  b=int(input("Enter the day [ex. 5]: "))
  if a=="April" or a=="May" or (a=="March" and 31>=b>=20) or (a=="June" and 1<=b<21):
    print(f"{a} {b} is in Spring")
  elif (a=="June" and 31>b>=21) or a=="July" or a=="August" or (a=="September" and 1<=b<22):
    print(f"{a} {b} is in Summer")
  elif (a=="September" and 31>b>=22) or a=="October" or a=="November" or (a=="December" and 1<=b<21):
    print(f"{a} {b} is in Fall")
  elif (a=="December" and 31>=b>=21) or a=="January" or a=="February" or (a=="March" and 1<=b<20):
    print(f"{a} {b} is in Winter")
  pass

if __name__ == "__main__":
  main()
