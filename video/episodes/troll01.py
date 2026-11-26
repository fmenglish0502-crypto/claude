"""악플러 1부: 매일 악플 달다가 고소당한 '정의의칼'. 지어낸 이야기. 대본: scripts/series-batch-01.md 4번.
대화 위주(내레이션 0줄). 첫 장면 맞붙기 → 회상 → 고소 사이다 → 떡밥(영상 도둑 채널).
게시 제목 안(바이럴 공식: 가해 행동 + 반전 장치 한마디/한 장): "매일 밤 악플 달던 '정의의칼', 경찰서에서 이름 불리자 얼굴이 굳었다"
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")

PART = ("악플러 참교육", "1부")
END = ("2부 예고", "영상 도둑 채널의 정체?", "팔로우하고 다음 편 보기")

SO = "korean woman in her late 20s, shoulder-length wavy brown hair, cream knit sweater, small silver earrings"
CHOI = "thin korean man in his mid 20s, messy short black hair, dark circles under eyes, gray hoodie"
FR = "korean woman in her 20s, high ponytail, denim jacket"
LAW = "korean female lawyer in her 40s, short bob hair, black suit, white blouse"
COP = "korean police detective in his 50s, short gray buzz cut, white shirt, loosened tie"
SERA = "korean woman in her 30s, bleached blonde long hair, heavy makeup, pink tracksuit"
YUN = "korean man in his 50s, neatly combed silver hair, three-piece navy suit, gold rimmed glasses"

S = [
    # --- 첫 장면: 맞붙기 ---
    dict(dur=3.0, photos=[f"{SO} confronting {CHOI} face to face in a police station hallway, tense",
                          f"close-up portrait of {CHOI}, smug sneer, single person!*"],
         lines=[("최도윤", "익명인데 네가 어쩔 건데?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SO}, cold calm stare, single person"],
         lines=[("소담", "이제 익명 아니잖아요. 최도윤 씨.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {CHOI}, shocked, eyes wide, single person!"],
         lines=[("최도윤", "내… 내 이름을 어떻게?!")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{CHOI} typing on a keyboard in a dark messy room, face lit by monitor glow",
                                      f"close-up portrait of {CHOI}, evil grin in monitor light, single person"],
         lines=[("최도윤", "오늘은 누구를 혼내 줄까~")]),
    dict(dur=3.0, sepia=True, photos=["close-up of a computer screen full of hateful comments in a video site comment section, no people"],
         lines=[("최도윤", "얼굴 보기 싫다. 유튜브 접어라.")]),
    dict(dur=3.0, sepia=True, photos=[f"{SO} sitting alone on her bed at night looking at a smartphone, tears",
                                      f"close-up portrait of {SO}, crying, single person"],
         lines=[("소담", "내가… 뭘 잘못했지…")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {FR}, worried, single person"],
         lines=[("하린", "소담아, 댓글 그만 봐. 너 요즘 잠도 못 자잖아.")]),
    dict(dur=2.5, sepia=True, photos=["close-up of a smartphone screen showing many comments piling up, no people"],
         lines=[("시청자", "멘탈 약하면 유튜브 하지 마~")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{SO} and {LAW} at a law office desk with printed screenshots",
                                      f"close-up portrait of {LAW}, confident, single person"],
         lines=[("서변호사", "캡처 다 모으셨죠? 모욕·명예훼손으로 고소할 수 있어요.")]),
    dict(dur=3.0, photos=["close-up of an official police summons letter envelope on a doormat, no people",
                          f"close-up portrait of {CHOI}, pale, holding a letter, single person"],
         lines=[("최도윤", "경찰서… 출석 요구서?")]),
    dict(dur=3.0, photos=[f"{COP} sitting across {CHOI} in a police interrogation room",
                          f"close-up portrait of {COP}, stern, single person"],
         lines=[("형사", "닉네임 정의의칼. 작성한 댓글 수백 개 확인됐습니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {CHOI}, sweating, nervous smile, single person"],
         lines=[("최도윤", "그냥… 장난이었어요.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {SO}, firm, single person"],
         lines=[("소담", "장난이라면서, 사과는 한 번도 안 하셨죠.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {CHOI}, desperate, begging, single person!"],
         lines=[("최도윤", "합의해 주세요! 저 취업도 했단 말이에요!")]),
    dict(dur=3.0, photos=[f"{CHOI} answering a phone call on the street, devastated",
                          f"close-up portrait of {CHOI}, stunned, phone at ear, single person"],
         lines=[("최도윤", "네? 합격… 취소라고요?")]),
    dict(dur=3.0, photos=[f"{SO} smiling at a camera in a bright cozy filming room, ring light",
                          f"close-up portrait of {SO}, warm smile, single person"],
         lines=[("소담", "화면 뒤에도 사람이 있어요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=["close-up of a smartphone screen showing two identical video thumbnails side by side, no people",
                          f"close-up portrait of {FR}, shocked, single person"],
         lines=[("하린", "소담아! 네 영상이랑 똑같은 게 올라왔어!")]),
    dict(dur=3.0, flash=True, photos=[f"close-up portrait of {SERA}, sly smirk, ring light behind, single person"],
         lines=[("오세라", "조회수는 먼저 올린 사람이 임자야~")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")

