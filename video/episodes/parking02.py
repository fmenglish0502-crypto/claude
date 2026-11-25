"""주차 빌런 참교육 2화: '잠깐이면 돼요' 이중주차 빌런. 지어낸 이야기."""

TITLE = ("\"잠깐이면 돼요\" 이중주차 빌런", "8시간 갇힌 사연")
END = ("다음 편", "충전 자리 빌런?", "팔로우하고 다음 편 보기")

CHARS = {
    "haeun": dict(hair=(60, 40, 30), style="long", shirt=(60, 150, 110), pants=(60, 60, 80)),
    "yang": dict(hair=(110, 60, 40), style="bun", shirt=(200, 60, 140), pants=(50, 50, 60), bag=True, glasses=True),
    "landlord": dict(hair=(200, 200, 205), style="short", shirt=(60, 70, 120), pants=(70, 70, 80), cane=True),
    "mover": dict(hair=(30, 30, 30), style="short", shirt=(40, 90, 170), pants=(50, 50, 60)),
}
GRAY, BLUE, WHITE = (120, 125, 130), (40, 70, 160), (235, 235, 240)

S = [
    dict(dur=3.5, bg="parking", night_park=True, cars=[(540, GRAY, "34나 7788")], cones=[90],
         chars=[], lines=[(None, "새벽에 꼬깔을 치운 회색 차. 주인은 양여사였다.")]),
    dict(dur=4.0, bg="parking", cars=[(380, WHITE, "하은 차"), (760, GRAY, "34나 7788")],
         chars=[("haeun", 900, 1430, 0.9, "stand", "shock", True, None)],
         lines=[(None, "하은의 차 앞을 딱 막은 이중주차."), ("하은", "출근해야 하는데…")]),
    dict(dur=3.5, bg="parking", phone="post", post_site="차 앞유리 메모", post_title="잠깐이면 돼요^^ 금방 뺄게요",
         post_meta="010-****-**** (연락 주세요)", post_body=["…라고 적혀 있었다."], chars=[],
         lines=[(None, "앞유리엔 메모 한 장.")]),
    dict(dur=5.0, bg="parking", cars=[(380, WHITE, "하은 차"), (760, GRAY, "34나 7788")],
         chars=[("haeun", 900, 1430, 0.9, "phone", "sweat", True, "shake")],
         lines=[("하은", "차 좀 빼주세요, 지각이에요!"), ("양여사", "아유, 지금 미용실이라 못 가요~ 택시 타요!")]),
    dict(dur=5.0, bg="parking", cars=[(760, GRAY, "34나 7788")],
         chars=[("p2", 170, 1430, 0.85, "point", "angry", False, None),
                ("p1", 420, 1430, 0.85, "stand", "smirk", False, None),
                ("haeun", 650, 1430, 0.9, "stand", "sad", False, None)],
         lines=[("이웃1", "잠깐인데 좀 봐주지, 예민하네~"), ("이웃2", "아가씨가 택시 타면 되지 뭘.")]),
    dict(dur=4.0, bg="parking", cars=[(760, GRAY, "34나 7788")],
         chars=[("landlord", 300, 1430, 0.95, "stand", "calm", False, None)],
         lines=[(None, "그날 오후, 건물주 할아버지에게 전화가 왔다."), ("건물주", "오늘 1층에 새 세입자 이삿짐 들어와요.")]),
    dict(dur=4.5, bg="parking", flash=True, cars=[(760, GRAY, "34나 7788"), (300, BLUE, "이삿짐센터")],
         chars=[("mover", 520, 1430, 0.9, "stand", "smile", False, None)],
         lines=[(None, "회색 차 바로 뒤에 선 5톤 이삿짐 트럭."), ("이삿짐기사", "8시간 작업입니다~")]),
    dict(dur=4.0, bg="parking", phone="post", post_site="트럭 앞유리 메모", post_title="잠깐이면 돼요^^ 8시간 뒤에 뺄게요",
         post_meta="이삿짐센터 (작업 중엔 통화 어려움)", post_body=["…라고 적혀 있었다."], chars=[],
         lines=[(None, "트럭 앞유리에도 메모 한 장.")]),
    dict(dur=5.0, bg="parking", cars=[(760, GRAY, "34나 7788"), (300, BLUE, "이삿짐센터")],
         chars=[("yang", 540, 1430, 1.0, "phone", "angry", False, "shake")],
         lines=[("양여사", "차 빼요! 나 딸 상견례 가야 된다고!"), ("이삿짐기사", "아유, 지금 작업 중이라 못 가요~ 택시 타세요!")]),
    dict(dur=4.0, bg="parking", cars=[(760, GRAY, "34나 7788"), (300, BLUE, "이삿짐센터")],
         chars=[("yang", 540, 1430, 1.0, "stand", "sweat", False, "shake")],
         lines=[(None, "결국 상견례엔 두 시간 지각."), ("양여사", "사돈댁이… 화가 많이 나셨대…")]),
    dict(dur=5.0, bg="parking", cones=[300, 780],
         chars=[("p2", 200, 1430, 0.85, "stand", "sad", False, None),
                ("haeun", 540, 1430, 0.95, "stand", "smile", False, "bob"),
                ("landlord", 880, 1430, 0.95, "stand", "smile", True, None)],
         lines=[("이웃1", "잠깐이 그렇게 길 줄 몰랐네…"), ("하은", "남의 잠깐은, 내 하루일 수도 있어요.")]),
    dict(dur=4.0, bg="parking", phone="comments", comments_head="댓글 11,207개",
         comments=["잠깐이면 돼요 메모 레전드ㅋㅋ", "똑같이 당하니까 사이다", "이중주차 진짜 극혐", "이삿짐 기사님 최고",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 이후 회색 차는 다시 오지 않았다.")]),
    dict(dur=4.0, bg="parking", night_park=True, cars=[(540, (60, 60, 65), "")],
         chars=[], lines=[(None, "그런데 건물 앞 전기차 충전 자리에, 매일 서 있는 기름차가…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
