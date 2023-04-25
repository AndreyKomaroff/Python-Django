from pytube import YouTube
from pytube.cli import on_progress

video = YouTube(input('Введите ссылку: '))

video.register_on_progress_callback(on_progress)

d_streams = video.streams.get_highest_resolution()
d_streams.download(output_path= f'{123}')

v_title = d_streams.default_filename

file = v_title