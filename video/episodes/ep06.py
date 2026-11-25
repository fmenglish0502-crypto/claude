"""06편(5화): 손잡은 두 악녀. make_karma.py에 EP=episodes/ep06.py 로 넘긴다."""

TITLE = ("두 악녀의 AI 조작 영상", "회장님의 마지막 한 수")
END = ("다음 편", "할아버지의 정체?", "팔로우하고 다음 편 보기")
LOBBY_TEXT = "한결그룹 기자회견장"

CHARS = {
    "madam": dict(hair=(40, 25, 20), style="bun", shirt=(25, 25, 30), pants=(25, 25, 30), bag=True),
    "police": dict(hair=(20, 20, 30), style="short", shirt=(30, 50, 110), pants=(30, 40, 80)),
    "grandpa": dict(hair=(210, 210, 210), style="short", shirt=(140, 100, 70), pants=(80, 70, 60), cane=True),
}

# 캐릭터: (이름, x, 발y, 크기, 포즈, 표정, 왼쪽보기, 움직임)
S = [
    dict(dur=5.0, bg="night", monitor="AI 합성중…", chars=[("madam", 250, 1430, 0.95, "phone", "smirk", False, None),
                                                          ("jimin", 560, 1430, 0.95, "stand", "smirk", True, None)],
         lines=[(None, "손잡은 두 악녀. 그들의 마지막 계획은…"), ("사모님", "서연이가 회장님 미는 영상, 만들 수 있지?"),
                ("지민", "AI로 하면 5분이면 돼요.")]),
    dict(dur=3.5, bg="night", monitor="", phone="views", feed_title="[단독] 새 후계자 회장 폭행 영상",
         feed_views=5200000, feed_comments=["와 소름", "은혜를 원수로 갚네", "후계자 자격 없다"], chars=[],
         lines=[(None, "다음 날, 충격적인 영상이 퍼졌다.")]),
    dict(dur=5.0, bg="lobby", chars=[("p1", 150, 1450, 0.85, "phone", "angry", False, "bob"),
                                     ("p2", 380, 1450, 0.85, "point", "angry", False, "shake"),
                                     ("seoyeon", 840, 1430, 0.95, "stand", "sweat", True, "shake")],
         lines=[("기자1", "영상 속 사람, 서연 씨 맞습니까?"), ("기자2", "회장님 폭행 인정하세요!"),
                ("서연", "저는 절대 그런 적 없어요…!")]),
    dict(dur=4.0, bg="lobby", zoom=(1.0, 1.1), chars=[("madam", 330, 1430, 1.0, "stand", "smirk", False, None),
                                                       ("jimin", 680, 1430, 1.0, "stand", "smirk", True, None)],
         lines=[("사모님", "이제 끝이네, 후계자님."), ("지민", "그때 내 기분, 이제 알겠지?")]),
    dict(dur=3.0, bg="lobby", flash=True, zoom=(1.0, 1.15),
         chars=[("jimin", 300, 1430, 1.0, "shock", "shock", False, "shake"),
                ("grandma", 820, 1430, 1.0, "walk", "angry", True, ("slide", 300))],
         lines=[("회장", "그 영상 속 할머니가 나라고?")]),
    dict(dur=4.0, bg="lobby", chars=[("seoyeon", 330, 1430, 0.95, "stand", "shock", False, None),
                                     ("grandma", 780, 1430, 1.0, "stand", "calm", True, None)],
         lines=[("회장", "나는 그날 하루 종일 병원에 있었다. 진료 기록도 있지.")]),
    dict(dur=4.5, bg="lobby", phone="post", post_site="AI 합성 감정 결과",
         post_title="해당 영상: AI 합성 확률 99.8%", post_meta="한결그룹 보안팀 · 원본 파일 분석",
         post_body=["얼굴 합성 흔적 발견.", "최초 업로드 계정: jimin_official"], chars=[],
         lines=[("회장", "그리고 이 영상, 처음 올린 계정이 누구더라?")]),
    dict(dur=5.0, bg="lobby", chars=[("p1", 140, 1450, 0.85, "point", "angry", False, None),
                                     ("jimin", 450, 1430, 1.0, "point", "sweat", False, "shake"),
                                     ("madam", 800, 1430, 1.0, "shock", "shock", True, "shake")],
         lines=[("기자1", "지민 씨, 해명하세요!"), ("지민", "사, 사모님이 시킨 거예요!"), ("사모님", "너까지 이러기야?!")]),
    dict(dur=3.5, bg="lobby", chars=[("jimin", 250, 1430, 0.95, "stand", "sad", False, None),
                                     ("madam", 500, 1430, 0.95, "stand", "sad", False, None),
                                     ("police", 830, 1430, 1.0, "walk", "calm", True, ("slide", 300))],
         lines=[("경찰", "허위 영상 유포 혐의로 두 분 모두 같이 가시죠.")]),
    dict(dur=5.5, bg="lobby", chars=[("jimin", 330, 1430, 0.95, "stand", "sad", False, None),
                                     ("grandma", 780, 1430, 1.0, "stand", "calm", True, None)],
         lines=[("지민", "회장님… 저도 다시 시작할 수 있을까요?"),
                ("회장", "버스 정류장에서 쓰러진 사람 일으켜 세우는 것부터 해봐라.")]),
    dict(dur=4.0, bg="bus", chars=[("grandpa", 280, 1460, 0.9, "fall", "sad", False, None),
                                   ("jimin", 840, 1430, 0.95, "help", "smile", True, ("slide", 250))],
         lines=[(None, "몇 달 뒤, 그 버스 정류장."), ("지민", "할아버지, 괜찮으세요?")]),
    dict(dur=4.5, bg="bus", chars=[("seoyeon", 330, 1430, 0.95, "stand", "smile", False, "bob"),
                                   ("grandma", 740, 1430, 0.95, "stand", "smile", True, "bob")],
         lines=[("서연", "회장님, 저기 지민 씨…"), ("회장", "사람은 변할 수 있는 거다.")]),
    dict(dur=4.5, bg="lobby", phone="comments", comments_head="댓글 102,394개",
         comments=["1화랑 이어지는 거 소름", "지민 성장 서사 미쳤다", "회장님 명언",
                   "근데 저 할아버지 누구야??", "다음 편 빨리요"], chars=[],
         lines=[(None, "할머니를 밀쳤던 지민이, 이번엔 할아버지를 일으켜 세웠다. 그런데 그 할아버지는…")]),
    dict(dur=3.5, bg="dark", end=True, chars=[], lines=[]),
]
