"""생활 민폐 빌런 5화: 구태만이 이사 왔다 (독서실 자리 맡기). 지어낸 이야기.

참조 스타일 시험판(STYLE="ref"): 제목 바 없음, 대사 한 줄에 그림 2~3장(빠른 컷), 얼굴 클로즈업 위주,
화면 아래 가운데 흰색 기울임 자막.
"""

STYLE = "ref"
TITLE = ("", "")
END = ("다음 편", "입주자 대표 구태만?", "팔로우하고 다음 편 보기")
PHOTO_STYLE = "realistic photo, korean drama still, cinematic lighting, shallow depth of field, sharp focus, high detail"

GU = "smug korean man in his 30s, slicked side-part hair, beige trench coat"
JI = "young korean man in his 20s, gray hoodie, kind face"
STU = "korean female high school student, long black hair, school uniform"
MGR = "korean apartment manager in his 50s, gray vest uniform, glasses"

S = [
    dict(dur=3.5, photos=[f"close-up portrait of {GU}, smug smirk, carrying a moving box, apartment hallway",
                          f"{GU} pushing a cart full of moving boxes into an apartment elevator"],
         lines=[(None, "새치기의 그 남자, 구태만이 이 아파트로 이사 왔다.")]),
    dict(dur=3.5, photos=[f"close-up portrait of {GU}, greedy grin, looking around a quiet apartment study room",
                          "close-up of a man's hand placing a leather bag on an empty wooden study desk"],
         lines=[("구태만", "독서실이 공짜라고? 자리부터 맡아야지.")]),
    dict(dur=3.5, photos=["row of empty study desks in a quiet reading room, a bag on every desk, nobody sitting",
                          f"back view of {GU} walking out through a glass door, hands in pockets"],
         lines=[(None, "가방 다섯 개로 자리 다섯 개를 맡고, 그는 사라졌다.")]),
    dict(dur=3.5, photos=[f"close-up portrait of {STU}, worried face, hugging textbooks",
                          "empty study desks with only bags on them, reading room, sad mood"],
         lines=[("수험생", "자리가 하나도 없네… 시험이 내일인데.")]),
    dict(dur=5.0, photos=[f"close-up portrait of {JI}, reading a notice on a bulletin board, serious",
                          f"{JI} carefully placing bags into lockers in a reading room",
                          f"close-up portrait of {STU}, grateful smile, sitting at a study desk"],
         lines=[("지훈", "30분 넘게 비운 자리는 정리해도 된대요."), (None, "지훈은 가방을 보관함에 조심스럽게 옮겼다.")]),
    dict(dur=3.5, photos=[f"extreme close-up of {GU}, furious face, shouting, veins on forehead",
                          f"{GU} pointing angrily at a young man in a gray hoodie, reading room"],
         lines=[("구태만", "누가 내 가방 만졌어! 너지? 도둑놈!")]),
    dict(dur=4.5, photos=["close-up of two middle-aged korean women whispering and glaring, apartment lobby",
                          f"close-up portrait of {JI}, nervous, sweating, unfairly accused"],
         lines=[("주민", "새로 온 총각이 남의 가방을 뒤졌대."), ("지훈", "저는 규칙대로 했을 뿐인데…")]),
    dict(dur=3.5, flash=True, photos=[f"close-up portrait of {MGR}, serious expression, holding a tablet",
                                      "close-up of a tablet screen showing an access log table with times"],
         lines=[("관리소장", "잠깐만요. 출입 기록 확인했습니다.")]),
    dict(dur=6.0, photos=[f"close-up portrait of {MGR}, calm and firm, looking at someone",
                          f"extreme close-up of {GU}, shocked, eyes wide, mouth open",
                          f"close-up portrait of {GU}, sweating, speechless, embarrassed"],
         lines=[("관리소장", "구태만 씨, 아침 7시에 들어와 1분 만에 나가셨네요."),
                ("관리소장", "자리만 맡고 여섯 시간 비우셨어요."), ("관리소장", "규정상 한 달 이용 정지입니다.")]),
    dict(dur=4.5, photos=[f"close-up portrait of {GU}, flustered, making excuses",
                          "close-up of korean apartment residents laughing and pointing, lobby"],
         lines=[("구태만", "아니, 바쁜 사람이 먼저지!"), ("주민", "바쁘면 줄을 서세요!")]),
    dict(dur=3.5, photos=[f"close-up portrait of {JI}, calm confident smile",
                          f"{STU} studying happily at a desk in a bright reading room"],
         lines=[("지훈", "자리는 맡는 게 아니라, 쓰는 거예요.")]),
    dict(dur=4.0, flash=True, photos=["a paper notice with a man's photo taped on an apartment elevator wall, close-up",
                                      f"close-up portrait of {GU}, sly smile, giving a thumbs up"],
         lines=[(None, "그런데 며칠 뒤, 엘리베이터에 붙은 공고."), (None, "입주자 대표 후보… 구태만?!")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
