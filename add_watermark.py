import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import uuid


def get_file_path_with_type(file_path, file_type):
    file_paths = []
    root_dir = os.walk(file_path)

    for sub_dir, folder_name, file_list in root_dir:
        for file_name in file_list:
            file_path = os.path.join(sub_dir, file_name)
            if file_type in file_path:
                file_paths.append(file_path)
    file_paths = sorted(file_paths)
    return file_paths


if __name__ == "__main__":
    src_folder = 'xxxxx'

    img_paths = get_file_path_with_type(src_folder, '.JPG')

    for im in img_paths:
        src = Image.open(im).convert('RGBA')
        mask = Image.new('RGBA', src.size, (0, 0, 0, 0))
        """ set font """
        font = ImageFont.truetype('c:/windows/Fonts/msyh.ttc', 25)
        rst = ImageDraw.Draw(mask)
        rst.text((int(mask.size[0] / 2) - 50,
                  mask.size[1] - 60),
                 "©shelly", font=font,
                 fill=(192, 192, 192, 192))
        dst = Image.alpha_composite(src, mask)
        name = str(uuid.uuid4()) + '.png'
        path = os.path.join(src_folder, name)
        dst.save(path)
