"""05편(4화): 쫓겨난 손자의 역습. make_karma.py에 EP=episodes/ep05.py 로 넘긴다."""

TITLE = ("후계자 쫓아내려던 손자", "이사회에서 벌어진 일")
END = ("다음 편", "손잡은 두 악녀?", "팔로우하고 다음 편 보기")
ROOM_TEXT = "한결그룹 이사회 회의실"

CHARS = {
    "madam": dict(hair=(40, 25, 20), style="bun", shirt=(25, 25, 30), pants=(25, 25, 30), bag=True),
    "taejun": dict(hair=(25, 25, 25), style="short", shirt=(245, 245, 245), pants=(40, 40, 55), tie=True, glasses=True),
    "police": dict(hair=(20, 20, 30), style="short", shirt=(30, 50, 110), pants=(30, 40, 80)),
    "doctor": dict(hair=(120, 120, 120), style="short", shirt=(240, 240, 245), pants=(80, 80, 90)),
}

# 캐릭터: (이름, x, 발y, 크기, 포즈, 표정, 왼쪽보기, 움직임)
S = [
    dict(dur=3.0, bg="room", fg=True, chars=[("seoyeon", 540, 1250, 0.95, "stand", "smile", False, "bob")],
         lines=[(None, "후계자로 발표된 서연. 그런데 첫 이사회 날…")]),
    dict(dur=3.5, bg="room", fg=True, zoom=(1.0, 1.1), chars=[("taejun", 330, 1250, 1.0, "point", "angry", False, "shake"),
                                                               ("seoyeon", 800, 1250, 0.9, "stand", "shock", True, None)],
         lines=[("태준", "이사님들, 이 여자는 사기꾼입니다!")]),
    dict(dur=4.5, bg="room", phone="post", post_site="한결대학병원 진단서",
         post_title="진단명: 중증 치매 / 환자: 한결그룹 회장", post_meta="담당의 서명 · 2026.11.24",
         post_body=["판단 능력 없음.", "최근 결정은 모두 무효로 볼 것."], post_likes=0, chars=[],
         lines=[("태준", "할머니는 치매예요. 이 여자가 정신없는 할머니를 이용한 거라고요!")]),
    dict(dur=4.0, bg="room", fg=True, chars=[("p1", 250, 1250, 0.85, "stand", "shock", False, None),
                                             ("p3", 560, 1250, 0.85, "stand", "angry", False, None),
                                             ("seoyeon", 870, 1250, 0.85, "stand", "sweat", True, "shake")],
         lines=[("이사1", "회장님이 치매라니…"), ("이사2", "어쩐지 이상하다 했어.")]),
    dict(dur=3.5, bg="room", fg=True, chars=[("madam", 330, 1250, 1.0, "stand", "smirk", False, None),
                                             ("taejun", 650, 1250, 1.0, "stand", "smirk", False, None)],
         lines=[("사모님", "자, 서연 씨 해임안 투표하시죠.")]),
    dict(dur=4.5, bg="room", fg=True, chars=[("p1", 200, 1250, 0.85, "point", "angry", False, None),
                                             ("p3", 470, 1250, 0.85, "point", "angry", False, None),
                                             ("seoyeon", 860, 1250, 0.9, "stand", "sweat", True, "shake")],
         lines=[("이사1", "찬성합니다."), ("이사2", "저도 찬성."), ("서연", "회장님은 치매가 아니에요…!")]),
    dict(dur=3.0, bg="room", fg=True, flash=True, zoom=(1.0, 1.15),
         chars=[("taejun", 300, 1250, 1.0, "shock", "shock", False, "shake"),
                ("grandma", 820, 1250, 1.0, "walk", "angry", True, ("slide", 300))],
         lines=[("회장", "누가 치매라고?")]),
    dict(dur=4.0, bg="room", fg=True, chars=[("taejun", 320, 1250, 1.0, "stand", "sweat", False, "shake"),
                                             ("grandma", 780, 1250, 1.0, "stand", "calm", True, None)],
         lines=[("회장", "태준아, 어젯밤 11시에 뭐 했는지 내가 말해줄까?")]),
    dict(dur=4.5, bg="room", phone="blackbox", bb_label="● REC  병원 주차장 CCTV  23:04",
         bb_chars=[("taejun", "help", "smirk", False, 0.5, 30, 300), ("doctor", "stand", "smirk", True, 0.5, 280, 300)],
         bb_circle=(20, 260, 560, 690), chars=[],
         lines=[("회장", "병원 원장한테 돈봉투 주고, 가짜 진단서 받았지.")]),
    dict(dur=4.5, bg="room", fg=True, chars=[("taejun", 330, 1250, 1.0, "point", "sweat", False, "shake"),
                                             ("madam", 700, 1250, 1.0, "shock", "shock", True, "shake")],
         lines=[("태준", "할머니, 그게… 엄마가 시킨 거예요!"), ("사모님", "너 이게 무슨 소리야!")]),
    dict(dur=3.5, bg="room", fg=True, chars=[("taejun", 330, 1250, 1.0, "shock", "shock", False, "shake"),
                                             ("police", 800, 1250, 1.0, "walk", "calm", True, ("slide", 300))],
         lines=[("경찰", "이태준 씨, 문서위조 혐의로 체포하겠습니다.")]),
    dict(dur=5.5, bg="room", fg=True, chars=[("p1", 180, 1250, 0.8, "stand", "sad", False, None),
                                             ("seoyeon", 480, 1250, 0.9, "stand", "smile", False, "bob"),
                                             ("grandma", 820, 1250, 0.95, "stand", "smile", True, "bob")],
         lines=[("이사1", "서연 씨, 저희가 오해했습니다…"), ("회장", "서연아, 이제 네가 이 회사를 지켜라.")]),
    dict(dur=4.5, bg="night", monitor="", chars=[("madam", 330, 1430, 1.0, "phone", "angry", False, "shake")],
         lines=[(None, "그날 밤, 혼자 남은 사모님이 누군가에게 전화를 걸었다."), ("사모님", "지민아… 이제 네 차례야.")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
