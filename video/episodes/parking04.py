"""주차 빌런 참교육 4화: 몇 달째 방치된 캠핑카. 주인은 1화의 최사장. 지어낸 이야기."""

TITLE = ("주차장에 캠핑카 버려둔 주인", "알고 보니 그 사람이었다")
END = ("다음 편", "최사장의 복수?", "팔로우하고 다음 편 보기")

CHARS = {
    "haeun": dict(hair=(60, 40, 30), style="long", shirt=(60, 150, 110), pants=(60, 60, 80)),
    "villain": dict(hair=(30, 30, 30), style="short", shirt=(230, 180, 30), pants=(30, 30, 30), glasses=True),
    "landlord": dict(hair=(200, 200, 205), style="short", shirt=(60, 70, 120), pants=(70, 70, 80), cane=True),
    "officer": dict(hair=(30, 30, 30), style="long", shirt=(70, 110, 160), pants=(50, 50, 60)),
}
CAMPER = (235, 235, 230)

S = [
    dict(dur=3.5, bg="parking", cars=[(540, CAMPER, "")],
         chars=[], lines=[(None, "주차장 한 칸을 몇 달째 차지한 하얀 캠핑카.")]),
    dict(dur=4.5, bg="parking", cars=[(540, CAMPER, "")],
         chars=[("haeun", 880, 1430, 0.9, "stand", "sweat", True, None)],
         lines=[(None, "연락처도 없고, 먼지만 쌓여갔다."), ("하은", "이 차 주인은 대체 누구지…")]),
    dict(dur=4.5, bg="parking", cars=[(540, CAMPER, "")],
         chars=[("p1", 200, 1430, 0.85, "stand", "smirk", False, None),
                ("p2", 450, 1430, 0.85, "point", "angry", False, None),
                ("haeun", 820, 1430, 0.9, "stand", "sad", True, None)],
         lines=[("이웃1", "캠핑카 하나 가지고 뭘 그래~"), ("이웃2", "아가씨는 동네 정이 없어.")]),
    dict(dur=4.5, bg="parking", cars=[(540, CAMPER, "")],
         chars=[("landlord", 300, 1430, 0.95, "stand", "angry", False, None),
                ("officer", 780, 1430, 0.95, "stand", "calm", True, None)],
         lines=[("건물주", "구청에 장기 방치 차량으로 신고했어요."), ("구청직원", "공고 붙이고, 기간 지나면 강제 견인합니다.")]),
    dict(dur=4.0, bg="parking", phone="post", post_site="구청 공고문", post_title="장기 방치 차량 자진 처리 명령",
         post_meta="기한 내 미처리 시 강제 견인·처분", post_body=["차량 소유자는 즉시 연락 바랍니다."], chars=[],
         lines=[(None, "캠핑카 앞유리에 붙은 공고문.")]),
    dict(dur=3.5, bg="parking", flash=True, cars=[(540, CAMPER, "")],
         chars=[("villain", 840, 1430, 1.0, "walk", "angry", True, ("slide", 300))],
         lines=[(None, "기한 마지막 날, 드디어 나타난 주인은…")]),
    dict(dur=4.5, bg="parking", zoom=(1.0, 1.15), cars=[(540, CAMPER, "")],
         chars=[("haeun", 250, 1430, 0.9, "stand", "shock", False, None),
                ("villain", 840, 1430, 1.0, "point", "angry", True, "shake")],
         lines=[("하은", "최사장님?!"), ("최사장", "내 캠핑카 누가 신고했어! 견인당하면 책임질 거야?")]),
    dict(dur=5.0, bg="parking", phone="blackbox", bb_label="● REC  1층 주차장 CCTV  03:12", bb_car=CAMPER,
         bb_chars=[("villain", "push", "smirk", False, 0.5, 30, 300)], bb_circle=(10, 260, 570, 690), chars=[],
         lines=[("건물주", "견인되고 나서 새벽에 몰래 갖다 놓은 거, 다 찍혔어요.")]),
    dict(dur=5.0, bg="parking", cars=[(540, CAMPER, "")],
         chars=[("villain", 300, 1430, 1.0, "stand", "sweat", False, "shake"),
                ("officer", 800, 1430, 0.95, "point", "calm", True, None)],
         lines=[("구청직원", "기한 지났습니다. 강제 견인하고, 보관료도 청구됩니다."), ("최사장", "보관료까지…?!")]),
    dict(dur=5.0, bg="parking", cones=[300, 780],
         chars=[("p2", 200, 1430, 0.85, "stand", "sad", False, None),
                ("haeun", 540, 1430, 0.95, "stand", "smile", False, "bob"),
                ("landlord", 880, 1430, 0.95, "stand", "smile", True, None)],
         lines=[("이웃2", "아가씨, 정 없다고 해서 미안해."), ("하은", "주차장은 창고가 아니에요.")]),
    dict(dur=4.0, bg="parking", phone="comments", comments_head="댓글 16,033개",
         comments=["최사장 또 너야?ㅋㅋㅋ", "캠핑카 방치 진짜 민폐", "보관료 폭탄 사이다", "하은 씨 고생 많다",
                   "최사장 복수 예고 무섭다"], chars=[], lines=[(None, "견인차에 실려 가는 캠핑카를 보며, 최사장이 중얼거렸다.")]),
    dict(dur=4.0, bg="parking", night_park=True, chars=[("villain", 540, 1430, 1.0, "phone", "angry", False, "shake")],
         lines=[("최사장", "두고 봐… 이번엔 건물을 통째로 사버릴 테니까.")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
