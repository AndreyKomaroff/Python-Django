import moviepy.editor as mp 
  
video = mp.VideoFileClip("./123/Música Relajante para Dormir Desde Rio Manso en la Noche de Luna.mp4") 
audio = video.audio 
audio.write_audiofile("myaudio.mp3")