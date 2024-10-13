from pytube import YouTube

# Specify the URL of the YouTube video
url = "https://www.youtube.com/watch?v=HJJaxdt6k0A"

# Create a YouTube object
yt = YouTube(url)

# Get the video title
print("Title:", yt.title)

# Get the video author
print("Author:", yt.author)

# Get the video length (in seconds)
print("Duration:", yt.length, "seconds")

# Get the number of views
print("Views:", yt.views)

# Get the rating
print("Rating:", yt.rating)

# Get the thumbnail URL
print("Thumbnail URL:", yt.thumbnail_url)

# Get the video descriptions
print("Description:", yt.description)