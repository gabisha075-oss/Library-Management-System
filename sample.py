class Library:

    def __init__(self):
        self.books = []                     # list of books available in library
        self.students = {}                  # {student_id : [list of borrowed books]}
        self.issued_file = "issued_books.txt"

        # load issued books from file
        self.load_issued_books()

    # ---------------- LOAD FILE ----------------
    def load_issued_books(self):
        try:
            with open(self.issued_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        student_id, book = line.split("|")
                        if student_id not in self.students:
                            self.students[student_id] = []
                        self.students[student_id].append(book)
        except FileNotFoundError:
            open(self.issued_file, "w").close()

    # ---------------- SAVE FILE ----------------
    def save_issued_books(self):
        with open(self.issued_file, "w") as f:
            for student_id, book_list in self.students.items():
                for book in book_list:
                    f.write(f"{student_id},{book}\n")

    # ---------------- ADD BOOK ----------------
    def add_book(self):
        book = input("Enter Book Name: ").strip()

        if book in self.books:
            print("❌ Book already exists!")
            return

        self.books.append(book)
        print("📚 Book Added Successfully!")

    # ---------------- DISPLAY AVAILABLE BOOKS ----------------
    def display_books(self):
        if not self.books:
            print("No available books.")
            return

        print("\n📚 Available Books:")
        for b in self.books:
            print("-", b)

    # ---------------- DISPLAY ISSUED BOOKS ----------------
    def issued_books(self):
        if not self.students:
            print("No books issued yet.")
            return

        print("\n📕 Issued Books:")

        for sid, books in self.students.items():
            print(f"Student {sid} → {books}")

    # ---------------- BORROW BOOK ----------------
    def borrow_book(self):
        student_id = input("Enter student ID: ")
        book = input("Enter book name to borrow: ")

        if book not in self.books:
            print("❌ Book is not available in library!")
            return

        # Issue book
        self.books.remove(book)

        if student_id not in self.students:
            self.students[student_id] = []

        # prevent duplicate issue
        if book in self.students[student_id]:
            print("❌ Student already issued this book!")
            return

        self.students[student_id].append(book)
        self.save_issued_books()
        print("✅ Book issued successfully!")

    # ---------------- RETURN BOOK ----------------
    def return_book(self):
        student_id = input("Enter student ID: ")
        book = input("Enter book name to return: ")

        if student_id not in self.students:
            print("❌ This student has not issued any books.")
            return

        if book not in self.students[student_id]:
            print("❌ This book is NOT issued to this student!")
            return

        # return book
        self.students[student_id].remove(book)
        self.books.append(book)
        self.save_issued_books()

        print("✅ Book returned successfully!")


# ================= MENU ================
lib = Library()

while True:
    print("\n------ Library Management System ------")
    print("1. Add New Book")
    print("2. Display Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Issued Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        lib.add_book()
    elif choice == '2':
        lib.display_books()
    elif choice == '3':
        lib.borrow_book()
    elif choice == '4':
        lib.return_book()
    elif choice == '5':
        lib.issued_books()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")


