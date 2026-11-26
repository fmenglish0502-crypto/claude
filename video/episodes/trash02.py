"""종량제 봉투 빌런 2화: 건물주 언니의 등장 (보복 퇴거 협박). 지어낸 이야기.

1화 떡밥("이 빌라, 우리 언니 건물인 거 몰랐지?")을 받는다. 건물주 한미자가 동생 편을 들며 지원에게 나가라고 한다.
사이다: 세입자의 계약 갱신 요구 + "실거주"라더니 부동산 앱에 매물을 올려둔 증거. 법 대사는 단정 대신 "~할 수 있다" 수준.
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("종량제 빌런", "2부")
END = ("3부 예고", "빌라 관리비의 비밀?", "팔로우하고 다음 편 보기")

HAN = "middle-aged korean woman in her late 50s, wrinkled aged face, sagging cheeks, short curly permed hair, leopard print blouse"
MJ = "rich elderly korean woman in her 60s, wrinkled face, elegant gray bob hair, fur coat, pearl earrings, arrogant"
JI = "korean woman in her 20s, long straight black hair, white shirt"
NB1 = "elderly korean woman in her late 60s, wrinkled face, gray streaked short permed hair, purple blouse"
AG = "kind korean man in his 40s, real estate agent, navy suit, glasses"

S = [
    # --- 첫 장면: 대화 훅 ---
    dict(dur=3.0, photos=[f"{MJ} glaring down at {JI} at a villa doorway, tense confrontation",
                          f"close-up portrait of {MJ}, cold arrogant glare, single person!*"],
         lines=[("한미자", "우리 동생 과태료 물게 한 게 너야?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, nervous but standing firm"],
         lines=[("지원", "잘못은 동생분이 하셨잖아요.")]),
    dict(dur=3.0, photos=[f"{MJ} throwing a document at the floor in front of {JI}", f"close-up portrait of {MJ}, shouting!"],
         lines=[("한미자", "계약 끝나면 나가! 연장은 꿈도 꾸지 마!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, smug grin behind her sister"],
         lines=[("한미숙", "그러게 왜 건드렸어~")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB1}, worried whisper, villa hallway"],
         lines=[("이웃1", "괜히 건드렸다가 쫓겨나게 생겼네…")]),
    # --- 지원의 사정 ---
    dict(dur=3.0, photos=[f"{JI} sitting alone in a small tidy studio apartment at night, looking at a lease contract",
                          "close-up of a korean lease contract document on a table, pen, no people"],
         lines=[("지원", "2년 동안 월세 한 번 안 밀렸는데…")]),
    dict(dur=3.0, photos=[f"close-up portrait of {JI}, determined, reading on a smartphone"],
         lines=[("지원", "세입자는 계약 갱신을 요구할 수 있다고 했어.")]),
    # --- 다음 날: 언니의 두 번째 공격 ---
    dict(dur=3.0, flash=True, photos=[f"{MJ} smirking and holding a paper notice at the villa entrance", f"close-up portrait of {MJ}, smug"],
         lines=[("한미자", "갱신? 거절이야. 내가 직접 들어와 살 거니까!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, shocked, mouth open"],
         lines=[("지원", "집주인이 직접 살면… 거절할 수 있잖아.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, laughing loudly!"],
         lines=[("한미숙", "짐 싸~ 1층 아가씨!")]),
    # --- 사이다 ---
    dict(dur=3.0, photos=[f"{JI} entering a bright real estate office, {AG} at the desk",
                          f"close-up portrait of {AG}, surprised, looking at a computer monitor"],
         lines=[("중개사", "어? 이 집, 어제 매물로 올라왔는데요?")]),
    dict(dur=3.0, photos=["close-up of a smartphone screen showing a real estate listing app with an apartment photo and price, no people",
                          f"close-up portrait of {JI}, eyes narrowing, realizing"],
         lines=[("지원", "직접 산다면서… 다른 사람한테 세를 놓으시려고요?")]),
    dict(dur=3.0, flash=True, photos=[f"{JI} showing a smartphone screen to {MJ} at the villa entrance, neighbors watching",
                                      f"extreme close-up of {MJ}, shocked, eyes wide!"],
         lines=[("지원", "거짓 실거주로 쫓아내면, 손해배상을 청구할 수 있어요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {MJ}, flustered, stammering, sweating"],
         lines=[("한미자", "그, 그건 그냥 시세 알아본 거야!")]),
    dict(dur=2.5, photos=[f"{NB1} and an old korean man in a cardigan glaring at {MJ}, villa entrance"],
         lines=[("이웃1", "세입자 쫓아내려고 별짓을 다 하네!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {MJ}, defeated, biting her lip", f"close-up portrait of {JI}, calm confident smile"],
         lines=[("한미자", "…계약, 연장해 줄게."), ("지원", "법대로 하시면 돼요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=["close-up of a paper notice on a villa bulletin board about maintenance fee increase, no people"],
         lines=[("이웃1", "지원 씨, 게시판에 이상한 공고 붙었어!")]),
    dict(dur=3.0, flash=True, photos=[f"extreme close-up of {HAN}, evil smirk, holding a cash envelope"],
         lines=[("한미숙", "관리비는 이제 내가 걷을 거야. 총무니까~")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
