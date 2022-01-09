from PIL import Image
import imageio
from pathlib import Path

RAW_IMAGE_PATH = Path(__file__).parent.parent / "assets"/"raw"/"images"
GOLD_IMAGE_PATH = Path(__file__).parent.parent / "assets"/"gold"/"images"
GOLD_GIF_PATH = Path(__file__).parent.parent / "assets"/"gold"/"gifs"

def resize_images():
    for source in RAW_IMAGE_PATH.glob("*.png"):
        target = GOLD_IMAGE_PATH/"1400px_wide"/source.name
        resize_width(source, target, width=1400)
        yield target

def create_gif(duration=1):
    images=[]
    for filename in resize_images():
        images.append(imageio.imread(filename))
    target = GOLD_GIF_PATH/"intro.gif"
    print(f"creating {target.name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    imageio.mimsave(target, images, duration=duration)

def resize_width(source: Path, target: Path, width=1400):
    print(f"resizing {source.name}")
    image = Image.open(source)
    height=int(image.height*width/image.width)
    heigth=850
    new_image = image.resize((width, height))
    new_image.save(target)
    

if __name__=="__main__":
    create_gif()