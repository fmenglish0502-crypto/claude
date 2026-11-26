"""종량제 봉투 빌런 3화: 빌라 관리비의 비밀 (총무가 된 한미숙). 지어낸 이야기.

2화 떡밥("관리비는 이제 내가 걷을 거야")을 받는다. 한미숙이 관리비를 올려 걷고 사적으로 쓴다.
오해: 장부 공개를 요구한 지원이 "돈 문제로 이웃을 의심한다"고 욕먹음. 사이다: 통장 내역·영수증 대조. 법 대사는 "~될 수 있다" 수준.
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("종량제 빌런", "3부")
END = ("4부 예고", "잠긴 옥상의 비밀?", "팔로우하고 다음 편 보기")

HAN = "middle-aged korean woman in her late 50s, wrinkled aged face, sagging cheeks, short curly permed hair, leopard print blouse"
JI = "korean woman in her 20s, long straight black hair, white shirt"
NB1 = "elderly korean woman in her late 60s, wrinkled face, gray streaked short permed hair, purple blouse"
NB2 = "elderly korean man in his late 60s, wrinkled face, gray hair, beige cardigan"
YO = "young korean man in his 30s, glasses, plain gray sweater, accountant"

S = [
    # --- 첫 장면: 대화 훅 ---
    dict(dur=3.0, photos=[f"wide shot, {HAN} shouting and pointing her finger at {JI}, two women facing each other in a villa hallway",
                          f"close-up portrait of {HAN}, angry, mouth open yelling, single person!*"],
         lines=[("한미숙", "너 지금 내가 돈 빼돌렸다는 거야?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, calm but tense"],
         lines=[("지원", "장부만 보여달라는 거예요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB1}, annoyed, frowning"],
         lines=[("이웃1", "젊은 사람이 이웃을 도둑 취급하네!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB2}, shaking his head, disappointed"],
         lines=[("이웃2", "총무님이 고생하는데, 너무하네.")]),
    # --- 회상: 한 달 전 ---
    dict(dur=3.0, sepia=True, photos=[f"{HAN} collecting cash envelopes door to door in a villa hallway, fake smile"],
         lines=[("한미숙", "이번 달부터 관리비 두 배예요~")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {HAN}, sweet fake smile"],
         lines=[("한미숙", "청소비가 올라서 그래요~ 현금으로 주세요.")]),
    dict(dur=3.0, sepia=True, photos=["dirty villa staircase with dust and trash, not cleaned for weeks, no people",
                                      f"close-up portrait of {JI}, suspicious, looking at a dirty staircase"],
         lines=[("지원", "청소비는 올랐는데… 계단은 왜 그대로지?")]),
    dict(dur=3.0, sepia=True, photos=[f"{HAN} coming out of a luxury department store with many shopping bags, happy"],
         lines=[("한미숙", "어머, 이 가방? 그냥 하나 샀어~")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{YO} standing up at the villa meeting holding a folder", f"close-up portrait of {YO}, calm, adjusting his glasses"],
         lines=[("3층 총각", "저 회계사입니다. 장부, 제가 같이 봐도 될까요?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, nervous, eyes darting"],
         lines=[("한미숙", "자, 장부는… 집에 두고 왔는데?")]),
    dict(dur=3.0, photos=["close-up of a bank statement paper with highlighted lines and a calculator, no people",
                          f"close-up portrait of {YO}, serious, pointing at a document"],
         lines=[("3층 총각", "청소 업체에 보낸 돈은 0원이네요.")]),
    dict(dur=3.0, photos=["close-up of a luxury handbag receipt next to a cash envelope, no people",
                          f"extreme close-up of {HAN}, shocked, mouth open!"],
         lines=[("3층 총각", "같은 날, 백화점에서 같은 금액이 결제됐고요.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {JI}, firm, looking straight"],
         lines=[("지원", "공금을 마음대로 쓰면, 횡령이 될 수 있어요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, desperate, flustered!"],
         lines=[("한미숙", "빌린 거야! 갚으려고 했어!")]),
    dict(dur=3.0, photos=[f"{NB1} and {NB2} glaring at {HAN}, villa meeting room", f"close-up portrait of {NB1}, furious"],
         lines=[("이웃1", "당장 돌려놔요! 총무도 내려놓고!")]),
    dict(dur=3.0, photos=[f"wide shot, {NB1} bowing apologetically to {JI}, two women in a villa hallway", f"close-up portrait of {JI}, gentle smile"],
         lines=[("이웃1", "지원 씨, 또 오해했네. 미안해요."), ("지원", "모두의 돈은 모두가 볼 수 있어야죠.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=["rooftop door of a korean villa locked with a heavy new padlock and chain, staircase, no people"],
         lines=[("이웃2", "어? 옥상 문이 왜 잠겨 있어?")]),
    dict(dur=3.0, flash=True, photos=[f"extreme close-up of {HAN}, sly smile, dangling a key"],
         lines=[("한미숙", "옥상은 이제 내 거야. 열쇠는 나만 있어~")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
