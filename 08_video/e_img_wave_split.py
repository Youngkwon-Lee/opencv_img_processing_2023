from moviepy.editor import VideoFileClip


def separate_audio_and_video(video_filename):
    clip = VideoFileClip(video_filename)

    # 비디오만 있는 새 파일 생성
    clip.without_audio().write_videofile("res_mp4/video_only.mp4")

    # 오디오만 있는 새 파일 생성
    clip.audio.write_audiofile("res_mp4/audio_only.wav")


# 'people_dancing.mp4' 파일에서 영상과 소리를 분리
separate_audio_and_video("img/people_dancing.mp4")
