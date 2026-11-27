"""만약에 시뮬레이션 「7일 뒤 대정전」 4부: 창고 밑 저장고를 벙커로, 비축품 숨기기, 피난민과 나눌 것인가. 지어낸 가상 시나리오.
5부 떡밥: 할아버지 저장고 벽 뒤의 오래된 철문.
게시 제목 안: "정전 7일째 밤, 할아버지가 창고 바닥을 뜯자 나온 것"
"""

STYLE = "sim"
PHOTO_MODEL = "dreamshaper"
PHOTO_STYLE = ("flat design vector art illustration, adobe illustrator, 2d motion graphics animation still, bold flat colors, "
               "dark navy blue and warm orange palette, simple geometric shapes, cel shading, clean lines, detailed background, no text")
TITLE = ("", "")

ME = "a young korean man in his 20s with short black hair and a dark navy hoodie, simple flat cartoon character"
GP = "an old korean grandfather in his 70s with short white hair, tanned wrinkled face, brown work vest, simple flat cartoon character"
HOUSE = "a traditional korean countryside house with a tiled roof, stone wall, persimmon tree, mountains behind"


def P(prompt, line, dur=2.6, **kw):
    """장면 하나 = 그림 한 장(또는 여러 장) + 해설 한 줄."""
    photos = prompt if isinstance(prompt, list) else [prompt]
    return dict(dur=dur, photos=photos, lines=[("해설", line)], **kw)

PART = ("7일 뒤 대정전", "4부")
END = ("5부 예고", "할아버지가 숨긴 철문의 비밀?", "팔로우하고 다음 편 보기")

S = [
    P("silhouettes of several people with flashlights at a stone wall gate at night, tense", "[정전 6일] 밤. 대문 밖에 사람들이 서 있습니다.", 3.0),
    P("dark farmhouse at night, a hand turning off a lantern behind a paper window, no people visible", "할아버지가 [불]부터 끕니다.", 2.6),
    P(f"{GP} whispering to {ME} in a dark farmhouse room, finger on lips", "\"우리 집에 [먹을 게] 있는 걸 알면 안 된다.\"", 3.0),
    P(f"{GP} lifting old wooden floor boards inside a barn, revealing a dark hole with a ladder, lantern light", "할아버지가 창고 바닥을 [뜯습니다].", 2.8, flash=True),
    P("old underground earthen cellar with wooden beams, shelves and jars, lit by one lantern, no people", "옛날 [김치 저장고]. 땅속 2미터.", 2.8),
    P(f"{ME} carrying boxes of food down a ladder into an underground cellar, lantern light", "비축품을 [반으로] 나눠 숨깁니다.", 2.8),
    P("plastic pipe sticking out of the ground next to a barn, air vent, simple, no people", "[환기구]는 꼭 뚫어 둡니다.", 2.6),
    P("small gas camping stove crossed out with a red x inside a dark cellar, warning infographic, no people", "밀폐된 곳에서 [불]은 절대 안 됩니다.", 2.8),
    P("heavy wooden door with a thick iron bar lock inside an old barn, no people", "문은 [안에서] 잠그게 고칩니다.", 2.6),
    P(f"{ME} and {GP} sitting in an underground cellar with supplies on shelves, lantern light, quiet", "이제 이곳이 우리의 [벙커]입니다.", 2.8),
    P("knocking hand on an old wooden gate at dawn, no faces visible", "[정전 7일] 새벽. 누군가 문을 두드립니다.", 2.8, flash=True),
    P("tired young korean mother holding a small child at a farmhouse gate at dawn, pleading face", "아이를 안은 [엄마]입니다.", 2.6),
    P("close-up of a small child's face, pale, tired eyes, wrapped in a scarf", "\"애가 이틀째 [물]을 못 마셨어요.\"", 3.0),
    P(f"{ME} standing behind the gate, conflicted face, holding a water bottle", "당신이라면 [문]을 열겠습니까?", 2.8),
    P(f"{GP} opening the gate and handing two water bottles and rice to the mother, dawn light", "할아버지는 [문]을 엽니다.", 2.6),
    P(f"{GP} talking kindly to the mother, pointing toward the village hall, warm morning light", "\"[나누는] 집이 오래 버티는 법이다.\"", 3.0),
    P("village hall yard in the morning, villagers bringing pots, firewood and water barrels together", "마을 회관에 [공동 부엌]이 차려집니다.", 2.8),
    P("villagers taking turns guarding the village entrance with flashlights at night, organized", "밤엔 [돌아가며] 마을을 지킵니다.", 2.8),
    P("a crowd of people sharing hot soup at long tables outdoors, warm atmosphere", "혼자 숨은 집보다 [함께]가 셌습니다.", 2.8),
    P(f"{ME} going down into the cellar alone at night with a lantern to check supplies", "그날 밤, 당신은 저장고를 [정리]하다가", 2.8, flash=True),
    P("old cellar earthen wall with a few bricks fallen out, revealing a rusty iron surface behind, lantern light", "흙벽 뒤에서 [쇳소리]를 듣습니다.", 2.8),
    P("rusty old iron door hidden behind a crumbling earthen wall in a cellar, mysterious, dramatic lantern light", "벽 뒤에 숨겨진 [철문].", 2.8),
    P(f"{GP} standing at the top of the ladder looking down into the cellar, serious shadowed face", "할아버지가 말합니다. \"그건… [아직] 열면 안 된다.\"", 3.4),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
