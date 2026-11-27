"""만약에 시뮬레이션 「7일 뒤 대정전」 2부: 정전 첫날~사흘. 도시는 엘리베이터·수돗물·통신·카드가 멈추고, 시골은 우물·장작으로 버틴다. 지어낸 가상 시나리오.
게시 제목 안: "전기가 끊긴 지 3일, 도시 아파트에서 가장 먼저 멈춘 것"
"""

STYLE = "sim"
PHOTO_MODEL = "dreamshaper"
PHOTO_STYLE = "cute 2d cartoon animated movie still, single frame, big round eyes, simple faces, bold outlines, flat colors, wide shot, detailed background"
TITLE = ("", "")

ME = "cartoon young korean man with big round eyes, black hair, navy hoodie"
GP = "cartoon korean grandpa with big round eyes, white hair, brown vest"
HOUSE = "a traditional korean countryside house with a tiled roof, stone wall, persimmon tree, mountains behind"


def P(prompt, line, dur=2.6, **kw):
    """장면 하나 = 그림 한 장(또는 여러 장) + 해설 한 줄."""
    photos = prompt if isinstance(prompt, list) else [prompt]
    return dict(dur=dur, photos=photos, lines=[("해설", line)], **kw)

PART = ("7일 뒤 대정전", "2부")
END = ("3부 예고", "변기 물이 안 내려간다", "팔로우하고 다음 편 보기")

S = [
    P("pitch black korean countryside village at night under a sky full of stars, no lights anywhere", "[정전 1시간]. 사방이 깜깜합니다.", 2.8),
    P(f"{ME} lighting a camping lantern on a wooden table in a dark farmhouse room, warm glow", "당신은 [랜턴]부터 켭니다.", 2.6),
    P("close-up of a hand holding a glowing smartphone in the dark, screen full of chat message bubbles, no faces", "서울 친구들 단톡방이 [불]납니다.", 2.6),
    P("tall seoul apartment complex at night, completely dark, a few flashlight beams in windows", "도시의 고층 아파트.", 2.6),
    P("dark apartment stairwell, tired people climbing stairs with flashlights and water bottles", "[엘리베이터]가 멈췄습니다. 25층까지 계단.", 3.0),
    P("close-up of a kitchen faucet turned on with no water coming out, dark kitchen, no people", "그리고 [수돗물]도 끊깁니다.", 2.6),
    P("cross-section of a tall apartment building with a water pump in the basement and pipes going up, simple infographic, no text", "고층은 [전기 펌프]로 물을 올리거든요.", 3.0),
    P(f"{ME} looking worried at his phone in a dark room, phone shows a red battery", "[정전 6시간]. 배터리 31%.", 2.6, flash=True),
    P("cell phone tower on a rooftop at night with its lights going dark, gloomy sky, no people", "기지국 비상전원이 [바닥]납니다.", 2.8),
    P("close-up of a smartphone on a wooden table, screen shows a big no signal cross icon, dark room, no people", "[전화]도, 인터넷도 끊깁니다.", 2.6),
    P("dark convenience store at night, cashier shaking head at a customer holding a credit card", "편의점 카드기는 [먹통].", 2.6),
    P("long line of people outside a small store at night holding cash, flashlights", "[현금] 있는 사람만 물을 삽니다.", 2.6),
    P(f"{ME} pulling a bucket of water up from an old stone well in a farmhouse yard, morning", "그 시간, 시골의 당신은 [우물]에서 물을 깁니다.", 3.0),
    P(f"{GP} cooking rice in an iron pot over a wood fire in an outdoor kitchen, smoke rising", "할아버지는 [가마솥]에 밥을 짓습니다.", 2.8),
    P("open refrigerator with no light inside in a dark kitchen, food going bad, no people", "[정전 1일]. 냉장고가 문제입니다.", 2.6, flash=True),
    P("spoiled food containers and milk carton on a kitchen counter, flies, dark mood, no people", "꺼진 지 [4시간] 넘으면 상하기 시작합니다.", 3.0),
    P(f"{GP} putting kimchi jars and meat into a cold underground earthen storage pit in the yard", "할아버지는 [땅속 저장고]로 옮깁니다.", 2.8),
    P("frosty apartment window with snow falling outside at night, cold blue tones, no people", "[정전 2일]. 기온 영하 8도.", 2.6, flash=True),
    P("a family wrapped in thick blankets huddled together in a dark cold apartment living room", "가스보일러도 [전기]가 있어야 돕니다.", 2.8),
    P("many lit candles on a table in a dark apartment, warm glow, no people", "사람들이 [촛불]을 켜기 시작합니다.", 2.6),
    P("apartment building at night with one window burning with bright orange flames and black smoke, fire truck with red lights below", "정전 때 [불]이 자주 나는 이유죠.", 2.8),
    P("small gasoline generator running on an enclosed apartment balcony, grey fumes, dark night, no people", "누군가는 [발전기]를 베란다 안에서 돌립니다.", 2.8),
    P("invisible grey gas drifting under a door into a dark room, eerie, no people", "[일산화탄소]는 냄새도 없습니다.", 2.8),
    P(f"{ME} and {GP} sitting by a warm wood stove in a farmhouse room at night, firelight", "시골집은 [장작 난로] 하나로 따뜻합니다.", 2.8),
    P(f"{ME} listening to an old portable radio on the floor, serious face, lantern light", "[정전 3일]. 라디오만 들립니다.", 2.6, flash=True),
    P("close-up of an old silver portable radio with a glowing dial on a wooden floor, lantern light, no people", "\"복구 시점은 [미정]입니다.\"", 2.8),
    P(f"{ME} staring at the phone with the last message on screen, worried face, lantern light", "마지막으로 온 친구 문자 한 통.", 2.8),
    P(f"{ME} reading a text message on his phone in the dark, shocked face, lantern light", "\"야… 우리 집 [화장실]이 이상해.\"", 3.2),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
