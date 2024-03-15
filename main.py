import ui
import bookmarks
import api_manager


def main():

    # You will need some kind of menu so user can choose to search or view bookmarks, 
    # They will also need to select whether they wish to save a set of results or not 

    # Get user's search query 
    search_term = ui.get_search_term()

    results = api_manager.perform_search(search_term)

    ui.display_results(results)

    bookmarks.add_new_bookmark(search_term, results)

    # If user wants to see all results, 
    all_results = bookmarks.get_all_bookmarks()

    # Create and call ui module function to display all results 
    


if __name__ == '__main__':
    main()