"""만약에 시뮬레이션 「7일 뒤 대정전」 3부: 배관이 멈춰 화장실을 못 쓰게 된다. 역류·위생 위기, 할아버지와 간이 화장실·빗물받이. 지어낸 가상 시나리오.
게시 제목 안: "정전 5일째, 아파트 사람들이 제일 먼저 포기한 것은 화장실이었다"
"""

STYLE = "sim"
PHOTO_MODEL = "dreamshaper"
PHOTO_STYLE = ("2d animated film still, flat vector illustration, simple cel shading, cinematic wide shot, muted colors, "
               "dark navy blue shadows with warm amber lamp light, detailed environment, single scene, no text")
TITLE = ("", "")

ME = "a young korean man in his 20s with short black hair and a dark navy hoodie, simple flat cartoon character"
GP = "an old korean grandfather in his 70s with short white hair, tanned wrinkled face, brown work vest, simple flat cartoon character"
HOUSE = "a traditional korean countryside house with a tiled roof, stone wall, persimmon tree, mountains behind"


def P(prompt, line, dur=2.6, **kw):
    """장면 하나 = 그림 한 장(또는 여러 장) + 해설 한 줄."""
    photos = prompt if isinstance(prompt, list) else [prompt]
    return dict(dur=dur, photos=photos, lines=[("해설", line)], **kw)

PART = ("7일 뒤 대정전", "3부")
END = ("4부 예고", "밤마다 다가오는 발소리", "팔로우하고 다음 편 보기")

S = [
    P("close-up of a white toilet in a dark apartment bathroom, flashlight beam, no people", "[정전 4일]. 변기 물이 안 내려갑니다.", 2.8),
    P("empty toilet water tank with the lid open, dry inside, flashlight beam, no people", "물탱크를 채울 [물]이 없으니까요.", 2.8),
    P("people in an apartment hallway carrying buckets of water up the stairs, exhausted", "사람들은 [마실 물]로 변기를 내립니다.", 2.8),
    P("almost empty water bottles on a kitchen floor in a dark apartment, no people", "그러다 [마실 물]이 떨어집니다.", 2.6),
    P("cross-section of an apartment building basement with a stopped sewage pump and rising dirty water, simple infographic, no text", "지하의 [오수 펌프]도 멈췄습니다.", 2.8, flash=True),
    P("dirty water bubbling up from a floor drain in a dark bathroom, disgusting, no people", "저층에선 [하수]가 거꾸로 올라옵니다.", 2.8),
    P("apartment hallway at night with people covering their noses, trash bags piled up", "복도엔 [냄새]가 가득합니다.", 2.6),
    P("park at night next to apartments with people digging small holes in the dark, flashlights", "사람들이 [화단]에 몰래 볼일을 봅니다.", 2.8),
    P("glowing green germs and bacteria floating in murky dirty water, close-up, dark, no people, no text", "이게 진짜 위험입니다. [전염병].", 2.8),
    P("busy hospital entrance at night with no lights, people waiting outside", "단전된 병원은 [발전기]로 겨우 버팁니다.", 2.8),
    P(f"{ME} reading a message on the phone in a farmhouse room, shocked face, lantern light", "친구의 문자를 본 당신은 [얼어붙습니다].", 2.8),
    P(f"{GP} pointing at a corner of the farmhouse yard behind the shed, morning, explaining", "할아버지가 말합니다. \"[뒷간]부터 만들자.\"", 3.0, flash=True),
    P(f"{ME} digging a deep hole with a shovel behind a wooden shed, morning sunlight", "집에서 [멀리], 우물에서 더 멀리.", 2.8),
    P("simple wooden outhouse with a small door being built in a countryside yard, tools on the ground, no people", "나무판으로 [간이 화장실]을 세웁니다.", 2.8),
    P("bucket with a plastic bag inside and a sack of sawdust and a scoop next to it, simple, no people", "볼일 뒤엔 [톱밥]이나 흙을 덮습니다.", 2.8),
    P("lime powder bag and a scoop next to an outhouse, clean, no people", "[석회]를 뿌리면 냄새와 벌레가 줄어요.", 2.8),
    P(f"{GP} washing hands with soap over a basin using water from a ladle, outdoor", "그리고 [손 씻기]. 물이 귀해도요.", 2.8),
    P(f"{ME} setting big plastic barrels under the roof gutter of a farmhouse, cloudy sky", "지붕 물받이 밑엔 [빗물 통]을 놓습니다.", 2.8),
    P("rain pouring from a roof gutter into a blue plastic barrel, close-up, no people", "빗물은 [변기·빨래]용으로 씁니다.", 2.8),
    P(f"{GP} boiling water in a big pot over a wood fire, steam rising", "마실 물은 꼭 [끓여서].", 2.6),
    P("flat lay of a water filter, water purification tablets and bottles on a table, no people", "[정전 5일]. 물이 곧 생명입니다.", 2.8, flash=True),
    P("korean countryside village road with a few cars arriving loaded with luggage, dusk", "그날 오후, 마을에 [낯선 차]들이 들어옵니다.", 3.0),
    P("tired city family standing at a village gate with suitcases, dusk", "도시를 탈출한 [사람들]입니다.", 2.6),
    P(f"{GP} standing at the stone wall gate watching strangers, worried face, dusk", "할아버지의 얼굴이 [굳습니다].", 2.6),
    P("dark country road at night with flashlight beams of several people walking toward the village", "그리고 그날 밤, [발소리]가 들립니다.", 3.2),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
