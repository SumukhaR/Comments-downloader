# Comments-downloader
### YouTube offers a Data API for accessing video details including comments.

## Steps:
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