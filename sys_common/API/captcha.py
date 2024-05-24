from captcha.image import ImageCaptcha
from PIL import Image
from random import choices
from io import BytesIO

from django.http import HttpResponse


def gen_captcha(content="012345689"):
    """生成验证码"""
    image = ImageCaptcha()
    # 获取字符串
    captcha_text = "".join(choices(content, k=4)).lower()
    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image


# 返回png图片
def make_captcha(request):
    code, image = gen_captcha()
    print(code, image)
    out = BytesIO()
    request.session["code"] = code
    image.save(out, "png")
    out.seek(0)
    return HttpResponse(out.read(), content_type="image/png")
