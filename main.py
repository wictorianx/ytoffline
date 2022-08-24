import pytube
import os
from pytube import YouTube,Playlist

tempLink = "https://www.youtube.com/watch?v=Q4Y1lAhnOVY"

def main():
    pass
    #mp3download("https://www.youtube.com/watch?v=Q4Y1lAhnOVY","D:\\")
    
def mp3download(link,destination):
    yt = YouTube(link)
    sound = yt.streams.filter(only_audio=True).first()
    out_file = sound.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
def mp4download(link, destination):
    yt = YouTube(link)
    sound = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    out_file = sound.download(output_path=destination)
    print(yt.title + " has been successfully downloaded.")
def downloadSubtitle(link,destination, languages):
    subs = destination+"\\Subs"
    os.makedirs(subs)
    yt = YouTube(link)
    title = yt.title
    captions=[]
    for lan in languages:
        caption = yt.captions.get_by_language_code(lan)
        captions.append(caption.generate_srt_captions)
        os.makedirs(subs+"\\{lan}")
    for i in range(len(captions)):
        with open(f"{subs}\\{languages[0]}\\{title}.txt", "x") as file:
            file.write(captions[0])
def manageP(playlistLink,mp3,mp4,subs,destination,languages):
    p = Playlist(playlistLink)
    for url in p.video_urls:
        if mp3:
            mp3download(url,destination)
        if mp4:
            mp3download(url,destination)
        if subs:
            downloadSubtitle(url,destination,languages)
def manageV(url,mp3,mp4,subs,destination,languages):
    p = YouTube(url)
    if mp3:
        mp3download(url,destination)
    if mp4:
        mp3download(url,destination)
    if subs:
        downloadSubtitle(url,destination,languages)
main()

