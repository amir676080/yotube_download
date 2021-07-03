from pytube import YouTube

link =input("enter link: ")
url =YouTube(link)
print("downloading....")
video = url.streams.first( )
video.download( )
print("end")