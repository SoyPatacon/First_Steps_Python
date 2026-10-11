import yt_dlp

url = input("Ingrese la URL del video de YouTube: ")
opciones = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

try:
    print ("Iniciando descarga mi vida")
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
    print ("Tu descarga está lista cabrón.")
except Exception as e:
    print(f"Error al descargar el video: {e}")