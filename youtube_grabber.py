import csv
import urllib
from json import loads
from urllib import request

def main():
    # You can get an access token following instructions on
    # https://developers.google.com/youtube/v3/getting-started
    secret_key = "AIzaSyChB1p2qpkNp7Q9wkp_fV4ra-kFO8vVorY"
    # secret_key = "YOUR_ACCESS_TOKEN"
    # Playlist that contains lectures collection of Programming Paradigms of Stanford University 
    playlist_id = "PL9D558D49CA734A02"
    
    print("Getting all video ids from playlist %s..." % playlist_id)
    try:
        video_ids = get_video_ids(playlist_id, secret_key)

        video_data = [("Lecture", "Views", "Likes")]
        print("Getting videos info...")
        for videoId in video_ids:
            video_data.append(get_info(videoId, secret_key))
        print("Complete.")
        with open("data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for item in video_data:
                print("%10s | %7s | %5s" % item)
                writer.writerow(item)
    except urllib.error.URLError:
        import sys
        print("Can't connect to www.youtube.com...")
        print("Closing.")
        sys.exit()

def process(rawResp):
    """Return a dictionary recieced from response."""
    data = rawResp.read().decode("utf-8")
    data_dict = loads(data)
    return data_dict
    
def get_video_ids(playlistId, secret):
    """Return ids of all video from playlist."""
    all_video_ids = []
    playlistAPICall = ("https://www.googleapis.com/youtube/v3/playlistItems?"
                       "part=contentDetails&playlistId={}&key={}&pageToken={}")
    
    resp = request.urlopen(playlistAPICall.format(playlistId, secret, ""))    
    data = process(resp)
    nextPageToken = data.get("nextPageToken", "")
    while nextPageToken:
        for item in data["items"]:
            all_video_ids.append(item["contentDetails"]["videoId"])
        
        nextPageToken = data.get("nextPageToken", "")
        resp = request.urlopen(playlistAPICall.format(playlistId, secret, nextPageToken))
        data = process(resp)
    
    return all_video_ids

def get_info(videoId, secret):
    """Return tuple that contains video title, number of views and likes."""
    videoAPICall = ("https://www.googleapis.com/youtube/v3/videos?id={}&part=statistics,snippet&"
                   "fields=items%28id,snippet/title,statistics%28viewCount,likeCount%29%29&key={}")
    resp = request.urlopen(videoAPICall.format(videoId, secret))
    
    data = process(resp)
    item = data["items"][0]
    title = item["snippet"]["title"][8:10].strip()
    viewCount = item["statistics"]["viewCount"]
    likeCount = item["statistics"]["likeCount"]
    
    return (title, viewCount, likeCount)

if __name__ == '__main__':
    main()