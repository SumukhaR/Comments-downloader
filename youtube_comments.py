import requests
import csv

API_KEY = 'your_api_key'
VIDEO_ID = 'your_video_id'
URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

def get_youtube_comments():
    params = {
        'part': 'snippet',
        'videoId': VIDEO_ID,
        'key': API_KEY,
        'maxResults': 50
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
# change file name according to the comments you are trying to extract
def save_comments_to_csv(comments, filename="youtube_comments.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(["Comment", "Author", "Published At"])
        for item in comments['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            writer.writerow([comment, author, published_at])


comments = get_youtube_comments()
if comments:

    save_comments_to_csv(comments)
    print("Comments saved")
