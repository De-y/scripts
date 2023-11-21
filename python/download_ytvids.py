from pytube import YouTube as yt
from ffmpeg import FFmpeg, Progress
import os, shutil

def video_download(videos: list, directory: str, create_directory: bool, convert_to_mp3: bool):
    """
        Download YouTube videos and be able to convert them to mp3 or leave as mp4 in directory.
    """
    print("Recieved Signal!")
    if create_directory == True:
        print("Attempting to make a dedicated directory.")
        try:
            shutil.rmtree(directory)
            os.mkdir(directory)
            print("Successfully removed already-existing directory & changed to dedicated directory.")
        except:
            try:
                os.mkdir(directory)
                print("Made the directory.")
            except:
                pass
        os.chdir(directory)
    else:
        os.chdir(directory)

    print("Downloading videos.")
    for video in videos:
        yt(video).streams.filter(progressive=True, file_extension='mp4').first().download()
        print(f'Download for video using link {video} done!')
    print("Download finished, thinking about whether or not to convert them to mp3's.")
    if convert_to_mp3 == True:
        files = os.listdir()
        for file in files:
            print(f"Converting to mp3 for file {file}")
            ffmpeg = (
                FFmpeg()
                .option("y")
                .input(file)
                .output(
                    file[0:-4] + '.mp3',
                )
            )
            ffmpeg.execute()
            os.remove(file)
            print(f"Converted for file {file}, now it is {file[0:-4]}.mp3!")
    os.chdir(os.curdir)
    print("Finished!")
    
if __name__ == '__main__':
    videos = ["VIDEOS HERE"]
    video_download(videos=videos, directory='mp3_assets', create_directory=True, convert_to_mp3=True)
