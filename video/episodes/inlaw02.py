"""시집살이 2부: 김장날. 시누이 부부는 놀고 은서만 100포기. 시누이는 해마다 김치를 가져가 몰래 팔고 있었다.
게시 제목 안: "김장날 며느리만 100포기 시킨 시누이, 중고마켓에 올라온 판매글 하나로 들통났다"
사이다: 재료비 전부 은서 카드 + 시누이 판매글 캡처. 떡밥: 시아버지가 쓰러짐(간병은 누가?).
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("시집살이", "2부")
END = ("3부 예고", "아버님은 누가 모시니?", "팔로우하고 다음 편 보기")

GO = "elderly korean old lady aged 65, wrinkled aged face, graying short tight permed hair, red lipstick, burgundy cardigan, gold necklace"
EUN = "korean woman in her early 30s, low ponytail, gentle face, beige blouse"
JUN = "korean man in his mid 30s, short neat hair, round face, navy polo shirt"
AUNT = "korean woman in her late 60s, gray hair in a bun, green quilted jacket"
SIS = "korean woman in her late 30s, long curled brown hair, designer clothes, sunglasses on her head"
SH = "korean man in his 40s, slicked back hair, thin mustache, white shirt, flashy gold watch"
FA = "frail korean man in his early 70s, thin white hair, gray pajamas"

S = [
    dict(dur=3.0, photos=[f"{SIS} lounging with nail polish while {EUN} salts piles of cabbage in a yard",
                          f"close-up portrait of {SIS}, mocking smile, painting her nails, single person!*"],
         lines=[("시누이", "올케~ 백 포기는 해야 우리도 나눠 먹지~")]),
    dict(dur=2.5, photos=[f"close-up portrait of {EUN}, exhausted, red hands, single person"],
         lines=[("은서", "아가씨도 좀 도와주시면…")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, angry, single person!"],
         lines=[("고정숙", "우리 딸 손 다치면 네가 책임질래?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SH}, laughing, eating, single person"],
         lines=[("고서방", "김치는 역시 처남댁 손맛이지~")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=["close-up of a long supermarket receipt for cabbages, red pepper powder and salt, no people",
                                      f"close-up portrait of {EUN}, worried, looking at a receipt, single person"],
         lines=[("은서", "재료비 80만 원… 또 내 카드네.")]),
    dict(dur=3.0, sepia=True, photos=[f"{SIS} loading many kimchi containers into a car trunk, sneaky"],
         lines=[("시누이", "이번에도 스무 통은 챙겨 가야지~")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {JUN}, puzzled, single person"],
         lines=[("준호", "누나네는 셋인데… 그걸 다 먹어?")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=["close-up of a smartphone screen showing a second-hand market listing selling homemade kimchi with photos, no people",
                                      f"close-up portrait of {EUN}, sharp, showing a phone, single person"],
         lines=[("은서", "아가씨, 이 판매글… 아가씨 계정 맞죠?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SIS}, startled, single person!"],
         lines=[("시누이", "그, 그건 친구가 올린 거야!")]),
    dict(dur=3.0, photos=["close-up of a smartphone screen showing a chat where a seller writes delivery details, no people",
                          f"close-up portrait of {EUN}, calm, single person"],
         lines=[("은서", "택배 보내는 주소가, 아가씨 집이던데요?")]),
    dict(dur=3.0, photos=[f"close-up portrait of {JUN}, angry, standing up, single person"],
         lines=[("준호", "누나! 내 아내 손으로 만든 걸 팔았어?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, flustered, single person"],
         lines=[("고정숙", "아이고… 딸아, 그게 정말이니?")]),
    dict(dur=3.0, photos=[f"close-up portrait of {EUN}, firm, single person"],
         lines=[("은서", "재료비 80만 원, 팔린 만큼 돌려주세요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SH}, sweating, looking away, single person"],
         lines=[("고서방", "여보… 그만 가자.")]),
    dict(dur=3.0, photos=[f"{EUN} and {JUN} packing kimchi together, smiling", f"close-up portrait of {EUN}, warm smile, single person"],
         lines=[("은서", "나눠 먹는 정은, 같이 담글 때 생기는 거예요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, flash=True, photos=[f"{FA} collapsing in the living room, family rushing to him"],
         lines=[("고정숙", "여보! 여보, 정신 차려요!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {SIS}, cold calculating look, single person"],
         lines=[("시누이", "병간호는… 당연히 올케가 해야지?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
