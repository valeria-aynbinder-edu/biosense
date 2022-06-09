from ebook_hw.ebook import EBook

if __name__ == '__main__':
    ebook = EBook('../files/data/alice_in_wonderland.txt', 100)
    print("------------------------------")
    print(f"Pages number: {ebook.get_pages_num()}")
    print("------------------------------")
    print(f"Page 20 content:\n\n{ebook.get_page_content(20)}")
    print("------------------------------")
    ebook.add_bookmark(47, "bookmark_47")
    print("------------------------------")
    ebook.add_bookmark(50, "the best")
    print("------------------------------")
    ebook.add_bookmark(50, "another best")
    print("------------------------------")
    ebook.add_bookmark(100, "my bookkmark")
    print("------------------------------")
    ebook.display_bookmarks()
    print("------------------------------")
    ebook.delete_bookmark_by_name("bookmark_47")
    print("------------------------------")
    ebook.display_bookmarks()
    print("------------------------------")
    ebook.delete_bookmarks_for_page(50)
    print("------------------------------")
    ebook.display_bookmarks()
    print("------------------------------")
    ebook.get_bookmark_by_name("my bookkmark")



