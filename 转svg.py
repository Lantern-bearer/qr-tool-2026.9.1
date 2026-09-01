from PIL import Image
import qrcode
import os
from pyzbar.pyzbar import decode
from qrcode.image.svg import SvgImage

script_dir = os.path.dirname(os.path.abspath(__file__))
# os.path.abspath() 的作用是：把传入的路径转换成绝对路径。
# 绝大多数情况下 __file__ 已经是绝对路径了，但万一你以相对路径方式运行脚本（比如 python ../script.py），它会把相对路径补齐成完整路径，确保后续操作不出错。
save_path1 = os.path.join(script_dir, "svg二维码导出", "001.svg")

# 确保文件夹存在（如果不存在就创建）
os.makedirs(os.path.dirname(save_path1), exist_ok=True)


print(script_dir)
img = qrcode.make("这是一段文字，它被用于理解二维码如何将信息编进矩阵",image_factory=SvgImage)
img.save(save_path1)




