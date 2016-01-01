import json
from urllib import request

def api(method_name, **kargs):
    url_t = "http://api.vk.com/method/{0}?{1}&v=5.4"
    ins_params = []
    for param in kargs:
        ins_params.append(str(param) + "=" + str(kargs[param]))
    return url_t.format(method_name, "&".join(ins_params))

def get(g_request):
    data = request.urlopen(g_request).read().decode(errors="ignore")
    return json.loads(data)

def get_albums(uid):
    albums_req = api("photos.getAlbums", owner_id=uid)
    albums = get(albums_req)
    albums = albums["response"]["items"]
    result = []
    for album in albums:
        result.append(album["id"])
    return result

def get_photos(uid, album):
    photos_req = api("photos.get", owner_id=uid, album_id=album)
    photos = get(photos_req)
    photos = photos["response"]["items"]
    result = []
    for photo in photos:
        result.append(photo["id"])
    return result

def form_links(links):
    w_link = ""
    link_template = "<a href=\"{0}\">{1}</a>"
    for link in links:
        w_link += link_template.format(link[0], link[1]) + "<br>"
    return w_link

def main():
    uid = 1
    albums_ids = get_albums(uid)
    print(albums_ids)
    albums_ids += ["wall", "profile", "saved"]
    ofile = open("links.html", "w")
    for album in albums_ids:
        photos = get_photos(uid, album)
        template = "http://vk.com/photo{0}_{1}"

        formatted = []
        for photo in photos:
            formatted.append((template.format(uid, photo), photo))
            #print(template.format(uid, photo))

        ofile.write(form_links(formatted))
        
    ofile.close()


if __name__ == '__main__':
    main()