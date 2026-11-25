"""생활 민폐 빌런 3화: 복도에 짐 쌓는 이웃. 지어낸 이야기."""

TITLE = ("공용 복도를 창고로 쓰던 이웃", "소방 점검 날 생긴 일")
END = ("다음 편", "남의 택배 뜯는 이웃?", "팔로우하고 다음 편 보기")

JANG = "stubborn korean man in his 50s, bald head, gray tracksuit, standing in front of piled boxes in an apartment hallway"

S = [
    dict(dur=3.5, bg="dark", photo=f"{JANG}, arms crossed, hallway crowded with boxes, bicycles and an old refrigerator", move="zoomin",
         lines=[(None, "공용 복도를 자기 창고처럼 쓰는 남자, 장씨.")]),
    dict(dur=4.5, bg="dark", photo="young korean mother pushing a baby stroller, stuck between boxes in a narrow apartment hallway", move="shake",
         lines=[("엄마", "유모차가 안 지나가요…"), ("장씨", "옆으로 살살 지나가면 되지.")]),
    dict(dur=4.0, bg="dark", photo="apartment fire exit door blocked by a stack of boxes and an old cabinet, warning sign covered", move="zoomin",
         lines=[(None, "비상구 문까지 막혀버렸다.")]),
    dict(dur=4.5, bg="dark", photo="korean apartment residents in a hallway, one woman being scolded by others", move="panr",
         lines=[("주민1", "새댁이 너무 예민해~"), ("주민2", "이웃끼리 신고는 좀 그렇지.")]),
    dict(dur=4.0, bg="dark", photo="young korean mother writing a complaint on a smartphone, worried, holding a baby", move="zoomin",
         lines=[("엄마", "불나면 우리 아기는 어떡해요…")]),
    dict(dur=3.5, bg="dark", flash=True, photo="korean firefighters in uniform doing a safety inspection in an apartment hallway with clipboards", move="zoomin",
         lines=[(None, "그리고 소방 안전 점검 날.")]),
    dict(dur=5.0, bg="dark", photo="korean fire inspector pointing at a blocked fire exit, writing a ticket, serious", move="zoomin",
         lines=[("소방관", "비상구와 피난 통로를 막으면 과태료 대상입니다."), ("소방관", "오늘 안에 전부 치우세요.")]),
    dict(dur=4.5, bg="dark", photo=f"{JANG}, shocked holding a fine notice, sweating", move="shake",
         lines=[("장씨", "과태료?! 이게 다 내 물건인데!"), ("소방관", "그러니까 본인 집 안에 두셔야죠.")]),
    dict(dur=4.0, bg="dark", photo=f"{JANG}, carrying heavy boxes alone in a hallway, exhausted, sweating", move="zoomin",
         lines=[(None, "결국 혼자 하루 종일 짐을 옮겼다.")]),
    dict(dur=4.5, bg="dark", photo="clean wide apartment hallway, young mother happily pushing a stroller, neighbors smiling", move="zoomin",
         lines=[("주민1", "새댁, 그때 예민하다고 해서 미안해."), ("엄마", "복도는 모두가 지나가는 길이에요.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 8,772개",
         comments=["비상구 막는 거 진짜 위험", "소방관님 사이다", "복도 창고 우리 아파트에도 있음", "새댁 힘내요",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 이후, 복도엔 아무것도 쌓이지 않았다.")]),
    dict(dur=4.0, bg="dark", photo="hand secretly opening someone else's delivery package in front of an apartment door, hallway at night",
         move="zoomin", lines=[(None, "그런데 그날 밤, 남의 택배 상자를 몰래 뜯는 손이…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
