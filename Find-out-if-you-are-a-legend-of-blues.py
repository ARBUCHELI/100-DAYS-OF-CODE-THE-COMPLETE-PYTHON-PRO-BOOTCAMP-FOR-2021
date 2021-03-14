print('''
            /;)
           /;(
           >_/
           |-|
           |-|
           |-|
           |-|
           |-|
           |-|
           |-|
       _   |-|
      / \  |-|   _
    
     :   ,`'-'`'/|:
      \  \ ...   ;/
       :  )...  ::
       ; / ...  ::
      / /  ___   \\
     :  `-|||||.  \:
     :        (\`-';
      `._________,'
 
  
''')
print("WELCOME TO THE BLUESMEN TESTER.")
print("Here you will find out if you are a bluesman, a metalhead or in the worst case,a fan of Madonna or Britney Spears in which case---> Shame on You Ha Ha Ha!!\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
guitar = input("You're at a guitar shop. Which guitar you will buy? Type \"gibson\" or \"fender\"\n").lower()
if guitar == "gibson":
  artist = input("You've got free tickets for a concert. Which artist you are going to see?. Type \"clapton\" to see Eric Clapton. Type \"maiden\" to see Iron Maiden\n").lower()
  if artist == "clapton":
    formato = input("Someone is going to give you a new album for your blues collection in the format that you prefer. vinyl, cd and mp3. Which format do you choose?\n").lower()
    if formato == "vinyl":
      print("Cheers!! You are definitely a bluesman and you know about music!!")
    elif formato == "cd":
      print("Maybe you are too young to be a real bluesman son.")
    elif formato == "mp3":
      print("You're neither a metalhead nor a bluesman, you don't respect music, so you might as well go out there and listen to Madonna!")
    else:
      print("Shame on you, you probably like rap music!")
  else:
    print("You're a metalhead, you fit more in a bar in East London than in a bar in Chicago!")
else:
  print("You're a metalhead, you'd better go over there to listen to Anthrax or Slayer!!")
