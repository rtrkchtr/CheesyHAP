import subprocess
class check():
    def check_if_ffmpeg_is_installed():
        try:
            x = subprocess.check_output(["ffmpeg", "-version"])
            print(x)
            return True
        except:
            print("ffmpeg is not installed on your computer")
            return False



