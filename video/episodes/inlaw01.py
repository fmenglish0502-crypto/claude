"""시집살이 1부: 명절마다 며느리만 부엌에 가두던 시어머니. 지어낸 이야기. 대본: scripts/series-batch-01.md 6번.
게시 제목 안(바이럴 공식: 상황+결과): "명절마다 며느리만 부려먹던 시어머니, 며느리가 꺼낸 통장 한 장에 얼어붙었다"
대화만(내레이션 0). 맞붙기 → 회상 → 통장 사이다 → 떡밥(시누이 부부가 들어와 살겠다).
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("시집살이", "1부")
END = ("2부 예고", "시누이 부부가 들어왔다?", "팔로우하고 다음 편 보기")

GO = "elderly korean old lady aged 65, wrinkled aged face, graying short tight permed hair, red lipstick, burgundy cardigan, gold necklace"
EUN = "korean woman in her early 30s, low ponytail, gentle face, beige blouse"
JUN = "korean man in his mid 30s, short neat hair, round face, navy polo shirt"
AUNT = "korean woman in her late 60s, gray hair in a bun, green quilted jacket"
SIS = "korean woman in her late 30s, long curled brown hair, designer clothes, sunglasses on her head"
SH = "korean man in his 40s, slicked back hair, thin mustache, white shirt, flashy gold watch"
FA = "frail korean man in his early 70s, thin white hair, gray pajamas"

S = [
    dict(dur=3.0, photos=[f"{GO} scolding {EUN} in a korean kitchen full of holiday food, finger pointing",
                          f"close-up portrait of {GO}, contemptuous, mouth open scolding, single person!*"],
         lines=[("고정숙", "간이 왜 이래? 친정에서 뭘 배웠니?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {EUN}, tired, holding a spatula, single person"],
         lines=[("은서", "어머님, 새벽부터 저 혼자 했어요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JUN}, annoyed, lying on a sofa, single person"],
         lines=[("준호", "엄마 말 좀 들어. 너만 참으면 되잖아.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {AUNT}, gossiping whisper, single person"],
         lines=[("시고모", "요즘 며느리들은 버릇이 없어.")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{EUN} alone frying korean pancakes on the kitchen floor, piles of food",
                                      f"family watching TV and laughing in a living room, eating fruit"],
         lines=[("은서", "명절마다… 나만 부엌이었지.")]),
    dict(dur=3.0, sepia=True, photos=[f"close-up portrait of {GO}, smug, counting cash, single person"],
         lines=[("고정숙", "준호야, 이번 달 용돈도 꼭 보내라~")]),
    dict(dur=3.0, sepia=True, photos=["close-up of a bank statement showing monthly loan repayments, no people",
                                      f"close-up portrait of {EUN}, determined, at night, single person"],
         lines=[("은서", "이 집 대출금은… 내 월급으로 갚고 있는데.")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{EUN} taking off her apron and placing a document on the dining table",
                                      f"close-up portrait of {EUN}, calm, firm, single person"],
         lines=[("은서", "어머님, 오늘은 제가 할 말이 있어요.")]),
    dict(dur=3.0, photos=["close-up of a bank passbook open on a dining table next to korean holiday food, no people",
                          f"close-up portrait of {EUN}, steady gaze, single person"],
         lines=[("은서", "이 집 대출금, 3년 동안 제가 갚았어요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, shocked, stammering, single person!"],
         lines=[("고정숙", "그, 그건 준호가 낸 거잖아!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {EUN}, cool, single person"],
         lines=[("은서", "준호 씨 월급은 어머님 용돈으로 다 갔잖아요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {AUNT}, stunned, single person"],
         lines=[("시고모", "언니… 그게 사실이야?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JUN}, embarrassed, red face, single person"],
         lines=[("준호", "엄마… 우리가 그동안…")]),
    dict(dur=3.0, photos=[f"{EUN} walking out the front door with her bag, sunny", f"close-up portrait of {EUN}, relieved smile, single person"],
         lines=[("은서", "오늘부터 명절엔 친정 가요. 음식은 시켜 드세요.")]),
    dict(dur=2.5, photos=["delivery food boxes on a living room table, family sitting awkwardly, no faces visible"],
         lines=[("시고모", "배달 음식으로 차례를 지내게 생겼네…")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{SIS} and {SH} arriving at the front door with big suitcases, smirking"],
         lines=[("시누이", "엄마~ 우리 당분간 여기서 살게!")]),
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {SH}, sly smile, gold watch, single person"],
         lines=[("고서방", "처남댁, 내 방은 어디야?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
