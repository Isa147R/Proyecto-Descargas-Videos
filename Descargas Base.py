from pytube import YouTube

def descargar_video(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()

if __name__ == '__main__':
    enlace_youtube = input("Ingrese el enlace de YouTube: ")
    descargar_video(enlace_youtube)
