from pytube import Playlist
from pytube.cli import on_progress
import os


url = input('Введите ссылку: ')

playlist = Playlist(url)
title = playlist.title

count = 0

for video in playlist.videos:
    video.register_on_progress_callback(on_progress)

    d_streams = video.streams.get_highest_resolution()
    d_streams.download(output_path= f'{title}')

    v_title = d_streams.default_filename

    file = f'{title}/{v_title}'
    os.rename(file,f'{title}/New{count} {video.title}')
    print(f'Downloded {video.title}')

    count += 1