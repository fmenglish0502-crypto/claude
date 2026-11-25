"""종량제 봉투 빌런 1화: 남의 종량제 봉투에 쓰레기 버리던 이웃. 지어낸 이야기. 대본: scripts/series-batch-01.md 3번.

참조 스타일(STYLE="ref") + 배우 사진(output/cast/). 첫 장면은 오해로 몰아붙이는 대화 → "일주일 전" 회상 → 단속반 사이다 → 떡밥.
photos 끝 표시: ! 흔들림, < 좌우 뒤집기, * 얼굴 크게.
"""

STYLE = "ref"
TITLE = ("", "")
END = ("다음 편", "건물주 언니의 등장?", "팔로우하고 다음 편 보기")

CAST = {
    "han": "f60_leopard.jpg",         # 한미숙 (빌런, 50대 이웃)
    "ji": "f20_longhair.jpg",         # 지원 (빌라 1층)
    "nb1": "f60_purple_scream.jpg",   # 이웃1
    "nb2": "m60_grayhair.jpg",        # 이웃2
    "off": "m30_graysuit.jpg",        # 구청 단속반
}

S = [
    # --- 첫 장면: 오해로 몰아붙이기 (훅) ---
    dict(dur=3.0, photos=["@nb1|@ji", "@nb1!"], lines=[("이웃1", "1층 아가씨! 분리수거 안 할 거야?!")]),
    dict(dur=2.5, photos=["@ji*"], lines=[("지원", "저 아니에요… 제 봉투에 누가…")]),
    dict(dur=2.5, photos=["@han", "@han*"], lines=[("한미숙", "어머, 봉투에 이름까지 적혀 있는데?")]),
    dict(dur=2.5, photos=["@nb2"], lines=[("이웃2", "과태료 나오면 우리가 같이 물어야 해?")]),
    # --- 회상: 일주일 전 ---
    dict(dur=3.0, sepia=True, photos=["korean villa garbage collection area at night, tied white garbage bags piled by a wall, streetlight, no people"],
         lines=[(None, "모든 건 일주일 전부터 시작됐다.")]),
    dict(dur=3.5, sepia=True, photos=["close-up of an overstuffed white garbage bag about to burst, villa garbage area, no people", "@ji<"],
         lines=[(None, "돈 주고 산 내 봉투가, 다음 날이면 터질 듯 부풀어 있었다.")]),
    dict(dur=3.0, sepia=True, photos=["@han<", "=05_0"],
         lines=[("한미숙", "봉투값 아깝게 뭐하러 사?")]),
    dict(dur=3.0, sepia=True, photos=["close-up inside a garbage bag, crushed cans, plastic bottles and food waste mixed together, messy"],
         lines=[(None, "분리수거도 안 한 쓰레기를, 남의 봉투에.")]),
    dict(dur=3.0, sepia=True, photos=["white garbage bag with a big yellow rejection sticker attached, villa garbage area, daytime", "@ji"],
         lines=[("지원", "내 이름 적힌 봉투인데… 수거 거부라고?")]),
    # --- 다시 지금: 사이다 ---
    dict(dur=3.0, flash=True, photos=["@off", "grainy black and white CCTV footage of a woman in a leopard print shirt untying a garbage bag at night, timestamp"],
         lines=[("단속반", "무단투기 신고 들어왔습니다. CCTV 확인하겠습니다.")]),
    dict(dur=3.0, photos=["=09_1", "@han*!"], lines=[("단속반", "남의 봉투에 무단투기, 분리배출 위반까지.")]),
    dict(dur=2.5, photos=["@off<"], lines=[("단속반", "과태료 부과 대상입니다.")]),
    dict(dur=2.5, photos=["@han!"], lines=[("한미숙", "봉투 좀 같이 쓴 게 뭐 어때서!")]),
    dict(dur=3.0, photos=["close-up of a tablet screen showing a long list of CCTV video files with dates", "@han<!"],
         lines=[("단속반", "몇 달 치가 다 찍혀 있네요. 건마다 따로 부과됩니다.")]),
    dict(dur=2.5, photos=["@nb1<"], lines=[("이웃1", "지원 씨, 오해해서 미안해요.")]),
    dict(dur=3.0, photos=["@ji", "@ji*"], lines=[("지원", "내 쓰레기는 내 봉투에. 그게 상식이죠.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=["@han<"], lines=[(None, "그런데 다음 날, 한미숙이 웃으며 나타났다.")]),
    dict(dur=3.0, flash=True, photos=["@han*"], lines=[("한미숙", "이 빌라, 우리 언니 건물인 거 몰랐지?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
