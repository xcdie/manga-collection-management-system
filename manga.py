calss manga:
def __init__(self, title, author, volume)
self.title = title
self.author = author
self.volume = volume 

def __str__(self)
return(f"Title :{self.title} Author : {self.author} Volume: {self.volume}

class mangacollection:
def __init__(self):
        self.collection = [
            manga("Tatsuki Fujimoto", "Chainsaw Man", 1),
            manga("Gege Akutami", "Jujutsu kaisen", 2),
            manga("Kohei Horikawa", "Dr. Stone", 3),
            manga("Yuki Tanimoto", "Spy x Family", 4),
            manga("Masashi Kishimoto", "Naruto", 5),
            manga("kukushibo", "Demon slayer", 6),
            manga("Eiichiro Oda", "One Piece", 7),
            manga("Rei Torajirou", "Attack on Titan", 8)
        ]

    def show_manga_collection(self):
        print("\nYOUR MANGA COLLECTION")
        if not self.collection:
            print("Your collection is empty.")
        else:
            for index, manga in enumerate(self.collection):
                print(f"{index + 1}. {manga}")

    def Add_to_collection(self):
        print("\nADD NEW MANGA")
        title = input("Enter the manga's title: ").strip()
        author = input("Enter the author's name: ").strip()

        try:
            volume = int(input("Enter the volume number: ").strip())
            new_manga = manga(author, title, volume)
            self.collection.append(new_manga)
            print(f"Successfully added {new_manga} to your collection!")
        except ValueError:  
            print("Invalid input. Volume number must be an integer.")

    def search_manga(self):
        print("\nSEARCH MANGA")
        search_title = input("Enter the title of the manga to search: ").strip().lower()
        found_manga = [manga for manga in self.collection if search_title in manga.title.lower()]

        if found_manga:
            print("Found the following manga(s):")
            for manga in found_manga:
                print(manga)
        else:
            print("No manga found with that title.")

    def run(self):
        print("Welcome to the Manga Collection system")
        while True:
            print("\nMenu:")
            print("1. Show Manga Collection")
            print("2. Add New Manga")
            print("3. Search Manga")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                self.show_manga_collection()
            elif choice == '2':
                self.Add_to_collection()
            elif choice == '3':
                self.search_manga()
            elif choice == '4':
                print("Exiting the Manga Collection system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    manga_collection = mangacollection()
    manga_collection.run()

