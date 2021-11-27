from pytube import YouTube
link = input('enter the link')
print('Downloading....')
YouTube(link).streams.first().download()
print('Video Downloaded successfully')