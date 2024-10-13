from pytube import Search

# Prompt the user to enter the search query
search_query = input("Enter the search query: ")

# Create a Search object
search = Search(search_query)

# Get the search results
search_results = search.results

# Print the video information for each result
for video in search_results:
    print("Title:", getattr(video, 'title', 'Not available'))
    print("URL:", getattr(video, 'watch_url', 'Not available'))
    print("Author:", getattr(video, 'author', 'Not available'))
    
    # Duration
    duration = None
    try:
        duration = int(getattr(video, 'length', 0))
        duration = str(duration) + " seconds"
    except (TypeError, ValueError):
        duration = "Not available"
    print("Duration:", duration)
    
    # Views
    views = None
    try:
        views = int(getattr(video, 'views', 0))
        views = str(views)
    except (TypeError, ValueError):
        views = "Not available"
    print("Views:", views)
    
    # Rating
    rating = getattr(video, 'rating', 'Not available')
    if rating != 'Not available':
        rating = str(rating)
    print("Rating:", rating)
    
    # Thumbnail URL
    thumbnail_url = getattr(video, 'thumbnail_url', 'Not available')
    if thumbnail_url != 'Not available':
        thumbnail_url = str(thumbnail_url)
    print("Thumbnail URL:", thumbnail_url)
    
    # Description
    description = getattr(video, 'description', 'Not available')
    if description != 'Not available':
        description = str(description)
    print("Description:", description)
    print("---")