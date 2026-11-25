"""주차 빌런 참교육 1화. 실제 사람·장소와 무관한 지어낸 이야기. make_karma.py에 EP=episodes/parking01.py 로 넘긴다.
시리즈 주제: 배려 없이 사는 사람에게 상식을 알려준다. 완결 없이 매 화 다음 빌런 떡밥으로 끝낸다.
"""

TITLE = ("꼬깔 치우고 주차한 빌런", "CCTV 요구했다가 생긴 일")
END = ("다음 편", "두 번째 주차 빌런?", "팔로우하고 다음 편 보기")

CHARS = {
    "haeun": dict(hair=(60, 40, 30), style="long", shirt=(60, 150, 110), pants=(60, 60, 80)),
    "villain": dict(hair=(30, 30, 30), style="short", shirt=(230, 180, 30), pants=(30, 30, 30), glasses=True),
    "landlord": dict(hair=(200, 200, 205), style="short", shirt=(60, 70, 120), pants=(70, 70, 80), cane=True),
}

RED = (190, 30, 40)
GRAY = (120, 125, 130)

# 캐릭터: (이름, x, 발y, 크기, 포즈, 표정, 왼쪽보기, 움직임)
S = [
    dict(dur=3.5, bg="parking", cones=[300, 780], chars=[("haeun", 540, 1430, 0.95, "stand", "smile", False, "bob")],
         lines=[(None, "우리 건물 1층 주차장. 분명 세입자 전용인데…")]),
    dict(dur=4.0, bg="parking", cones=[120], chars=[("villain", 560, 1430, 1.0, "push", "angry", False, ("slide", -300))],
         lines=[(None, "매번 꼬깔을 치우고 차를 대는 사람이 있다."), ("최사장", "아 이거 뭐야, 거슬리게.")]),
    dict(dur=5.0, bg="parking", cars=[(540, RED, "12가 3456")], cones=[100],
         chars=[("haeun", 250, 1430, 0.95, "point", "normal", False, None),
                ("villain", 840, 1430, 1.0, "stand", "smirk", True, None)],
         lines=[("하은", "저기요, 여기 세입자 전용 주차장이에요."), ("최사장", "빈자리 있으면 대는 거지, 뭐 어때?")]),
    dict(dur=3.5, bg="parking", cars=[(540, RED, "12가 3456")], stones=[110, 970], cones=[60],
         chars=[], lines=[(None, "돌까지 갖다 놨지만… 다음 날 또.")]),
    dict(dur=4.5, bg="parking", cars=[(540, RED, "12가 3456")], zoom=(1.0, 1.12),
         chars=[("villain", 540, 1430, 1.05, "phone", "angry", False, "shake")],
         lines=[(None, "그리고 적반하장으로 전화가 왔다."), ("최사장", "여기 주차장에서 내 차 긁혔어요! CCTV 보여줘요!")]),
    dict(dur=5.0, bg="parking", cars=[(540, RED, "12가 3456")],
         chars=[("p2", 170, 1430, 0.85, "point", "angry", False, None),
                ("p1", 420, 1430, 0.85, "stand", "angry", False, None),
                ("haeun", 860, 1430, 0.95, "stand", "sweat", True, "shake")],
         lines=[("이웃1", "아가씨가 너무 야박하네~"), ("이웃2", "주차 좀 하게 해주지, 뭘 그래."),
                ("하은", "차 빼달라고 한 게 죄인가요…")]),
    dict(dur=3.5, bg="parking", cars=[(540, RED, "12가 3456")], flash=True, zoom=(1.0, 1.15),
         chars=[("villain", 280, 1430, 1.0, "stand", "smirk", False, None),
                ("landlord", 830, 1430, 1.0, "walk", "angry", True, ("slide", 300))],
         lines=[("건물주", "CCTV 보여달라고? 그래, 보여주지.")]),
    dict(dur=5.0, bg="parking", phone="blackbox", bb_label="● REC  1층 주차장 CCTV  22:17", bb_car=RED,
         bb_cones=[520], bb_chars=[("villain", "push", "smirk", False, 0.5, 30, 300)], bb_circle=(10, 260, 570, 690),
         chars=[], lines=[("건물주", "꼬깔 치우는 것도, 기둥에 혼자 긁는 것도 다 찍혔네요.")]),
    dict(dur=5.0, bg="parking", cars=[(540, RED, "12가 3456")],
         chars=[("villain", 300, 1430, 1.0, "stand", "sweat", False, "shake"),
                ("landlord", 800, 1430, 1.0, "point", "angry", True, None)],
         lines=[("최사장", "그, 그건…"), ("건물주", "무단주차에 허위 신고까지. 견인차 불렀습니다.")]),
    dict(dur=5.0, bg="parking", cones=[300, 780],
         chars=[("p2", 200, 1430, 0.85, "stand", "sad", False, None),
                ("haeun", 560, 1430, 0.95, "stand", "smile", False, "bob"),
                ("landlord", 880, 1430, 0.95, "stand", "smile", True, None)],
         lines=[("이웃1", "아가씨, 오해해서 미안해~"), ("하은", "남의 자리는 비워두는 게 상식이에요.")]),
    dict(dur=4.0, bg="parking", phone="comments", comments_head="댓글 8,412개",
         comments=["꼬깔 치우는 사람 진짜 있음", "상식이 없네 진짜", "건물주 사이다", "우리 동네에도 있다ㅠ",
                   "CCTV 요구한 게 자폭"], chars=[],
         lines=[(None, "그날 밤, 빨간 차는 견인됐다.")]),
    dict(dur=4.0, bg="parking", night_park=True, cars=[(540, GRAY, "")], cones=[90],
         chars=[], lines=[(None, "그런데 다음 날 새벽, 또 다른 차가 꼬깔을 치우고 있었다…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
