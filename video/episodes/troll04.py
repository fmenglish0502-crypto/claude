"""악플러 4부: 돌아온 최도윤이 윤대표 지시로 소담 집 주소를 퍼뜨린다(신상털기). 이웃들은 "유튜버 때문에 시끄럽다" 원망.
사이다: 형사 — 신상 공개·따라다니기는 처벌될 수 있다 + 윤대표 지시 메시지 증거. 떡밥: 윤대표 뒤의 더 큰 손(5부).
게시 제목 안(바이럴 공식: 가해 행동 + 반전 장치 한마디/한 장): "유튜버 집 주소 퍼뜨린 악플러, 형사가 보여준 메시지 한 줄에 무너졌다"
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")

PART = ("악플러 참교육", "4부")
END = ("5부 예고", "윤대표 뒤의 진짜 보스?", "팔로우하고 다음 편 보기")

SO = "korean woman in her late 20s, shoulder-length wavy brown hair, cream knit sweater, small silver earrings"
CHOI = "thin korean man in his mid 20s, messy short black hair, dark circles under eyes, gray hoodie"
FR = "korean woman in her 20s, high ponytail, denim jacket"
LAW = "korean female lawyer in her 40s, short bob hair, black suit, white blouse"
COP = "korean police detective in his 50s, short gray buzz cut, white shirt, loosened tie"
SERA = "korean woman in her 30s, bleached blonde long hair, heavy makeup, pink tracksuit"
YUN = "korean man in his 50s, neatly combed silver hair, three-piece navy suit, gold rimmed glasses"

NB = "korean woman in her 50s, short permed hair, apron, annoyed"
S = [
    dict(dur=3.0, photos=[f"{NB} scolding {SO} at an apartment entrance, crowd of strangers with phones behind",
                          f"upper body portrait of {NB}, irritated, yelling, single person, solo!"],
         lines=[("아주머니", "유튜버 아가씨 때문에 동네가 난리잖아!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SO}, scared, single person"],
         lines=[("소담", "저도… 제 주소가 왜 퍼졌는지 몰라요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB}, crossing arms, single person"],
         lines=[("아주머니", "그러게 왜 얼굴 팔고 다녀?")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{CHOI} in a dark room comparing a video frame of a window view with a map on his monitor",
                                      f"close-up portrait of {CHOI}, creepy smile in monitor glow, single person"],
         lines=[("최도윤", "창밖 간판 하나면… 주소 나오지.")]),
    dict(dur=3.0, sepia=True, photos=["close-up of a computer screen showing an anonymous online post with a blurred apartment photo and address, no people"],
         lines=[("최도윤", "소담 집 여기임. 놀러 가실 분~")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {SO}, terrified, peeking through curtains at night, single person"],
         lines=[("소담", "누가… 계속 문을 두드려.")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {FR}, alarmed, on the phone, single person"],
         lines=[("하린", "소담아, 당장 신고해! 혼자 있지 마!")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{COP} knocking on a dark apartment door with officers behind him",
                                      f"close-up portrait of {COP}, stern, single person"],
         lines=[("형사", "최도윤 씨, 또 뵙네요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {CHOI}, panicked, single person!"],
         lines=[("최도윤", "저, 저는 글만 올렸어요!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {COP}, firm, holding a document, single person"],
         lines=[("형사", "남의 주소를 퍼뜨리고 따라다니게 하면, 처벌받을 수 있습니다.")]),
    dict(dur=3.0, photos=["close-up of a smartphone screen showing a chat message conversation, no people",
                          f"upper body portrait of {COP}, serious, showing a phone, single person, solo"],
         lines=[("형사", "윤대표랑 나눈 메시지도 다 확인했고요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {CHOI}, desperate, single person"],
         lines=[("최도윤", "대표님이 시킨 거예요! 저는 돈만…")]),
    dict(dur=3.0, photos=[f"{YUN} being escorted out of his luxury office by detectives, reporters flashing cameras",
                          f"close-up portrait of {YUN}, humiliated, hiding face, single person"],
         lines=[("윤대표", "변호사 불러! 나 누군지 알아?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB}, apologetic, single person"],
         lines=[("아주머니", "아가씨… 우리가 몰라서 그랬어. 미안해.")]),
    dict(dur=3.0, photos=[f"{SO} standing at her apartment entrance with neighbors, morning sunlight",
                          f"close-up portrait of {SO}, brave smile, single person"],
         lines=[("소담", "화면 밖의 내 삶도, 함부로 침범할 수 없어요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{YUN} in a police car making a whispered phone call"],
         lines=[("윤대표", "회장님… 일이 커졌습니다.")]),
    dict(dur=3.0, flash=True, photos=["close-up of a man's hand with a heavy gold ring holding a phone in a dark luxury room, no face"],
         lines=[("그 회장", "그 유튜버, 내가 직접 만나 보지.")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")

