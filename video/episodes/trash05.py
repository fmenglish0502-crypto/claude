"""종량제 봉투 빌런 5부: 한미숙 자매의 마지막 카드 — 빌라를 통째로 팔아 세입자를 쫓아내려 한다. 지어낸 이야기.
4부 떡밥("이 빌라, 통째로 팔아 버리면 되지")을 받는다. 5부 규칙: 만들어두고 반응 보고 게시(보류).
사이다: 집이 팔려도 전입·거주한 세입자의 계약은 이어질 수 있다 + 숨긴 문제(관리비·소방 위반)를 매수인이 알게 되자 계약 취소.
법 대사는 "~될 수 있다" 수준. 떡밥(6부): 한미숙이 지원네 옆집으로 이사 온다?
게시 제목 안: "세입자 쫓아내려고 빌라 통째로 판 집주인, 매수인이 서류 한 장 보더니 계약을 깼다"
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("종량제 빌런", "5부")
END = ("6부 예고", "옆집이 된 한미숙?", "팔로우하고 다음 편 보기")

HAN = "middle-aged korean woman in her late 50s, wrinkled aged face, sagging cheeks, short curly permed hair, leopard print blouse"
MJ = "rich elderly korean woman in her 60s, wrinkled face, elegant gray bob hair, fur coat, pearl earrings, arrogant"
JI = "korean woman in her 20s, long straight black hair, white shirt"
NB1 = "elderly korean woman in her late 60s, wrinkled face, gray streaked short permed hair, purple blouse"
NB2 = "elderly korean man in his late 60s, wrinkled face, gray hair, beige cardigan"
BUY = "calm korean man in his 50s, short salt-and-pepper hair, beige trench coat, holding a document folder"
AG = "kind korean man in his 40s, real estate agent, navy suit, glasses"

S = [
    dict(dur=3.0, photos=[f"{MJ} waving a sale contract in front of {JI} at a villa entrance, neighbors behind",
                          f"close-up portrait of {MJ}, triumphant sneer, single person!*"],
         lines=[("한미자", "이 빌라 팔렸어! 새 주인이 다 비우래!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, calm, single person"],
         lines=[("지원", "집이 팔려도, 제 계약은 그대로예요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB2}, worried, single person"],
         lines=[("이웃2", "우리 같은 늙은이는 어디로 가라고…")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, gloating, single person"],
         lines=[("한미숙", "다 1층 아가씨 탓인 줄 알아~")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{MJ} and {HAN} shaking hands with {BUY} at a real estate office, fake smiles"],
         lines=[("한미자", "문제요? 이 빌라엔 아무 문제 없어요~")]),
    dict(dur=3.0, sepia=True, photos=[f"{HAN} stuffing papers into a drawer, looking around nervously",
                                      "close-up of a fire safety violation notice and an unpaid fee lawsuit paper hidden in a drawer, no people"],
         lines=[("한미숙", "소방 위반이랑 관리비 소송은… 숨겨야지.")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {JI}, thinking, reading a phone, single person"],
         lines=[("지원", "전입신고 하고 살고 있으면… 새 주인한테도 계약을 주장할 수 있어.")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{BUY} walking into the villa hallway with {AG}",
                                      f"close-up portrait of {BUY}, polite, serious, single person"],
         lines=[("매수인", "잔금 치르기 전에, 건물 좀 직접 보겠습니다.")]),
    dict(dur=3.0, photos=[f"{NB1} handing a folder of papers to {BUY}", f"close-up portrait of {NB1}, determined, single person"],
         lines=[("이웃1", "사장님, 이것도 보셔야 해요. 우리 빌라 사정이에요.")]),
    dict(dur=3.0, photos=["close-up of documents spread on a table: fire inspection violation, embezzlement complaint, fines, no people",
                          f"close-up portrait of {BUY}, frowning, reading, single person"],
         lines=[("매수인", "소방 위반에, 관리비 횡령 소송까지…")]),
    dict(dur=2.5, photos=[f"close-up portrait of {MJ}, panicked, single person!"],
         lines=[("한미자", "그, 그건 다 끝난 일이에요!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {BUY}, cold, firm, single person"],
         lines=[("매수인", "중요한 문제를 숨기셨으면, 계약을 무를 수 있습니다.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {AG}, nodding, single person"],
         lines=[("중개사", "세입자분들 계약도 그대로 이어지고요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, shocked, mouth open, single person!"],
         lines=[("한미숙", "언니! 계약금 돌려줘야 해?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB2}, relieved laugh, single person"],
         lines=[("이웃2", "허허, 지원 씨 덕에 살았네!")]),
    dict(dur=3.0, photos=[f"{JI} and neighbors smiling together in front of the villa at sunset",
                          f"close-up portrait of {JI}, confident smile, single person"],
         lines=[("지원", "집은 팔아도, 사는 사람 권리는 못 팔아요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{HAN} dragging a suitcase toward the villa at night, grinning"],
         lines=[("한미숙", "언니, 그럼 내가 직접 들어가 살지 뭐~")]),
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {HAN}, evil smile at a door with a unit number 102, single person"],
         lines=[("한미숙", "지원 씨~ 오늘부터 우리 옆집이야!")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
