#import libraries here

def main():
  a=input("Enter a month [ex. March]: ")
  b=int(input("Enter the day [ex. 12]: "))
  if (a=="December" and 31>=b>=22) or (a=="January" and 1<=b<=19):
    print("Your zodiac sign is Capricorn")
  elif (a=="January" and 31>=b>=20) or (a=="February" and 1<=b<=18):
    print("Your zodiac sign is Aquarius")
  elif (a=="February" and 29>=b>=19) or (a=="March" and 1<=b<=20):
    print("Your zodiac sign is Pisces")
  elif (a=="March" and 31>=b>=21) or (a=="April" and 1<=b<=19):
    print("Your zodiac sign is Aries")
  elif (a=="April" and 30>=b>=20) or (a=="May" and 1<=b<=20):
    print("Your zodiac sign is Taurus")
  elif (a=="May" and 31>=b>=21) or (a=="June" and 1<=b<=20):
    print("Your zodiac sign is Gemini")
  elif (a=="June" and 30>=b>=21) or (a=="July" and 1<=b<=22):
    print("Your zodiac sign is Cancer")
  elif (a=="July" and 31>=b>=23) or (a=="August" and 1<=b<=22):
    print("Your zodiac sign is Leo")
  elif (a=="August" and 31>=b>=23) or (a=="September" and 1<=b<=22):
    print("Your zodiac sign is Virgo")
  elif (a=="September" and 30>=b>=23) or (a=="October" and 1<=b<=22):
    print("Your zodiac sign is Libra")
  elif (a=="October" and 31>=b>=23) or (a=="November" and 1<=b<=21):
    print("Your zodiac sign is Scorpion")
  elif (a=="November" and 30>=b>=22) or (a=="December" and 1<=b<=21):
    print("Your zodiac sign is Sagittarius")
  else:
    print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
