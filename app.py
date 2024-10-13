from flask import Flask, render_template, request, jsonify
from pytube import Search

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    search = Search(search_query)
    search_results = search.results
    
    videos = []
    for video in search_results:
        video_info = {
            'title': getattr(video, 'title', 'Not available'),
            'url': getattr(video, 'watch_url', 'Not available'),
            'author': getattr(video, 'author', 'Not available'),
            'duration': get_duration(video),
            'views': get_views(video),
            'rating': getattr(video, 'rating', 'Not available'),
            'thumbnail_url': getattr(video, 'thumbnail_url', 'Not available'),
            'description': getattr(video, 'description', 'Not available')
        }
        videos.append(video_info)
    
    return jsonify(videos)

def get_duration(video):
    try:
        duration = int(getattr(video, 'length', 0))
        return str(duration) + " seconds"
    except (TypeError, ValueError):
        return "Not available"

def get_views(video):
    try:
        views = int(getattr(video, 'views', 0))
        return str(views)
    except (TypeError, ValueError):
        return "Not available"

if __name__ == '__main__':
    app.run(debug=True)