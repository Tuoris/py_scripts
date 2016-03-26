import csv
import urllib
from json import loads
from urllib import request

def main():
    # You can get an access token following instructions on
    # https://developers.google.com/youtube/v3/getting-started
    secret_key = "YOUR_ACCESS_TOKEN"
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
    except urllib.error.URLError as e:
        import sys
        print("Error ocured: %s" % e.reason)
        print("Closing...")
        sys.exit()

def process(rawResp):
    """Return a dictionary recieved from response."""
    # TODO handle gzip response  
    data = rawResp.read()
    data = data.decode(rawResp.headers.get_content_charset(), "ignore")
    data_dict = loads(data)
    return data_dict

def send_request(url):
    r = request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", 
        })
    return urllib.request.urlopen(r) 
    
def get_video_ids(playlistId, secret):
    """Return ids of all video from playlist."""
    all_video_ids = []
    playlistAPICall = ("https://www.googleapis.com/youtube/v3/playlistItems?"
                       "part=contentDetails&playlistId={}&key={}&pageToken={}")
    
    resp = send_request(playlistAPICall.format(playlistId, secret, ""))
    data = process(resp)
    nextPageToken = data.get("nextPageToken", "")
    while nextPageToken:
        for item in data["items"]:
            all_video_ids.append(item["contentDetails"]["videoId"])
        
        nextPageToken = data.get("nextPageToken", "")
        resp = send_request(playlistAPICall.format(playlistId, secret, nextPageToken))
        data = process(resp)
    
    return all_video_ids

def get_info(videoId, secret):
    """Return tuple that contains video title, number of views and likes."""

    videoAPICall = ("https://www.googleapis.com/youtube/v3/videos?id={}&part=statistics,snippet&"
                   "fields=items%28id,snippet/title,statistics%28viewCount,likeCount%29%29&key={}")
    resp = send_request(videoAPICall.format(videoId, secret))
    
    data = process(resp)
    item = data["items"][0]
    title = item["snippet"]["title"]
    
    viewCount = item["statistics"].get("viewCount", 0)
    likeCount = item["statistics"].get("likeCount", 0)
    
    return (title, viewCount, likeCount)

if __name__ == '__main__':
    main()