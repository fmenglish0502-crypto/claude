"""만약에 시뮬레이션 「7일 뒤 대정전」 1부: 경보 → 무시하는 사람들 → 할아버지 시골집으로 → 사재기. 지어낸 가상 시나리오.
형식: "당신" 시점 해설 + 플랫 일러스트 빠른 컷 + 화면 가운데 큰 자막([ ] 낱말 주황 강조). 4부 합쳐 약 5분.
게시 제목 안: "7일 뒤 전국 전기가 끊긴다면, 당신은 뭘 하겠습니까?"
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

PART = ("7일 뒤 대정전", "1부")
END = ("2부 예고", "불이 꺼진 첫날 밤", "팔로우하고 다음 편 보기")

S = [
    P(f"{ME} seen from behind sitting on a sofa watching a big TV with a red emergency warning screen, city window at night", "당신에게 남은 시간은 [7일].", 2.8),
    P("TV news studio, a calm female anchor at a desk, red breaking news banner, glowing sun graphic on the screen behind her", "[역대급 태양폭풍]이 온다는 속보.", 2.8),
    P("giant glowing orange sun throwing a huge solar flare toward planet earth in dark space", "변압기가 타 버리면, 전국이 [정전]됩니다.", 3.0),
    P("press briefing room with a plain blue backdrop, an asian official in a gray suit at a podium with many microphones, no flags", "정부 발표: [복구까지 최소 몇 주].", 3.0),
    P(f"{ME} sitting on a sofa frozen, holding a phone, shocked face, dark living room lit by TV", "[대피 명령]은 없습니다.", 2.6, flash=True),
    P("group of four office workers in coats laughing together on a city street at dusk, one holding a coffee", "사람들은 웃습니다. [또 훈련이겠지].", 2.8),
    P("seoul subway platform seen from far away, a few small commuters waiting calmly, wide shot", "아무도 [준비]하지 않습니다.", 2.6),
    P(f"{ME} at a desk at night writing a list in a notebook, focused, lamp light", "하지만 당신은 [달랐습니다].", 2.6),
    P("close-up of an old flip phone ringing and glowing on a wooden table, dark room, no people", "시골에 혼자 사는 [할아버지].", 2.6),
    P(f"{GP} standing in front of {HOUSE}, holding an old phone to his ear, sunset", "\"내려와라. 여기는 [우물]이 있다.\"", 3.0),
    P(f"{ME} packing a big backpack on the floor of a small apartment, determined face", "남은 [6일]. 당신은 짐을 쌉니다.", 2.8, flash=True),
    P("korean highway at dawn, a small car driving toward green mountains, empty road", "서울을 떠나 [3시간].", 2.6),
    P(f"{HOUSE}, wide view, morning mist, a small car parked by the stone wall", "할아버지의 [시골집].", 2.6),
    P(f"{GP} and {ME} standing side by side in a farmhouse yard looking at a checklist, morning", "할아버지가 묻습니다. \"뭐부터 살래?\"", 3.0),
    P("flat lay of stacked water bottles, a big rice sack, ramen packs and canned food on a wooden floor, no people", "[물], [쌀], [통조림].", 2.8),
    P("flat lay of portable butane gas canisters, a camping stove, batteries and candles on a wooden floor, no people", "[부탄가스]와 [건전지].", 2.6),
    P("hand holding a thick stack of korean paper money bills, close-up, warm light", "그리고 [현금]. 카드는 곧 쓸모없어지니까.", 3.0),
    P("small rural hardware store, shelves with buckets, shovels and rope, an old shopkeeper, no customers", "읍내 철물점. 아직 [조용]합니다.", 2.6),
    P(f"{ME} pushing a shopping cart full of water bottles and rice sacks in a small grocery store", "당신은 [카트 세 대]를 채웁니다.", 2.6),
    P("grocery store cashier woman staring at a cart piled high, surprised face", "\"전쟁이라도 나요?\"", 2.6),
    P(f"{GP} pouring water from a bucket into big plastic water tanks next to an old stone well", "할아버지는 [우물]을 다시 손봅니다.", 2.8),
    P("old wooden shed full of firewood stacked neatly, axe on a stump, autumn afternoon, no people", "장작도 [겨울 치]를 쌓습니다.", 2.6),
    P(f"{ME} watching TV news in a farmhouse room, screen shows a crowded supermarket", "[D-3]. 뉴스가 바뀝니다.", 2.6, flash=True),
    P("crowded city supermarket, people fighting over the last water bottles, empty shelves, chaos", "그제야 사람들이 [마트]로 몰립니다.", 2.8),
    P("bare empty metal store shelves with nothing on them at all, cardboard boxes torn open on the floor, no people", "생수 진열대는 [텅] 비었습니다.", 2.6),
    P("long line of cars stuck at a gas station at night, red tail lights", "주유소엔 [몇 킬로] 줄이 섭니다.", 2.6),
    P(f"{GP} sitting on a wooden porch at night drinking tea, looking at the stars, calm", "할아버지가 말합니다. \"이제부턴 [시간] 싸움이다.\"", 3.2),
    P("big analog clock on a farmhouse wall at 11:59 pm, dim light, no people", "그리고 [D-day] 밤 11시 59분.", 2.8, flash=True),
    P("night view of a countryside village with warm house lights, a city glow on the horizon", "멀리 도시의 [불빛]이 보입니다.", 2.6),
    P("completely dark countryside village silhouette at night, every window dark, no lights at all, only stars in the sky", "그리고 [한순간에].", 3.0, flash=True),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
