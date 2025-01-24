# Comments-downloader
### YouTube offers a Data API for accessing video details including comments.

## Steps for extracting youtube comments:
### 1. Get an API key:
#### Visit Google Cloud Console
#### Create a project and enable the YouTube Data API v3
#### Generate an API Key
### 2.Use the API:
#### Use the commentThreads endpoint to get video comments.

#### Ensure VIDEO_ID corresponds to valid YouTube video.
#### VIDEO_ID is the part of the video URL after v=
#### Example: URL: https://wwww.youtube.com/watch?v=abcdefghijk
#### VIDEO_ID: abcdefghij
#### Ensure your API key has the correct permissions for the youtube data API v3.
#### Check if you've reached the quota for API usage.

## Steps for extracting facebook post comments:
### 1.Set up a facebook app:
#### Go to Facebook Developers and create an app to obtain an App ID and App Secret.
#### Request the necessary permissions.
### 2. Get an access token:
#### Generate a user or page access token.
### 3. Use the graph API:
#### Use the /post-id/comments endpoint to retrieve comments.

#### Ensure you have the correct permissions(user_posts or page_read_engagement).
#### If the post is on a facebook page, ensure your app has access to the page and pages_read_engagement permission.
