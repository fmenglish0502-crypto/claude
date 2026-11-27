"""만약에 시뮬레이션 1편: 서울에 72시간 대정전이 온다면. 지어낸 가상 시나리오(정보는 실제 정전 대비 상식).
형식: '당신' 시점 해설 + 플랫 일러스트 빠른 컷 + 화면 가운데 큰 자막([ ] 낱말은 주황색 강조).
게시 제목 안: "서울에 72시간 정전이 온다면, 당신은 버틸 수 있을까?"
"""

STYLE = "sim"
PHOTO_MODEL = "dreamshaper"
PHOTO_STYLE = ("flat design vector art illustration, adobe illustrator, 2d motion graphics animation still, bold flat colors, "
               "dark navy blue and warm orange palette, simple geometric shapes, cel shading, clean lines, detailed background, no text")
TITLE = ("", "")
PART = None
END = ("다음 편 예고", "라디오 속 목소리의 정체?", "팔로우하고 2편 보기")

ME = "a young korean man in a dark gray hoodie, simple flat cartoon character"

S = [
    dict(dur=2.5, photos=["night skyline of seoul with namsan tower, every building light switched off, dark city, orange dusk sky"],
         lines=[("해설", "지금부터 [72시간] 동안")]),
    dict(dur=2.5, photos=[f"{ME} seen from behind standing at an apartment window looking at a dark city with no lights"],
         lines=[("해설", "서울 전체에 [전기]가 끊깁니다.")]),
    dict(dur=2.5, photos=[f"{ME} sitting on a sofa in a dark living room holding a phone with flashlight on"],
         lines=[("해설", "당신은 [고층 아파트] 18층에 삽니다.")]),
    dict(dur=2.5, photos=["apartment hallway at night, several neighbors holding flashlights chatting and smiling, simple cartoon people"],
         lines=[("해설", "다들 금방 돌아올 거라며 [웃습니다].")]),
    dict(dur=2.5, photos=["closed metal elevator doors in a dark apartment lobby, flashlight beam, nobody around"],
         lines=[("해설", "그런데 [엘리베이터]가 멈췄고")]),
    dict(dur=2.5, photos=["close-up of a kitchen faucet turned on with no water coming out, dark kitchen, no people"],
         lines=[("해설", "수돗물도 [안 나옵니다].")]),
    dict(dur=3.0, photos=["cross-section diagram of a tall apartment building with a water pump in the basement and pipes going up, simple infographic, no text"],
         lines=[("해설", "고층은 [펌프]로 물을 올리거든요.")]),
    dict(dur=2.5, flash=True, photos=["big analog wall clock in a dark room, hands moving, dramatic shadow, no people"],
         lines=[("해설", "[6시간] 뒤.")]),
    dict(dur=2.5, photos=["hand holding a smartphone with a nearly empty red battery icon, dark background"],
         lines=[("해설", "휴대폰 배터리 [31%].")]),
    dict(dur=3.0, photos=["cell phone tower on a rooftop at night with its lights going dark, gloomy sky, no people"],
         lines=[("해설", "기지국 비상전원까지 [바닥]나면")]),
    dict(dur=2.5, photos=[f"{ME} frowning at a phone screen with no signal, dark room"],
         lines=[("해설", "[전화]도 인터넷도 끊깁니다.")]),
    dict(dur=2.5, photos=["dark convenience store at night, cashier shaking head at a customer holding a credit card, simple cartoon people"],
         lines=[("해설", "편의점에선 [카드]가 안 됩니다.")]),
    dict(dur=2.5, photos=["hand holding korean paper money bills buying bottled water at a counter, flashlight light"],
         lines=[("해설", "[현금] 있는 사람만 물을 삽니다.")]),
    dict(dur=2.5, flash=True, photos=["open refrigerator with no light inside in a dark kitchen, food going bad, no people"],
         lines=[("해설", "[12시간] 뒤, 냉장고.")]),
    dict(dur=3.0, photos=["spoiled food containers and milk carton on a kitchen counter, flies, dark mood, no people"],
         lines=[("해설", "4시간 넘게 꺼진 음식은 [위험]합니다.")]),
    dict(dur=2.5, photos=["frosty apartment window with snow falling outside at night, cold blue tones, no people"],
         lines=[("해설", "게다가 [겨울]이라면")]),
    dict(dur=2.5, photos=[f"{ME} wrapped in a thick blanket shivering next to a wall mounted gas boiler that is off"],
         lines=[("해설", "가스보일러도 [전기]가 있어야 돕니다.")]),
    dict(dur=2.5, photos=["many lit candles on a table in a dark apartment, warm glow, no people"],
         lines=[("해설", "사람들이 [촛불]을 켜기 시작합니다.")]),
    dict(dur=2.5, photos=["window of an apartment building at night with orange fire glow and smoke, fire trucks below"],
         lines=[("해설", "정전 때 [불]이 자주 나는 이유죠.")]),
    dict(dur=3.0, photos=["small gasoline generator running on an enclosed apartment balcony, grey fumes, dark night, no people"],
         lines=[("해설", "옆집은 [발전기]를 베란다 안에서 돌립니다.")]),
    dict(dur=2.5, photos=["invisible grey gas drifting under a door into a dark room, eerie, no people"],
         lines=[("해설", "[일산화탄소]는 냄새도 없습니다.")]),
    dict(dur=3.0, photos=[f"{ME} facing the viewer in a dark room, serious expression, flashlight under the chin"],
         lines=[("해설", "당신이라면 [지금] 뭘 챙기겠습니까?")]),
    dict(dur=3.0, photos=["flat lay of survival items on a table: water bottles, cash, flashlight, power bank, radio, simple icons style"],
         lines=[("해설", "[물] 3일 치, [현금], [손전등].")]),
    dict(dur=2.5, photos=["portable power bank charging a smartphone on a wooden table, cozy light, no people"],
         lines=[("해설", "그리고 [보조배터리].")]),
    dict(dur=2.5, flash=True, photos=["dark city skyline under a starry sky, total silence, one tiny window glowing, no people"],
         lines=[("해설", "그런데 [72시간]째 밤.")]),
    dict(dur=3.5, photos=["old portable radio on a windowsill glowing faintly in a dark room, mysterious, no people"],
         lines=[("해설", "꺼져 있던 [라디오]에서 목소리가 들립니다.")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
