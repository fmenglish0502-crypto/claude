"""02편 '할머니를 밀친 여자의 최후' 자막 애니메이션 영상 만들기 (1080x1920, 30fps).

사용법: python3 make_karma.py <폰트폴더> <출력.mp4>
블록 캐릭터를 직접 그리고, 자막을 올리고, ffmpeg로 mp4를 만든다. 소리는 무음 트랙.
"""
import math
import os
import subprocess
import sys
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H, FPS = 1080, 1920, 30
FONT_DIR = sys.argv[1]
OUT = sys.argv[2]


@lru_cache(None)
def font(size, weight="Bold"):
    name = {"Bold": "NanumGothicBold.ttf", "XB": "NanumGothicExtraBold.ttf", "R": "NanumGothic.ttf"}[weight]
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


SKIN = (247, 214, 176)
CHARS = {
    "seoyeon": dict(hair=(70, 45, 30), style="short", shirt=(70, 130, 220), pants=(40, 40, 60)),
    "jimin": dict(hair=(20, 20, 25), style="long", shirt=(215, 40, 60), pants=(215, 40, 60), glasses=True, bag=True),
    "grandma": dict(hair=(200, 200, 205), style="bun", shirt=(130, 80, 170), pants=(90, 70, 110), cane=True),
    "p1": dict(hair=(40, 30, 20), style="short", shirt=(90, 160, 90), pants=(60, 60, 60)),
    "p2": dict(hair=(110, 60, 20), style="long", shirt=(240, 170, 60), pants=(70, 90, 140)),
    "p3": dict(hair=(30, 30, 30), style="short", shirt=(150, 150, 160), pants=(50, 50, 50)),
    "sec": dict(hair=(20, 20, 20), style="short", shirt=(35, 35, 45), pants=(35, 35, 45), tie=True),
}


def draw_face(d, expr):
    # 눈
    if expr == "shock":
        for ex in (230, 290):
            d.ellipse((ex - 16, 200, ex + 16, 232), fill="white", outline="black", width=3)
            d.ellipse((ex - 6, 210, ex + 6, 222), fill="black")
        d.ellipse((245, 250, 275, 285), fill=(60, 20, 20))
    else:
        for ex in (230, 290):
            d.ellipse((ex - 9, 207, ex + 9, 225), fill="black")
        if expr == "smile":
            d.arc((235, 235, 285, 275), 20, 160, fill="black", width=5)
        elif expr == "smirk":
            d.line((240, 260, 270, 260), fill="black", width=5)
            d.line((270, 260, 288, 248), fill="black", width=5)
        elif expr == "angry":
            d.line((212, 190, 245, 202), fill="black", width=6)
            d.line((308, 190, 275, 202), fill="black", width=6)
            d.arc((235, 255, 285, 290), 200, 340, fill="black", width=5)
        elif expr in ("sad", "sweat"):
            d.line((212, 200, 245, 190), fill="black", width=5)
            d.line((308, 200, 275, 190), fill="black", width=5)
            d.arc((238, 258, 282, 290), 200, 340, fill="black", width=5)
        elif expr == "calm":
            d.line((242, 262, 278, 262), fill="black", width=5)
        else:
            d.arc((240, 240, 280, 268), 20, 160, fill="black", width=4)
    if expr == "sweat":
        d.polygon([(345, 165), (333, 195), (357, 195)], fill=(90, 170, 255))
        d.ellipse((333, 185, 357, 209), fill=(90, 170, 255))


@lru_cache(None)
def char_img(name, pose="stand", expr="normal", phase=0):
    s = CHARS[name]
    im = Image.new("RGBA", (520, 760), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sw = int(28 * math.sin(phase / 8 * 2 * math.pi)) if pose == "walk" else 0
    # 다리
    d.polygon([(200, 525), (255, 525), (255 + sw, 740), (200 + sw, 740)], fill=s["pants"])
    d.polygon([(265, 525), (320, 525), (320 - sw, 740), (265 - sw, 740)], fill=s["pants"])
    d.rectangle((196 + sw, 725, 259 + sw, 745), fill=(30, 30, 30))
    d.rectangle((261 - sw, 725, 324 - sw, 745), fill=(30, 30, 30))
    # 팔
    arm = tuple(max(0, c - 25) for c in s["shirt"])
    if pose == "shock":
        d.rectangle((140, 160, 185, 335), fill=arm)
        d.rectangle((335, 160, 380, 335), fill=arm)
        d.rectangle((140, 140, 185, 175), fill=SKIN)
        d.rectangle((335, 140, 380, 175), fill=SKIN)
    else:
        d.rectangle((140, 325, 185, 505), fill=arm)
        d.rectangle((140, 490, 185, 525), fill=SKIN)
        if pose in ("point", "push"):
            d.rectangle((335, 330, 490, 378), fill=arm)
            d.rectangle((480, 330, 515, 378), fill=SKIN)
        elif pose == "phone":
            d.rectangle((335, 250, 380, 380), fill=arm)
            d.rectangle((328, 180, 392, 262), fill=(30, 30, 40), outline=(200, 200, 210), width=3)
        elif pose == "help":
            d.rectangle((335, 420, 470, 465), fill=arm)
            d.rectangle((460, 420, 500, 465), fill=SKIN)
        else:
            d.rectangle((335, 325, 380, 505), fill=arm)
            d.rectangle((335, 490, 380, 525), fill=SKIN)
    # 몸통
    d.rectangle((185, 320, 335, 535), fill=s["shirt"])
    if name == "grandma":
        d.rectangle((248, 320, 272, 535), fill=(225, 215, 235))
    if s.get("tie"):
        d.polygon([(253, 322), (267, 322), (272, 440), (260, 460), (248, 440)], fill=(190, 30, 40))
        d.polygon([(185, 320), (245, 320), (215, 420)], fill=(245, 245, 245))
    if s.get("bag"):
        d.line((150, 330, 135, 450), fill=(200, 160, 40), width=5)
        d.rectangle((95, 440, 175, 520), fill=(225, 185, 50), outline=(150, 110, 20), width=4)
    if s.get("cane") and pose not in ("shock",):
        d.line((372, 500, 400, 742), fill=(120, 75, 35), width=12)
    # 머리
    hc = s["hair"]
    if s["style"] == "long":
        d.rectangle((178, 160, 342, 380), fill=hc)
    d.rounded_rectangle((190, 150, 330, 300), radius=20, fill=SKIN)
    d.rectangle((182, 132, 338, 182), fill=hc)
    d.rectangle((182, 132, 200, 230), fill=hc)
    d.rectangle((320, 132, 338, 230), fill=hc)
    if s["style"] == "bun":
        d.ellipse((228, 82, 292, 142), fill=hc)
    draw_face(d, expr)
    if s.get("glasses") and expr != "shock":
        d.rectangle((208, 200, 252, 230), fill=(15, 15, 15))
        d.rectangle((268, 200, 312, 230), fill=(15, 15, 15))
        d.line((252, 212, 268, 212), fill=(15, 15, 15), width=5)
    if pose == "fall":
        im = im.rotate(80, expand=True, resample=Image.BICUBIC)
    return im


@lru_cache(None)
def char_final(name, pose, expr, phase, face_left, scale):
    im = char_img(name, pose, expr, phase)
    if face_left:
        im = ImageOps.mirror(im)
    if scale != 1:
        im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    return im


# ---------- 배경 ----------
def bg_busstop(d, t):
    d.rectangle((0, 0, W, 1150), fill=(150, 205, 245))
    d.ellipse((800, 120, 960, 280), fill=(255, 230, 120))
    for i, (x, w, h, c) in enumerate([(0, 220, 520, (190, 190, 200)), (230, 180, 640, (170, 175, 190)),
                                       (420, 260, 460, (200, 195, 185)), (690, 200, 700, (180, 185, 195)),
                                       (900, 180, 540, (195, 190, 200))]):
        d.rectangle((x, 1150 - h, x + w, 1150), fill=c)
        for wy in range(1150 - h + 40, 1130, 90):
            for wx in range(x + 25, x + w - 40, 60):
                d.rectangle((wx, wy, wx + 30, wy + 45), fill=(235, 240, 250))
    d.rectangle((0, 1150, W, 1450), fill=(205, 200, 190))
    d.rectangle((0, 1450, W, H), fill=(80, 80, 85))
    for x in range(0, W, 200):
        d.rectangle((x + 40, 1660, x + 140, 1680), fill=(240, 240, 240))
    d.rectangle((70, 850, 90, 1300), fill=(90, 90, 100))
    d.rounded_rectangle((20, 790, 200, 900), radius=14, fill=(40, 110, 200))
    d.text((110, 845), "버스", font=font(52, "XB"), fill="white", anchor="mm")


CUR_SC = {}


def bg_street(d, t):
    d.rectangle((0, 0, W, H), fill=(150, 205, 245))
    off = int(t * 1400) % 400
    for i in range(-1, 4):
        x = i * 400 - off
        d.rectangle((x, 500, x + 300, 1200), fill=(185, 185, 200))
    d.rectangle((0, 1200, W, H), fill=(80, 80, 85))
    for y in (300, 700, 1000, 1350):
        lx = (int(t * 2000) + y) % W
        d.line((lx, y, lx + 220, y), fill=(255, 255, 255), width=6)
    if not CUR_SC.get("clock", True):
        return
    d.rounded_rectangle((700, 330, 1000, 470), radius=20, fill=(255, 255, 255))
    d.text((850, 400), "09:58", font=font(80, "XB"), fill=(220, 40, 40), anchor="mm")


def bg_lobby(d, t):
    d.rectangle((0, 0, W, 1250), fill=(236, 226, 205))
    d.rectangle((0, 1250, W, H), fill=(170, 140, 110))
    d.rounded_rectangle((140, 480, 940, 640), radius=16, fill=(30, 60, 110))
    d.text((540, 560), LOBBY_TEXT, font=font(54, "XB"), fill="white", anchor="mm")
    for x in (60, 330, 600, 870):
        d.rectangle((x, 1180, x + 150, 1210), fill=(90, 70, 60))


def bg_room(d, t):
    d.rectangle((0, 0, W, 1250), fill=(225, 230, 236))
    d.rectangle((0, 1250, W, H), fill=(120, 110, 105))
    d.rectangle((90, 430, 470, 860), fill=(170, 210, 240), outline=(250, 250, 250), width=14)
    d.line((280, 430, 280, 860), fill=(250, 250, 250), width=10)
    d.rectangle((820, 620, 1020, 1250), fill=(140, 100, 70))
    d.ellipse((835, 950, 860, 975), fill=(230, 200, 90))
    d.text((540, 380), ROOM_TEXT, font=font(46, "XB"), fill=(90, 100, 120), anchor="mm")


def fg_table(d, t):
    d.rectangle((60, 1230, 1020, 1300), fill=(95, 70, 50))
    d.rectangle((90, 1300, 990, 1440), fill=(120, 90, 65))


def bg_dark(d, t):
    d.rectangle((0, 0, W, H), fill=(15, 15, 20))


def bg_office(d, t):
    d.rectangle((0, 0, W, 1250), fill=(232, 236, 240))
    d.rectangle((0, 1250, W, H), fill=(150, 150, 155))
    d.rounded_rectangle((300, 380, 780, 470), radius=14, fill=(30, 60, 110))
    d.text((540, 425), "한결그룹 마케팅팀", font=font(44, "XB"), fill="white", anchor="mm")
    for x in (40, 380, 720):
        d.rectangle((x + 60, 900, x + 260, 1040), fill=(40, 40, 50))
        d.rectangle((x + 75, 915, x + 245, 1025), fill=(120, 180, 230))
        d.rectangle((x + 145, 1040, x + 175, 1100), fill=(80, 80, 90))
        d.rectangle((x, 1100, x + 320, 1140), fill=(190, 160, 120))


def bg_night(d, t):
    d.rectangle((0, 0, W, H), fill=(25, 28, 50))
    d.rectangle((0, 1250, W, H), fill=(40, 35, 45))
    d.rectangle((640, 520, 980, 760), fill=(90, 200, 255))
    d.rectangle((700, 760, 920, 800), fill=(60, 60, 70))
    d.text((810, 640), CUR_SC.get("monitor", "편집중…"), font=font(44, "XB"), fill=(20, 30, 60), anchor="mm")
    d.polygon([(640, 760), (980, 760), (1080, 1250), (540, 1250)], fill=(45, 60, 95))


def bg_mansion(d, t):
    d.rectangle((0, 0, W, 1250), fill=(120, 30, 45))
    for x in range(0, W, 120):
        d.rectangle((x, 300, x + 8, 1250), fill=(150, 45, 60))
    d.rectangle((0, 1250, W, H), fill=(200, 170, 120))
    d.polygon([(380, 1250), (700, 1250), (820, H), (260, H)], fill=(170, 25, 40))
    d.line((540, 300, 540, 380), fill=(220, 190, 90), width=6)
    d.ellipse((400, 370, 680, 470), fill=(240, 210, 100))
    for i in range(7):
        x = 420 + i * 40
        d.polygon([(x, 465), (x + 14, 465), (x + 7, 505)], fill=(255, 245, 200))
    d.rounded_rectangle((290, 560, 790, 660), radius=16, fill=(250, 235, 200))
    d.text((540, 610), "회장님 팔순 생신 축하연", font=font(46, "XB"), fill=(120, 30, 45), anchor="mm")


BGS = {"mansion": bg_mansion, "bus": bg_busstop, "street": bg_street, "lobby": bg_lobby, "room": bg_room, "dark": bg_dark,
       "office": bg_office, "night": bg_night}


# ---------- 휴대폰 화면 ----------
def overlay_phone(d, kind, lt, sc=None):
    sc = sc or {}
    d.rounded_rectangle((220, 380, 860, 1320), radius=50, fill=(20, 20, 25), outline=(90, 90, 100), width=8)
    d.rounded_rectangle((250, 430, 830, 1280), radius=24, fill=(250, 250, 252))
    if kind == "views":
        d.rectangle((250, 430, 830, 780), fill=(60, 60, 70))
        d.polygon([(500, 540), (500, 680), (610, 610)], fill="white")
        d.text((270, 810), sc.get("feed_title", "할머니 밀친 학생 실화냐"), font=font(40, "XB"), fill="black")
        views = int(min(1, lt / 1.5) * sc.get("feed_views", 100000))
        d.text((270, 870), f"조회수 {views:,}회", font=font(36), fill=(120, 120, 120))
        for i, c in enumerate(sc.get("feed_comments", ["진짜 인성 무슨 일", "얼굴 다 나왔네 ㅋㅋ", "요즘 애들 무섭다"])):
            d.text((270, 960 + i * 90), "💬 " + c if False else "· " + c, font=font(36), fill=(60, 60, 60))
    elif kind == "blackbox":
        d.rectangle((250, 430, 830, 1280), fill=(30, 30, 30))
        d.text((540, 500), sc.get("bb_label", "● REC  버스 블랙박스  08:12"), font=font(34, "XB"), fill=(255, 70, 70), anchor="mm")
        im = Image.new("RGBA", (580, 700), (70, 75, 70, 255))
        bb = sc.get("bb_chars") or [("jimin", "push", "angry", False, 0.55, 20, 260), ("grandma", "fall", "shock", False, 0.5, 250, 440)]
        for (nm, po, ex, lf, scl, bx, by) in bb:
            im.alpha_composite(char_final(nm, po, ex, 0, lf, scl), (bx, by))
        dd = ImageDraw.Draw(im)
        dd.ellipse(sc.get("bb_circle", (40, 230, 320, 680)), outline=(255, 60, 60), width=10)
        d._image.paste(im.convert("RGB"), (250, 560))
    elif kind == "comments":
        d.text((270, 460), sc.get("comments_head", "댓글 12,483개"), font=font(40, "XB"), fill="black")
        cm = sc.get("comments", ["진짜 범인 따로 있었네", "학생 미안해요ㅠㅠ 오해했어요", "새치기녀 최종 탈락ㅋㅋㅋ",
                                 "회장님 레전드", "이게 인과응보지"])
        n = min(len(cm), int(lt / 0.6) + 1)
        for i in range(n):
            y = 540 + i * 140
            d.rounded_rectangle((270, y, 810, y + 115), radius=20, fill=(238, 240, 245))
            d.text((295, y + 57), cm[i], font=font(36), fill=(30, 30, 30), anchor="lm")
            d.text((780, y + 57), "♥", font=font(36), fill=(240, 60, 90), anchor="rm")
    elif kind == "live":  # 라이브 방송 화면: 방송하는 사람 + 실시간 채팅
        d.rectangle((250, 430, 830, 1280), fill=(35, 35, 45))
        who = sc.get("live_char", "jimin")
        im = char_final(who, "point", sc.get("live_expr", "angry"), 0, False, 0.75)
        d._image.paste(im, (540 - im.width // 2, 1000 - im.height), im)
        d.rounded_rectangle((270, 450, 380, 500), radius=10, fill=(230, 30, 50))
        d.text((325, 475), "LIVE", font=font(32, "XB"), fill="white", anchor="mm")
        d.text((400, 475), f"👁 {int(300 + lt * 900):,}" if False else f"시청 {int(300 + lt * 900):,}명",
               font=font(30, "XB"), fill="white", anchor="lm")
        chat = sc.get("chat", [])
        n = min(len(chat), int(lt / 0.5) + 1)
        for i, c in enumerate(chat[max(0, n - 4):n]):
            y = 1010 + i * 64
            d.rounded_rectangle((265, y, 815, y + 54), radius=14, fill=(0, 0, 0, 0) if False else (60, 60, 75))
            d.text((285, y + 27), c, font=font(32, "XB"), fill="white", anchor="lm")
    elif kind == "necklace":  # 가방 속에서 나온 목걸이
        d.rectangle((250, 430, 830, 1280), fill=(245, 240, 230))
        d.rounded_rectangle((330, 760, 750, 1160), radius=40, fill=(60, 110, 200), outline=(30, 60, 130), width=8)
        d.arc((420, 640, 660, 880), 180, 360, fill=(30, 60, 130), width=14)
        k = min(1, lt / 0.6)
        cy = int(900 - 260 * k)
        for i in range(14):
            a = math.pi * (0.1 + 0.8 * i / 13)
            x = 540 + int(150 * math.cos(a))
            y = cy + int(150 * math.sin(a)) - 150
            d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=(230, 240, 255), outline=(150, 170, 220), width=3)
        d.polygon([(540, cy + 30), (575, cy + 80), (540, cy + 140), (505, cy + 80)], fill=(120, 200, 255), outline=(255, 255, 255))
        if int(lt * 6) % 2:
            d.text((610, cy + 40), "✦", font=font(60, "XB"), fill=(255, 230, 120))
        d.text((540, 520), "가방 안에서 나온 것은…", font=font(40, "XB"), fill=(40, 40, 40), anchor="mm")
    elif kind == "post":  # 커뮤니티 폭로글
        d.rectangle((250, 430, 830, 520), fill=(40, 90, 200))
        d.text((540, 475), sc.get("post_site", "직장인 커뮤니티"), font=font(36, "XB"), fill="white", anchor="mm")
        f = font(42, "XB")
        y = 560
        for ln in wrap(sc.get("post_title", ""), f, 540):
            d.text((275, y), ln, font=f, fill=(20, 20, 20))
            y += 58
        d.text((275, y + 10), sc.get("post_meta", ""), font=font(30), fill=(130, 130, 130))
        y += 80
        for ln in sc.get("post_body", []):
            for l2 in wrap(ln, font(34), 540):
                d.text((275, y), l2, font=font(34), fill=(50, 50, 50))
                y += 50
        if sc.get("post_likes"):
            likes = int(min(1, lt / 1.2) * sc["post_likes"])
            d.text((275, 1220), f"추천 {likes:,}   댓글 {likes // 3:,}", font=font(34, "XB"), fill=(220, 50, 60))


# ---------- 자막 ----------
def wrap(text, f, maxw):
    lines, cur = [], ""
    for word in text.split(" "):
        test = (cur + " " + word).strip()
        if f.getlength(test) <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def caption(d, speaker, text, lt):
    f = font(66, "XB")
    lines = wrap(text, f, 920)
    lh = 86
    top = 1560 - (len(lines) * lh) // 2
    pop = min(1.0, lt / 0.12)
    narr = speaker is None
    color = (255, 236, 90) if narr else (255, 255, 255)
    if speaker:
        chip = font(44, "XB")
        tw = chip.getlength(speaker)
        cx0 = 540 - tw / 2 - 30
        d.rounded_rectangle((cx0, top - 95, cx0 + tw + 60, top - 22), radius=30, fill=SPK_COLOR.get(speaker, (60, 60, 70)))
        d.text((540, top - 58), speaker, font=chip, fill="white", anchor="mm")
    for i, ln in enumerate(lines):
        y = top + i * lh + int((1 - pop) * 20)
        d.text((540, y + lh // 2), ln, font=f, fill=color, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))


SPK_COLOR = {"지민": (200, 40, 60), "서연": (50, 110, 210), "할머니": (120, 70, 160), "회장": (120, 70, 160),
             "비서": (40, 40, 50), "팀장": (90, 90, 100), "사모님": (30, 30, 35), "태준": (40, 90, 70), "경찰": (30, 50, 110)}
TITLE = ("할머니를 밀친 여자의", "충격적인 최후")
LOBBY_TEXT = "한결그룹 최종 면접 대기실"
ROOM_TEXT = "면접실"
END = ("다음 편", "지민의 복수?", "팔로우하고 다음 편 보기")


def title_bar(d, t):
    d.rectangle((0, 0, W, 300), fill=(0, 0, 0))
    d.text((540, 120), TITLE[0], font=font(70, "XB"), fill="white", anchor="mm")
    d.text((540, 215), TITLE[1], font=font(84, "XB"), fill=(255, 60, 60), anchor="mm")


# ---------- 장면 ----------
# 캐릭터: (이름, x, 발y, 크기, 포즈, 표정, 왼쪽보기, 움직임)
S = [
    dict(dur=3.6, bg="bus", chars=[("seoyeon", 540, 1430, 1.0, "stand", "smile", False, "bob")],
         lines=[(None, "오늘은 내 인생 첫 대기업 최종 면접날.")]),
    dict(dur=3.8, bg="bus", chars=[("seoyeon", 760, 1430, 0.95, "stand", "normal", True, "bob"),
                                   ("grandma", 360, 1430, 0.9, "walk", "normal", False, ("slide", -200))],
         lines=[(None, "짐이 무거워 보이는 할머니 한 분이 줄을 서 계셨다.")]),
    dict(dur=4.0, bg="bus", chars=[("grandma", 420, 1430, 0.9, "stand", "shock", False, "shake"),
                                   ("jimin", 160, 1430, 1.0, "push", "angry", False, ("slide", -400)),
                                   ("seoyeon", 830, 1430, 0.95, "stand", "shock", True, None)],
         lines=[("지민", "늙으면 집에나 있지. 비켜요!")]),
    dict(dur=3.0, bg="bus", chars=[("grandma", 380, 1460, 0.9, "fall", "sad", False, None),
                                   ("jimin", 160, 1430, 1.0, "stand", "smirk", False, None),
                                   ("seoyeon", 760, 1430, 0.95, "help", "shock", True, ("slide", 250))],
         lines=[("서연", "할머니! 괜찮으세요?!")]),
    dict(dur=3.6, bg="bus", zoom=(1.0, 1.12), chars=[("jimin", 300, 1430, 1.05, "point", "angry", False, "shake"),
                                                      ("seoyeon", 800, 1430, 0.95, "stand", "shock", True, None)],
         lines=[("지민", "어머! 저 학생이 할머니 밀었어요!!")]),
    dict(dur=5.4, bg="bus", chars=[("p1", 150, 1450, 0.85, "phone", "angry", False, "bob"),
                                   ("p2", 380, 1470, 0.85, "phone", "angry", False, "bob"),
                                   ("p3", 610, 1450, 0.85, "point", "angry", False, "shake"),
                                   ("seoyeon", 900, 1430, 0.95, "stand", "sweat", True, "shake")],
         lines=[("행인1", "요즘 애들 진짜 왜 저래?"), ("행인2", "찍어 찍어, 인터넷에 올려."), ("서연", "제가 안 그랬어요…!")]),
    dict(dur=3.2, bg="bus", bus=True, chars=[("jimin", 620, 1430, 1.0, "walk", "smirk", False, ("slide", -300))],
         lines=[(None, "진짜 범인은 유유히 버스에 올라탔다.")]),
    dict(dur=5.6, bg="bus", chars=[("grandma", 330, 1430, 0.9, "stand", "smile", False, "bob"),
                                   ("seoyeon", 740, 1430, 0.95, "stand", "smile", True, "bob")],
         lines=[("할머니", "학생, 면접 가는 길 아니었어요? 이름이 뭐예요?"), ("서연", "서연이요. 괜찮아요, 할머니가 먼저예요.")]),
    dict(dur=3.2, bg="street", chars=[("seoyeon", 540, 1600, 1.0, "walk", "sweat", False, "run")],
         lines=[(None, "할머니를 병원에 모셔다드리고, 겨우 도착한 면접장.")]),
    dict(dur=4.4, bg="lobby", phone="views", chars=[],
         lines=[("지민", "어? 할머니 민 애 아니야? ㅋㅋ 너 지금 조회수 10만이야.")]),
    dict(dur=4.2, bg="lobby", chars=[("p1", 200, 1430, 0.85, "stand", "shock", False, None),
                                     ("p2", 430, 1430, 0.85, "stand", "smirk", False, None),
                                     ("jimin", 660, 1430, 0.9, "phone", "smirk", False, "bob"),
                                     ("seoyeon", 900, 1430, 0.9, "stand", "sad", True, None)],
         lines=[("지원자1", "저 사람이야?"), ("지원자2", "헐… 대박.")]),
    dict(dur=3.0, bg="room", fg=True, chars=[("sec", 880, 1250, 0.85, "stand", "calm", True, None),
                                              ("jimin", 300, 1250, 0.85, "stand", "smirk", False, None),
                                              ("seoyeon", 560, 1250, 0.85, "stand", "normal", False, None)],
         lines=[("비서", "회장님 들어오십니다.")]),
    dict(dur=3.4, bg="room", fg=True, flash=True, zoom=(1.0, 1.15),
         chars=[("grandma", 900, 1250, 0.9, "walk", "calm", True, ("slide", 200)),
                ("jimin", 300, 1250, 0.85, "shock", "shock", False, "shake"),
                ("seoyeon", 560, 1250, 0.85, "stand", "shock", False, None)],
         lines=[("지민", "…!!!")]),
    dict(dur=5.0, bg="room", fg=True, chars=[("grandma", 820, 1250, 0.95, "stand", "calm", True, None),
                                              ("jimin", 300, 1250, 0.85, "stand", "sweat", False, "shake")],
         lines=[("회장", "아까 정류장에서 뵀죠?"), ("회장", "\"늙으면 집에나 있지\"… 맞죠?")]),
    dict(dur=5.6, bg="room", phone="blackbox", lt_split=0.45, chars=[],
         lines=[("지민", "회, 회장님… 그건 저 학생이…"), ("회장", "버스 블랙박스, 다 봤어요.")]),
    dict(dur=3.2, bg="room", fg=True, zoom=(1.05, 1.15), chars=[("grandma", 760, 1250, 1.0, "point", "angry", True, None),
                                                                   ("jimin", 300, 1250, 0.85, "stand", "sad", False, ("slide", 0))],
         lines=[("회장", "지민 씨는 나가주세요.")]),
    dict(dur=6.4, bg="room", fg=True, chars=[("grandma", 760, 1250, 0.95, "stand", "smile", True, "bob"),
                                              ("seoyeon", 330, 1250, 0.9, "stand", "shock", False, None)],
         lines=[("회장", "넘어진 사람 일으켜 세우는 사람. 그게 우리 회사 인재상이에요."),
                ("회장", "서연 씨, 내일부터 출근해요.")]),
    dict(dur=4.6, bg="lobby", phone="comments", chars=[],
         lines=[(None, "다음 날, 그 영상의 댓글은 완전히 뒤집혔다.")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]


# 다른 편: EP=episodes/epXX.py 로 장면·제목·엔딩을 바꿔 끼운다.
if os.environ.get("EP"):
    import importlib.util

    _spec = importlib.util.spec_from_file_location("episode", os.environ["EP"])
    _ep = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_ep)
    CHARS.update(getattr(_ep, "CHARS", {}))
    S, TITLE, END = _ep.S, _ep.TITLE, _ep.END
    LOBBY_TEXT = getattr(_ep, "LOBBY_TEXT", LOBBY_TEXT)
    ROOM_TEXT = getattr(_ep, "ROOM_TEXT", ROOM_TEXT)


def render_scene(sc, lt):
    CUR_SC.clear()
    CUR_SC.update(sc)
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    BGS[sc["bg"]](d, lt)
    if sc.get("bus"):
        bx = int(-900 + min(1, lt / 1.2) * 1000)
        d.rounded_rectangle((bx, 900, bx + 900, 1420), radius=40, fill=(60, 170, 90))
        for wx in range(bx + 60, bx + 860, 170):
            d.rectangle((wx, 960, wx + 130, 1130), fill=(200, 230, 250))
        d.ellipse((bx + 120, 1340, bx + 260, 1480), fill=(30, 30, 30))
        d.ellipse((bx + 640, 1340, bx + 780, 1480), fill=(30, 30, 30))
    for (name, x, fy, sc_, pose, expr, left, anim) in sc["chars"]:
        phase = int(lt * 16) % 8 if pose == "walk" else 0
        im = char_final(name, pose, expr, phase, left, sc_)
        dx, dy = 0, 0
        if anim == "bob":
            dy = int(6 * math.sin(lt * 5))
        elif anim == "shake":
            dx = int(9 * math.sin(lt * 60))
        elif anim == "run":
            dy = int(14 * abs(math.sin(lt * 10)))
        elif isinstance(anim, tuple) and anim[0] == "slide":
            k = min(1, lt / 0.6)
            dx = int(anim[1] * (1 - k) ** 2)
        px = x - im.width // 2 + dx
        py = fy - im.height - dy
        img.paste(im, (px, py), im)
    if sc.get("fg"):
        fg_table(d, lt)
    if sc.get("phone"):
        overlay_phone(d, sc["phone"], lt, sc)
    if sc.get("end"):
        d.text((540, 820), END[0], font=font(70, "XB"), fill=(200, 200, 200), anchor="mm")
        d.text((540, 960), END[1], font=font(110 if len(END[1]) < 9 else 80, "XB"), fill=(255, 60, 60), anchor="mm")
        d.text((540, 1180), END[2], font=font(56, "XB"), fill="white", anchor="mm")
    z = sc.get("zoom")
    if z:
        k = z[0] + (z[1] - z[0]) * min(1, lt / sc["dur"])
        cw, ch = int(W / k), int(H / k)
        x0, y0 = (W - cw) // 2, (H - ch) // 2
        img = img.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)
        d = ImageDraw.Draw(img)
    if sc.get("sepia"):  # 회상 장면
        g = img.convert("L")
        img = Image.merge("RGB", (g.point(lambda v: min(255, int(v * 1.08 + 20))), g.point(lambda v: int(v * 0.95 + 10)),
                                  g.point(lambda v: int(v * 0.75))))
        d = ImageDraw.Draw(img)
    if sc.get("flash") and lt < 0.25:
        img = Image.blend(img, Image.new("RGB", (W, H), "white"), 1 - lt / 0.25)
        d = ImageDraw.Draw(img)
    lines = sc["lines"]
    if lines and sc.get("starts"):
        idx = max(i for i, s in enumerate(sc["starts"]) if s <= lt)
        spk, txt = lines[idx]
        caption(d, spk, txt, lt - sc["starts"][idx])
    elif lines:
        split = sc.get("lt_split")
        if split and len(lines) == 2:
            idx = 0 if lt < sc["dur"] * split else 1
            start = 0 if idx == 0 else sc["dur"] * split
        else:
            seg = sc["dur"] / len(lines)
            idx = min(len(lines) - 1, int(lt / seg))
            start = idx * seg
        spk, txt = lines[idx]
        caption(d, spk, txt, lt - start)
    title_bar(d, lt)
    return img


def apply_voice(vdir):
    """녹음 길이에 맞춰 장면·자막 시간을 다시 잡고, 대사를 한 줄로 이어 붙인 wav를 만든다."""
    import json
    import wave

    import numpy as np

    timing = json.load(open(f"{vdir}/timing.json"))
    sr = 44100
    clips = []  # (시작초, 파일)
    t0 = 0.0
    for si, sc in enumerate(S):
        if sc["lines"]:
            starts, cur = [], 0.25
            for li in range(len(sc["lines"])):
                key = f"{si}_{li}"
                starts.append(cur if li else 0.0)
                if key in timing:
                    clips.append((t0 + max(cur if li else 0.25, 0.0), f"{vdir}/{key}.wav"))
                    cur += timing[key] + 0.35
                else:
                    cur += 2.6
            sc["starts"] = starts
            sc["dur"] = max(cur + 0.25, 2.0)
        if sc.get("flash"):
            clips.append((t0, "BOOM"))
        t0 += sc["dur"]
    mix = np.zeros(int((t0 + 1) * sr), dtype=np.float32)
    for st, path in clips:
        if path == "BOOM":  # 반전 효과음: 낮은 '둥'
            n = int(1.6 * sr)
            tt = np.arange(n) / sr
            clip = 0.6 * np.sin(2 * np.pi * 48 * tt) * np.exp(-tt * 2.2)
        else:
            with wave.open(path) as w:
                rate = w.getframerate()
                clip = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32767
            if rate != sr:
                clip = np.interp(np.arange(int(len(clip) * sr / rate)) * rate / sr, np.arange(len(clip)), clip)
        a = int(st * sr)
        mix[a:a + len(clip)] += clip[: len(mix) - a]
    mix = np.clip(mix / max(1.0, np.abs(mix).max() / 0.95), -1, 1)
    out = f"{vdir}/mix.wav"
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    return out


def main():
    import os

    vdir = os.environ.get("VOICE_DIR")
    audio = ["-i", apply_voice(vdir)] if vdir else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
    total = sum(s["dur"] for s in S)
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
         "-i", "-", *audio, "-shortest",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
    for sc in S:
        n = int(round(sc["dur"] * FPS))
        for i in range(n):
            ff.stdin.write(render_scene(sc, i / FPS).tobytes())
    ff.stdin.close()
    ff.wait()
    print(f"done {total:.1f}s -> {OUT}")


if __name__ == "__main__":
    if len(sys.argv) > 3:  # 미리보기: 장면 번호 목록 → PNG
        for k in sys.argv[3].split(","):
            sc = S[int(k)]
            render_scene(sc, sc["dur"] * 0.6).save(f"{OUT}_{k}.png")
    else:
        main()
