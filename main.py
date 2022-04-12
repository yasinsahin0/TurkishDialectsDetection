# from mutagen.mp3 import MP3
# audio = MP3("sound_download/azerbaycan/25_azerbaycan.mp4")
# print(audio.info.length)
#
# from __future__ import unicode_literals
# import youtube_dl
#
# link = "https://youtu.be/MRXCesWUUTY"
#
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
# }
#
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([link])