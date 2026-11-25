"""그림체 시험: 웹툰풍 한 장면 (보복운전 빌런이 창문 밖으로 소리치는 장면). 코드로 직접 그림.

사용법: python3 style_test_webtoon.py <폰트폴더> <출력.png>
"""
import math
import random
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_DIR, OUT = sys.argv[1], sys.argv[2]
SS = 2  # 2배로 그린 뒤 줄여서 테두리를 부드럽게
W, H = 1080 * SS, 1920 * SS
LINE = (25, 20, 25)
SKIN, SKIN_SH = (246, 208, 178), (222, 172, 140)


def f(size, w="XB"):
    name = {"XB": "NanumGothicExtraBold.ttf", "B": "NanumGothicBold.ttf"}[w]
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size * SS)


def S(*v):
    return tuple(int(x * SS) for x in v)


img = Image.new("RGB", (W, H), (120, 170, 225))
d = ImageDraw.Draw(img)

# --- 배경: 하늘, 도로, 속도선 ---
for y in range(0, 1250):
    k = y / 1250
    d.line(S(0, y, 1080, y), fill=(int(110 + 90 * k), int(165 + 60 * k), int(230 + 15 * k)))
d.rectangle(S(0, 900, 1080, 1920), fill=(70, 72, 80))
for i in range(6):
    x = 540 + (i - 2.5) * 260
    d.polygon(S(x - 8, 900, x + 8, 900, x * 1.6 - 330 + 25, 1920, x * 1.6 - 330 - 25, 1920), fill=(235, 235, 235))
random.seed(3)
for _ in range(60):
    y = random.randint(320, 1500)
    x = random.randint(-200, 1080)
    d.line(S(x, y, x + random.randint(120, 400), y), fill=(255, 255, 255), width=SS * random.randint(2, 5))
# 뒤차(피해 차량) 실루엣
d.rounded_rectangle(S(700, 760, 1060, 960), radius=40 * SS, fill=(235, 235, 240), outline=LINE, width=4 * SS)
d.rectangle(S(740, 790, 1020, 860), fill=(150, 190, 220), outline=LINE, width=3 * SS)

# --- 운전석 창문 프레임 (빌런 차) ---
d.rounded_rectangle(S(-60, 560, 760, 1560), radius=60 * SS, fill=(20, 20, 28), outline=LINE, width=8 * SS)
d.rounded_rectangle(S(-20, 600, 720, 1500), radius=40 * SS, fill=(40, 42, 55))
d.polygon(S(-60, 1560, 760, 1560, 900, 1920, -60, 1920), fill=(170, 20, 30), outline=LINE)
d.line(S(-60, 1560, 760, 1560), fill=LINE, width=8 * SS)

# --- 빌런 (상반신) ---
cx, cy = 360, 900  # 얼굴 중심
# 몸통(검은 가죽 재킷) + 금목걸이
d.polygon(S(130, 1500, 590, 1500, 560, 1170, 470, 1110, 250, 1110, 160, 1170), fill=(35, 35, 40), outline=LINE, width=6 * SS)
d.polygon(S(300, 1110, 420, 1110, 400, 1230, 320, 1230), fill=(250, 250, 250), outline=LINE, width=4 * SS)
d.arc(S(290, 1100, 430, 1260), 20, 160, fill=(230, 185, 40), width=10 * SS)
# 목
d.rectangle(S(315, 1040, 405, 1130), fill=SKIN_SH, outline=LINE, width=5 * SS)
# 얼굴 (턱선 있는 형태)
face = S(250, 740, 470, 760, 488, 900, 470, 1010, 400, 1075, 320, 1075, 250, 1010, 232, 900)
d.polygon(face, fill=SKIN, outline=LINE, width=6 * SS)
d.polygon(S(430, 760, 470, 760, 488, 900, 470, 1010, 420, 1060, 440, 900), fill=SKIN_SH)
# 귀
d.ellipse(S(212, 870, 252, 950), fill=SKIN, outline=LINE, width=5 * SS)
# 머리 (짧은 투블럭, 위로 뻗친)
hair = [(240, 830), (230, 740), (262, 680), (300, 655), (330, 630), (360, 650), (395, 620), (420, 655), (460, 650),
        (480, 700), (490, 790), (470, 760), (440, 720), (380, 735), (320, 720), (270, 760), (252, 830)]
d.polygon([(x * SS, y * SS) for x, y in hair], fill=(30, 25, 25), outline=LINE)
for x0 in (300, 345, 395, 440):
    d.line(S(x0, 680, x0 + 15, 725), fill=(80, 75, 80), width=3 * SS)
# 화난 눈썹, 눈, 핏줄
d.polygon(S(265, 845, 345, 870, 345, 885, 262, 862), fill=LINE)
d.polygon(S(455, 845, 375, 870, 375, 885, 458, 862), fill=LINE)
for ex in (305, 415):
    d.ellipse(S(ex - 32, 888, ex + 32, 925), fill="white", outline=LINE, width=4 * SS)
    d.ellipse(S(ex - 14, 892, ex + 10, 922), fill=(60, 35, 25))
    d.ellipse(S(ex - 8, 896, ex - 2, 904), fill="white")
d.line(S(360, 900, 350, 975, 372, 978), fill=SKIN_SH, width=5 * SS, joint="curve")
for a in range(4):  # 💢 핏줄 표시
    ang = a * math.pi / 2 + math.pi / 4
    x, y = 470 + 22 * math.cos(ang), 720 + 22 * math.sin(ang)
    d.arc(S(x - 18, y - 18, x + 18, y + 18), math.degrees(ang) + 90, math.degrees(ang) + 270, fill=(230, 40, 50), width=6 * SS)
# 소리치는 입
d.polygon(S(305, 995, 415, 995, 400, 1045, 320, 1045), fill=(110, 25, 35), outline=LINE, width=5 * SS)
d.rectangle(S(315, 997, 405, 1010), fill="white")
d.ellipse(S(335, 1022, 385, 1044), fill=(210, 90, 100))
# 창밖으로 내민 팔 + 삿대질
d.polygon(S(520, 1250, 590, 1200, 830, 1080, 860, 1140, 640, 1300, 560, 1330), fill=(35, 35, 40), outline=LINE, width=6 * SS)
d.ellipse(S(820, 1050, 920, 1150), fill=SKIN, outline=LINE, width=6 * SS)
d.polygon(S(900, 1080, 1010, 1040, 1020, 1070, 912, 1110), fill=SKIN, outline=LINE, width=5 * SS)

# --- 효과음 ---
for txt, x, y, sz, rot in [("빵!!", 800, 560, 120, 12), ("빵빵빵!!!", 640, 420, 90, -8)]:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text(S(x, y), txt, font=f(sz), fill=(255, 220, 40), anchor="mm", stroke_width=10 * SS, stroke_fill=LINE)
    img.paste(layer.rotate(rot, center=S(x, y)), (0, 0), layer.rotate(rot, center=S(x, y)))
d = ImageDraw.Draw(img)

# --- 상단 제목 + 자막 (기존 영상과 같은 형식) ---
d.rectangle(S(0, 0, 1080, 300), fill=(0, 0, 0))
d.text(S(540, 120), "매일 클락션 울리던 보복운전러", font=f(62), fill="white", anchor="mm")
d.text(S(540, 215), "결국 임자 만났다", font=f(84), fill=(255, 60, 60), anchor="mm")
d.rounded_rectangle(S(470, 1610, 610, 1680), radius=30 * SS, fill=(200, 40, 40))
d.text(S(540, 1645), "강상철", font=f(42), fill="white", anchor="mm")
d.text(S(540, 1750), "야! 운전 그따위로 할 거면 집에 있어!", font=f(58), fill="white", anchor="mm",
       stroke_width=8 * SS, stroke_fill=(0, 0, 0))
d.text(S(540, 1880), "[그림체 시험 A: 웹툰풍]", font=f(32, "B"), fill=(200, 200, 200), anchor="mm")

img = img.resize((1080, 1920), Image.LANCZOS)
img.save(OUT)
print("saved", OUT)
