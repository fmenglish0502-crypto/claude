"""악플러 2부: 영상 도둑 채널. 소담 영상을 베껴 올리고 오히려 소담을 표절범으로 몬다. 지어낸 이야기.
사이다: 원본 파일·촬영 기록 + 저작권 신고 → 채널 정지. 떡밥: 뒤에 있는 MCN 윤대표.
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")

PART = ("악플러 참교육", "2부")
END = ("3부 예고", "노예 계약서의 비밀?", "팔로우하고 다음 편 보기")

SO = "korean woman in her late 20s, shoulder-length wavy brown hair, cream knit sweater, small silver earrings"
CHOI = "thin korean man in his mid 20s, messy short black hair, dark circles under eyes, gray hoodie"
FR = "korean woman in her 20s, high ponytail, denim jacket"
LAW = "korean female lawyer in her 40s, short bob hair, black suit, white blouse"
COP = "korean police detective in his 50s, short gray buzz cut, white shirt, loosened tie"
SERA = "korean woman in her 30s, bleached blonde long hair, heavy makeup, pink tracksuit"
YUN = "korean man in his 50s, neatly combed silver hair, three-piece navy suit, gold rimmed glasses"

S = [
    dict(dur=3.0, photos=[f"{SERA} pointing at {SO} in a crowded cafe, phone camera recording",
                          f"close-up portrait of {SERA}, accusing, mouth open shouting, single person!*"],
         lines=[("오세라", "남의 영상 베낀 표절범이 여기 있네!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SO}, stunned, single person"],
         lines=[("소담", "그 영상… 제가 먼저 찍은 거예요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SERA}, mocking laugh, single person"],
         lines=[("오세라", "증거 있어? 내 구독자가 열 배야~")]),
    dict(dur=2.5, photos=["close-up of a smartphone screen showing angry comments under a video, no people"],
         lines=[("시청자", "표절범 소담 아웃!")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{SO} filming a cooking video in her small kitchen at night with a phone on a tripod",
                                      f"close-up portrait of {SO}, focused, single person"],
         lines=[("소담", "이번 영상, 사흘 밤 새워 찍었는데…")]),
    dict(dur=3.0, sepia=True, photos=[f"{SERA} at a desk copying video files on a laptop, smirking",
                                      f"close-up portrait of {SERA}, greedy smile in laptop glow, single person"],
         lines=[("오세라", "자막만 바꾸면 내 거지 뭐~")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {FR}, angry, single person"],
         lines=[("하린", "근데 왜 사람들이 너를 욕해?!")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {SO}, hurt, biting lip, single person"],
         lines=[("소담", "저쪽이 구독자가 많으니까…")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{SO} opening a laptop showing a folder of original video files with dates",
                                      "close-up of a laptop screen showing video file properties with creation dates, no people"],
         lines=[("소담", "원본 파일이에요. 촬영 날짜가 다 남아 있죠.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SERA}, flustered, eyes darting, single person"],
         lines=[("오세라", "그, 그런 건 조작할 수 있잖아!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {SO}, calm confident, single person"],
         lines=[("소담", "편집 전 원본 영상도 있어요. 제 얼굴까지 다 나와요.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {LAW}, firm, single person"],
         lines=[("서변호사", "남의 영상을 허락 없이 올리면 저작권 침해가 될 수 있어요.")]),
    dict(dur=3.0, photos=["close-up of a laptop screen showing a video channel page with a big red channel terminated notice, no people",
                          f"close-up portrait of {SERA}, shocked, mouth open, single person!"],
         lines=[("오세라", "내 채널이… 정지?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SERA}, desperate, crying, single person"],
         lines=[("오세라", "수익은?! 그 돈 다 어떡해!")]),
    dict(dur=2.5, photos=["close-up of a smartphone screen showing supportive comments with heart emojis, no people"],
         lines=[("시청자", "소담님 오해해서 죄송해요ㅠㅠ")]),
    dict(dur=3.0, photos=[f"{SO} and {FR} laughing together at a cafe table", f"close-up portrait of {SO}, relieved smile, single person"],
         lines=[("소담", "만든 사람의 땀은, 지켜져야죠.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{SERA} in a dark parking garage on the phone, scared"],
         lines=[("오세라", "대표님… 저 걸렸어요.")]),
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {YUN}, cold smile, holding a contract, single person"],
         lines=[("윤대표", "걱정 마. 그 여자, 우리 회사로 데려오면 되니까.")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")

