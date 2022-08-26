import pytube
import os
from pytube import YouTube,Playlist
import codecs

tempLink = "https://www.youtube.com/watch?v=Q4Y1lAhnOVY"
tempLink = "https://www.youtube.com/watch?v=PRSoRkM8GcM"
def main():
    pass
    #mp3download("https://www.youtube.com/watch?v=Q4Y1lAhnOVY","D:\\")
    
def mp3download(link,destination):
    print(link)
    yt = YouTube(link)
    sound = yt.streams.filter(only_audio=True).first()
    out_file = sound.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
    #message?
def mp4download(link, destination):
    yt = YouTube(link)
    sound = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    out_file = sound.download(output_path=destination)
    print(yt.title + " has been successfully downloaded.")
    #message
def downloadSubtitle(link,destination, languages):
    subs = destination+"\\Subs"
    if not os.path.isdir(subs):
        os.makedirs(subs)
    yt = YouTube(link)
    title = yt.title
    captions=[]
    for lan in languages:
        caption = yt.captions.get_by_language_code(lan)
        captions.append(caption.generate_srt_captions())
        print(caption.generate_srt_captions())
        os.makedirs(subs+f"\\{lan}")
    for i in range(len(captions)):
        with codecs.open(f"{subs}\\{languages[i]}\\{title}.srt", "x",encoding="utf-8") as file:
            try:
                file.write(captions[i])
            except:
                print("codec")
def manageP(playlistLink,mp3,mp4,subs,destination,languages):
    p = Playlist(playlistLink)
    for url in p.video_urls:
        if mp3:
            mp3download(url,destination)
        if mp4:
            mp4download(url,destination)
        if subs:
            downloadSubtitle(url,destination,languages)
def manageV(url,mp3,mp4,subs,destination,languages):
    p = YouTube(url)
    if mp3:
        mp3download(url,destination)
    if mp4:
        mp4download(url,destination)
    if subs:
        downloadSubtitle(url,destination,languages)
def convertUrlToChannelUrl(url):
    yt = YouTube(url)
    return(url.channel_url)
def manageF(playlistLink,mp3,mp4,subs,destination,languages,interval):
    #interval = [min,max]
    p = Playlist(playlistLink)
    vids = p.video_urls
    for i in range(len(interval)):
        interval[i]=interval[i]-1
    i0,i1 = interval[0],interval[1]
    url = i0
    while(i0 <= url and url <= i1):
        if url > i1:
            break
        if mp3:
            mp3download(vids[url],destination)
        if mp4:
            mp4download(vids[url],destination)
        if subs:
            downloadSubtitle(vids[url],destination,languages)
        url+=1

  
#manageF("https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg",True,False,False,"D:\\tests",[],[34,34])
