"""그림체 시험: AI 실사 이미지 한 장면 (LCM_Dreamshaper_v7, MIT 라이선스, CPU에서 실행).

사용법: HF_HUB_DISABLE_XET=1 python3 style_test_ai.py <폰트폴더> <출력.png>
AI로 그림을 만든 뒤 기존 영상과 같은 제목·자막을 얹는다.
"""
import sys
import time

import torch
from diffusers import DiffusionPipeline
from PIL import Image, ImageDraw, ImageFont

FONT_DIR, OUT = sys.argv[1], sys.argv[2]
torch.set_num_threads(4)

PROMPT = ("realistic photo, angry korean man in his 40s, short black hair, black leather jacket, gold necklace, "
          "shouting and pointing out of the driver side window of a red car, city road traffic in daytime, "
          "dramatic expression, cinematic lighting, sharp focus, high detail")

pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7", safety_checker=None,
                                         requires_safety_checker=False, torch_dtype=torch.float32)
pipe.set_progress_bar_config(disable=True)
t = time.time()
g = torch.Generator().manual_seed(7)
art = pipe(PROMPT, num_inference_steps=6, guidance_scale=8.0, width=512, height=768, generator=g).images[0]
print(f"generated in {time.time() - t:.0f}s")
art.save(OUT.replace(".png", "-raw.png"))

# 1080x1920 세로 화면: 그림을 1080 폭으로 키워서 가운데 배치(위아래는 제목·자막 자리)
W, H = 1080, 1920
canvas = Image.new("RGB", (W, H), (15, 15, 20))
art_big = art.resize((1080, 1620), Image.LANCZOS)
canvas.paste(art_big, (0, 300))
d = ImageDraw.Draw(canvas)


def f(sz, name="NanumGothicExtraBold.ttf"):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", sz)


d.rectangle((0, 0, W, 300), fill=(0, 0, 0))
d.text((540, 120), "매일 클락션 울리던 보복운전러", font=f(62), fill="white", anchor="mm")
d.text((540, 215), "결국 임자 만났다", font=f(84), fill=(255, 60, 60), anchor="mm")
d.rounded_rectangle((470, 1610, 610, 1680), radius=30, fill=(200, 40, 40))
d.text((540, 1645), "강상철", font=f(42), fill="white", anchor="mm")
d.text((540, 1750), "야! 운전 그따위로 할 거면 집에 있어!", font=f(58), fill="white", anchor="mm",
       stroke_width=8, stroke_fill=(0, 0, 0))
d.text((540, 1880), "[그림체 시험 B: AI 실사 이미지]", font=f(32, "NanumGothicBold.ttf"), fill=(220, 220, 220),
       anchor="mm", stroke_width=3, stroke_fill=(0, 0, 0))
canvas.save(OUT)
print("saved", OUT)
