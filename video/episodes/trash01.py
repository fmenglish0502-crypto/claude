"""종량제 봉투 빌런 1화: 남의 종량제 봉투에 쓰레기 버리던 이웃. 지어낸 이야기. 대본: scripts/series-batch-01.md 3번.

참조 스타일(STYLE="ref") + 선명한 사진풍 그림(PHOTO_MODEL="rv"). 장면마다 인물이 행동하는 그림을 새로 그린다.
첫 장면은 오해로 몰아붙이는 대화 → "일주일 전" 회상 → 단속반 사이다 → 떡밥.
photos 끝 표시: ! 흔들림, < 좌우 뒤집기, * 얼굴 크게. "=번호"는 그려둔 그림 다시 쓰기.
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
END = ("다음 편", "건물주 언니의 등장?", "팔로우하고 다음 편 보기")

HAN = "middle-aged korean woman in her late 50s, wrinkled aged face, sagging cheeks, short curly permed hair, leopard print blouse"
JI = "korean woman in her 20s, long straight black hair, white shirt"
NB1 = "elderly korean woman in her late 60s, wrinkled face, gray streaked short permed hair, purple blouse"
NB2 = "elderly korean man in his late 60s, wrinkled face, gray hair, beige cardigan"
OFF = "korean man in his 30s, district office enforcement officer, navy vest with ID badge"

S = [
    # --- 첫 장면: 오해로 몰아붙이기 (훅) ---
    dict(dur=3.0, photos=[f"{NB1} yelling and pointing at {JI}, face to face, villa entrance at night",
                          f"close-up portrait of {NB1}, furious, mouth wide open yelling, single person!*"],
         lines=[("이웃1", "1층 아가씨! 분리수거 안 할 거야?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, shocked and hurt, teary eyes"],
         lines=[("지원", "저 아니에요… 제 봉투에 누가…")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, sly smirk, arms crossed", f"{HAN} pointing at a garbage bag with a name written on it"],
         lines=[("한미숙", "어머, 봉투에 이름까지 적혀 있는데?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB2}, frowning, annoyed"],
         lines=[("이웃2", "과태료 나오면 우리가 같이 물어야 해?")]),
    # --- 회상: 일주일 전 ---
    dict(dur=3.0, sepia=True, photos=["korean villa garbage collection area at night, tied white garbage bags piled by a wall, streetlight, no people"],
         lines=[("지원", "일주일 전부터였어. 그날 밤도…")]),
    dict(dur=3.5, sepia=True, photos=["close-up of an overstuffed white garbage bag about to burst, villa garbage area, no people",
                                      f"close-up portrait of {JI}, puzzled, looking down at a garbage bag"],
         lines=[("지원", "반만 채운 봉투가… 왜 이렇게 꽉 찼지?")]),
    dict(dur=3.0, sepia=True, photos=[f"{HAN} secretly untying someone else's white garbage bag at night, looking around",
                                      f"close-up portrait of {HAN}, greedy grin, at night"],
         lines=[("한미숙", "봉투값 아깝게 뭐하러 사?")]),
    dict(dur=3.0, sepia=True, photos=["close-up inside a garbage bag, crushed cans, plastic bottles and food waste mixed together, messy"],
         lines=[("지원", "캔에 음식물까지… 이거 내 쓰레기 아닌데?")]),
    dict(dur=3.0, sepia=True, photos=["white garbage bag with a big yellow rejection sticker attached, villa garbage area, daytime, no people",
                                      f"close-up portrait of {JI}, frustrated, holding a yellow sticker"],
         lines=[("지원", "내 이름 적힌 봉투인데… 수거 거부라고?")]),
    # --- 다시 지금: 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {OFF}, serious, holding a tablet, villa entrance",
                                      "grainy black and white CCTV footage of a middle-aged woman in a leopard print shirt untying a garbage bag at night, timestamp"],
         lines=[("단속반", "무단투기 신고 들어왔습니다. CCTV 확인하겠습니다.")]),
    dict(dur=3.0, photos=["=09_1", f"extreme close-up of {HAN}, shocked, eyes wide, mouth open!"],
         lines=[("단속반", "남의 봉투에 무단투기, 분리배출 위반까지.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {OFF}, firm expression, writing a fine notice"],
         lines=[("단속반", "과태료 부과 대상입니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, angry, shouting, flustered!"],
         lines=[("한미숙", "봉투 좀 같이 쓴 게 뭐 어때서!")]),
    dict(dur=3.0, photos=["close-up of a tablet screen showing a long list of CCTV video files with dates, no people",
                          f"close-up portrait of {HAN}, pale, speechless, sweating"],
         lines=[("단속반", "몇 달 치가 다 찍혀 있네요. 건마다 따로 부과됩니다.")]),
    dict(dur=2.5, photos=[f"{NB1} bowing apologetically to {JI}, villa entrance"],
         lines=[("이웃1", "지원 씨, 오해해서 미안해요.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {JI}, calm confident smile", f"{JI} putting her own tied garbage bag neatly at the collection point"],
         lines=[("지원", "내 쓰레기는 내 봉투에. 그게 상식이죠.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{HAN} walking toward the villa with an elegant rich woman in her 60s in a fur coat, smirking"],
         lines=[("한미숙", "지원 씨~ 우리 언니 소개해 줄게.")]),
    dict(dur=3.0, flash=True, photos=[f"extreme close-up of {HAN}, evil smirk, looking down at someone"],
         lines=[("한미숙", "이 빌라, 우리 언니 건물인 거 몰랐지?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
