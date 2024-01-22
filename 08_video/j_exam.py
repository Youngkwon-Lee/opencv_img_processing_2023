from moviepy.editor import *

clip1  = VideoFileClip("img/cat.mp4")
print(clip1 , type(clip1))
duration = clip1.duration
width, height  = clip1.size
fps  = clip1.fps
#n_frames  = clip1.nframes
print(f'동영상의 길이 : {duration }')
print(f'동영상의 해상도 : {width } ,{ height}')
print(f'동영상의 프레임율 : {fps }프레임/초 ')
#print(f'동영상의 전체 프레임수  : {n_frames }')

audio  = clip1.audio
print(f'audio 길이 : {audio.fps } HZ, { audio.nchannels}')

#동영상을 시간별로 잘라서 연결해보자.
clip1  = VideoFileClip("img/cat.mp4").subclip(0,2)
clip2  = VideoFileClip("img/cat.mp4").subclip(4,5)
clip3  = VideoFileClip("img/cat.mp4").subclip(10,11)
final=  concatenate_videoclips([clip1,clip2,clip3])
final.write_videofile('res_mp4/final_cat.mp4')