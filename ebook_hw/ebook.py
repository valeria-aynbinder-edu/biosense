class EBook:

    def __init__(self, book_path, words_per_page):
        self.book_path = book_path
        self.words_per_page = words_per_page
        self.pages = []
        self.bookmarks = {}

        self.load_book()

    def load_book(self):
        with open(self.book_path) as f:
            content = f.read()

        split_by_words = content.split(" ")

        first_word_idx = 0
        for last_word_idx in range(self.words_per_page, len(split_by_words), self.words_per_page):
            self.pages.append(" ".join(split_by_words[first_word_idx:last_word_idx]))
            first_word_idx = last_word_idx

    def get_pages_num(self):
        return len(self.pages)

    def get_page_content(self, page_num):
        if page_num > len(self.pages):
            print(f"Page number {page_num} does not exist")
        else:
            return self.pages[page_num]

    def add_bookmark(self, page_num, name):
        if page_num > len(self.pages):
            print(f"Page number {page_num} does not exist")
        self.bookmarks[name] = page_num
        print(f"Added bookmark {name} for page {page_num}")

    def display_bookmarks(self):
        print(f"You have {len(self.bookmarks)} bookmarks:")
        print("\n".join([f"{name}: page {page}" for name, page in self.bookmarks.items()]))

    def delete_bookmark_by_name(self, name):
        if name not in self.bookmarks:
            print(f"Bookmark {name} does not exist")
        else:
            page_num = self.bookmarks.pop(name)
            print(f"Bookmark {name} for page {page_num} was successfully deleted")

    def delete_bookmarks_for_page(self, page_num):
        names_to_delete = []
        for name, page in self.bookmarks.items():
            if page == page_num:
                names_to_delete.append(name)
        for name in names_to_delete:
            self.bookmarks.pop(name)

        print(f"Deleted the following bookmarks for page {page_num}: {names_to_delete}")

    def get_bookmark_by_name(self, name):
        if name not in self.bookmarks:
            print(f"Bookmark with name {name} does not exist")
        else:
            print(f"Bookmark {name} for page {self.bookmarks[name]}")
