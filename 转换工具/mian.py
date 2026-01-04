import os

import resvg_py
import io
from PIL import Image


input_path = r"./input"
output_path = r"./output"

def tran_img_to_ico(image_name):
    try:
        img = Image.open(os.path.join(input_path,image_name))
        
        if img.mode != "RGBA":
            img = img.convert('RGBA')

        icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        image_name = image_name.split(".")[0]

        img.save(os.path.join(output_path,(image_name + ".ico")),format="ICO",sizes=icon_sizes)
        print(f"成功转换: {os.path.join(input_path,image_name)} -> {os.path.join(output_path,(image_name + ".ico"))}")

    except Exception as e:
        print(f"转换失败: {e}")

def tran_svg_to_ico(svg_name):
    try:
        with open(os.path.join(input_path,svg_name),"rb") as f:
            svg_data = f.read()

        png_data = resvg_py.svg_to_bytes(svg_data, width=256)
        img_buffer = io.BytesIO(png_data)
        img = Image.open(img_buffer)

        if img.mode != "RGBA":
            img = img.convert('RGBA')

        icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]

        svg_name = svg_name.split(".")[0]

        img.save(os.path.join(output_path,(svg_name + ".ico")),format="ICO",sizes=icon_sizes)
        print(f"成功转换: {os.path.join(input_path,svg_name)} -> {os.path.join(output_path,(svg_name + ".ico"))}")

        
    except Exception as e:
        print(f"转换失败: {e}")

image_list = os.listdir("./input")
for image in image_list:
    print(image)
file_name = input("输入想要转换的图片:")
if ".svg" in file_name:
    tran_svg_to_ico(file_name)
else:    
    tran_img_to_ico(file_name)
        
