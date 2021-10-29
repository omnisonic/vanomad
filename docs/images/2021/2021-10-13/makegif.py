#https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
import glob

from PIL import Image


def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.JPG")]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
               save_all=True, duration=1000, loop=0)
    

if __name__ == "__main__":
    make_gif("./van")