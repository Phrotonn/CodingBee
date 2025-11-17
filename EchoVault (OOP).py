import os
import time

class MusicVault:
  def __init__(self):
      self.genres = ["pop", "rock", "jazz", "r&b", "lofi"]

  def Wait(self):
      print("Please wait...")
      time.sleep(0.5)
      os.system("cls")

  def Enter(self):
      print("Please press [Enter] to continue")
      input("")
      os.system("cls")

  def Start(self):
    global a
    self.Wait()
    print("Welcome to EchoVault♫!")
    print("This program allows you to manage your music collection.")
    print("You can add, remove, and display songs in your vault.")
    print("Let's get started!")
    a = input("What would you like to do? (View/Add/Update/Delete/Search/Exit): ").lower()
    if a == "view":
      self.View()

    elif a == "add":
      self.Add()

    elif a =="update":
      self.Update()

    elif a =="delete":
      self.Delete()

    elif a =="search":
      self.Search()

    elif a == "exit":
      exit()

    else:
      print("Please input the given options")
      self.Start()
      
  def View(self):
    self.Wait()
    print("What genre of music would you like to view?")
    genre = input("Enter the genre (Pop, Rock, Jazz, R&B, Lofi): ").lower()

    if genre in ["pop", "rock", "jazz", "r&b", "lofi"]: #checks value in genre list, if item is in list = true, if not = false
      if not os.path.exists(genre):
        open(genre, "x").close() #create file but doesnt add anything else
      self.Wait()

      with open(genre, "r") as file:
        lines = file.readlines()
        if len(lines) == 0: #if file = empty 
          print("Empty Vault")
          self.Start()

        else:
          print(f"Displaying all {genre.capitalize()} songs in your vault:")
          for line in lines:
            print(line.strip()) #remove extra line spaces

          self.Enter()
          self.Start()

    else: 
      print("Please input the given genre")
      self.View()

  def Add(self):
    while True:
      self.Wait()
      print("What genre of music would you like to add?")
      genre = input("Enter the genre (Pop, Rock, Jazz, R&B, Lofi): ").lower()

      if genre in ["pop", "rock", "jazz", "r&b", "lofi"]:
        print("Please enter the details of the song you want to add")
        Title = input("Title : ")
        Artist = input("Artist : ")
        Duration = input("Duration : ")
        Date = input("Published date : ")
        print(f"Adding a new song to your {genre.capitalize()} vault")
        with open(genre, "a") as song:
            song.write(f"{Title:2} | {Artist:2} | {Duration:2} | {Date}\n")
        self.Start()

      else:
        print("Please input the given option")

  def Update(self):
      self.Wait()
      print("What genre of music would you like to update?")
      genre = input("Enter the genre (Pop, Rock, Jazz, R&B, Lofi): ").lower()

      if genre in ["pop", "rock", "jazz", "r&b", "lofi"]:
          if not os.path.exists(genre):
              open(genre, "x").close()  # create empty file if it doesn’t exist

          with open(genre, "r") as file:
              lines = file.readlines()

          if len(lines) == 0: 
              print("Empty Vault")
              self.Start()

          Title = input("Old Title: ").lower()
          Artist = input("Old Artist: ").lower()

          found = False
          updated_lines = []

          for line in lines:
              if Title in line.lower() and Artist in line.lower():
                  print("Song found:", line.strip())

                  # ask for new info
                  NewTitle = input("New Title : ")
                  NewArtist = input("New Artist : ")
                  NewDuration = input("New Duration : ")
                  NewDate = input("New Published date : ")

                  # replace only this line
                  updated_lines.append(f"{NewTitle} | {NewArtist} | {NewDuration} | {NewDate}\n")
                  found = True
              else:
                  # keep other lines the same
                  updated_lines.append(line)

          # write updated contents back
          with open(genre, "w") as file:
              file.writelines(updated_lines)

          if found:
              print("Song updated successfully!")

          else:
              print("No Match Found")
          self.Start()

      else:
          print("Please input the given genre")
          self.Update()

  def Delete(self):
    self.Wait()
    print("What genre of music would you like to delete?")
    genre = input("Enter the genre (Pop, Rock, Jazz, R&B, Lofi): ").lower()

    if genre in ["pop", "rock", "jazz", "r&b", "lofi"]: #checks value in genre list, if item is in list = true, if not = false
      if not os.path.exists(genre):
        open(genre, "x").close() #create file but doesnt add anything else
      self.Wait()

      with open(genre, "r") as file:
        lines = file.readlines()
        if len(lines) == 0: #if file = empty 
          print("Empty Vault")
          self.Start()

        print("Please enter the details of the song you want to delete")
        Title = input("Title : ")
        Artist = input("Artist : ")
        print(f"Removing a song from your {genre.capitalize()} vault")
        with open(genre, "w") as song:
            for line in lines:  #go through every saved song in list
                if Title.lower() in line.lower() and Artist.lower() in line.lower():
                    continue #deletes song / skips it
                song.write(line)  #to avoid deleting all other songs
        print("Song removed successfully")
        self.Start()

    else: 
      print("Please input the given genre")
      self.View()


  def Search(self):
      self.Wait()
      print("What song would you like to search?")
      search = input("Enter song title or artist: ").lower()

      genres = ["pop", "rock", "jazz", "r&b", "lofi"]
      found = False

      for genre in genres: #read all genre txt files
          if not os.path.exists(genre):
              open(genre, "x").close()

          with open(genre, "r") as file:
              lines = file.readlines()

              for line in lines:
                  if search in line.lower():  # check if search term is inside the line
                      if not found:
                          print("\nSearch results:")
                      print(f"[{genre.capitalize()}] {line.strip()}")
                      found = True

      if not found:
          print("No matching songs found.")

      self.Enter()
      self.Start()

if __name__ == "__main__": #only run whats needed from another file 
  vault = MusicVault()
  vault.Start()

# #View       -> view file from Pop.txt, Rock.txt
# #Create     -> make new file ex: Pop.txt, Rock.txt (if not yet exist) if exist, append new song to the file
# #Update     -> Append new song to the file / update song in the file
# #Delete     -> delete song from the file

# #Search     -> search song in the file
