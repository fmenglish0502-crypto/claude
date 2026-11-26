"""악플러 3부: MCN 윤대표의 노예 계약. 수익 9:1, 위약금 10배. 주변은 "기회니까 사인해" 압박.
사이다: 변호사가 독소조항 짚기 + 같은 회사 피해 유튜버들 증언. 떡밥: 윤대표가 악플러 최도윤을 부른다.
게시 제목 안(바이럴 공식: 가해 행동 + 반전 장치 한마디/한 장): "신인 유튜버에게 노예 계약 들이민 대표, 변호사가 꺼낸 서류에 말을 잃었다"
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")

PART = ("악플러 참교육", "3부")
END = ("4부 예고", "돌아온 악플러?", "팔로우하고 다음 편 보기")

SO = "korean woman in her late 20s, shoulder-length wavy brown hair, cream knit sweater, small silver earrings"
CHOI = "thin korean man in his mid 20s, messy short black hair, dark circles under eyes, gray hoodie"
FR = "korean woman in her 20s, high ponytail, denim jacket"
LAW = "korean female lawyer in her 40s, short bob hair, black suit, white blouse"
COP = "korean police detective in his 50s, short gray buzz cut, white shirt, loosened tie"
SERA = "korean woman in her 30s, bleached blonde long hair, heavy makeup, pink tracksuit"
YUN = "korean man in his 50s, neatly combed silver hair, three-piece navy suit, gold rimmed glasses"

S = [
    dict(dur=3.0, photos=[f"{YUN} pushing a contract across a glass desk toward {SO} in a luxury office",
                          f"close-up portrait of {YUN}, arrogant smile, single person!*"],
         lines=[("윤대표", "사인만 하면 구독자 백만, 내가 만들어 줄게.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SO}, hesitant, single person"],
         lines=[("소담", "계약서… 집에서 읽어 봐도 될까요?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {YUN}, annoyed, cold, single person"],
         lines=[("윤대표", "지금 안 하면 이 기회는 없어.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {FR}, excited, single person"],
         lines=[("하린", "소담아, 이런 회사가 어디 있어! 그냥 해!")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{YUN} toasting with wine at a luxury restaurant, laughing"],
         lines=[("윤대표", "유튜버들은 계약서를 안 읽어. 그게 돈이지.")]),
    dict(dur=3.0, sepia=True, photos=["close-up of a contract page with tiny fine print and a highlighted clause, no people",
                                      f"close-up portrait of {SO}, frowning, reading, single person"],
         lines=[("소담", "수익은 회사 9… 나는 1?")]),
    dict(dur=3.0, sepia=True, photos=[f"close-up portrait of {SO}, shocked, single person"],
         lines=[("소담", "그만두면 위약금이… 받은 돈의 열 배?")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{LAW} walking into the luxury office beside {SO}",
                                      f"close-up portrait of {LAW}, sharp gaze, single person"],
         lines=[("서변호사", "계약 검토는 제가 하겠습니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {YUN}, irritated, single person"],
         lines=[("윤대표", "변호사까지 데려와? 의심이 많네.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {LAW}, pointing at a contract, single person"],
         lines=[("서변호사", "이렇게 한쪽만 불리한 조항은 무효가 될 수 있어요.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {LAW}, calm, holding papers, single person"],
         lines=[("서변호사", "그리고 이 회사 소속 유튜버 세 명이, 이미 소송 중이고요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {YUN}, shocked, sweating, single person!"],
         lines=[("윤대표", "그걸… 어떻게?")]),
    dict(dur=3.0, photos=[f"three young korean creators walking into the office holding documents",
                          f"close-up portrait of a young korean man in a black cap, angry, single person"],
         lines=[("유튜버", "대표님, 저희 정산서 다 들고 왔습니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {YUN}, furious, slamming the desk, single person!"],
         lines=[("윤대표", "다 나가! 당장!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {FR}, embarrassed, single person"],
         lines=[("하린", "소담아… 내가 괜히 하라고 했다. 미안해.")]),
    dict(dur=3.0, photos=[f"{SO} tearing the contract in half in front of the office building, sunny",
                          f"close-up portrait of {SO}, confident smile, single person"],
         lines=[("소담", "읽지 않은 계약서엔, 사인하지 않아요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{YUN} alone in a dark office making a phone call, city lights behind"],
         lines=[("윤대표", "너, 소담한테 고소당했던 놈이지?")]),
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {CHOI}, wicked grin, phone at ear, dark room, single person"],
         lines=[("최도윤", "네. 이번엔 제대로 갚아 줄게요.")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")

