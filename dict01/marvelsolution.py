marvelchars= {
"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

def main():
  char=input("Select one of the following characters: (Starlord, Mystique, Hulk)")
  stat=input("Select something you want to know: (Real name, Powers, Archenemy)")

  charkey= char.lower()
  statvalue= stat.lower()
  charprint= char.title()
  
  print(f"{charprint}'s {statvalue} is : {marvelchars[charkey][statvalue]}.")
  

def again():
  while True:
    repeat= input("Would you like to ask again? (Y/N)").lower()
    if repeat == "y":
        main()
    elif repeat == "n":
        break
    else:
        print("Not a valid response!")
  print("Goodbye!")

main()
again()
