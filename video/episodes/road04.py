"""보복운전/도로 빌런 4화: 음주운전 빌런. 지어낸 이야기."""

TITLE = ("\"한 잔은 괜찮아\" 음주운전남", "시민들에게 딱 걸렸다")
END = ("다음 편", "면허 다시 따려는 강상철?", "팔로우하고 다음 편 보기")

JU = "korean man in his 30s, flushed red face, loosened tie, white shirt, holding car keys at night"

S = [
    dict(dur=3.5, bg="dark", photo=f"{JU}, laughing with friends at a korean pub, soju bottles on table", move="zoomin",
         lines=[(None, "술자리마다 차를 끌고 오는 남자, 주한량.")]),
    dict(dur=4.5, bg="dark", photo=f"{JU}, walking to his car outside a pub at night, swaying", move="zoomin",
         lines=[("친구", "야, 대리 불러."), ("주한량", "한 잔밖에 안 마셨어. 집 코앞인데 뭐.")]),
    dict(dur=4.5, bg="dark", photo="korean friends at a pub laughing and waving goodbye, careless, night", move="panr",
         lines=[("친구2", "쟤 원래 술 세. 괜찮아~"), (None, "아무도 말리지 않았다.")]),
    dict(dur=4.0, bg="dark", photo="a car swerving between lanes on a dark city road at night, headlights blur", move="shake",
         lines=[(None, "도로 위에서 비틀거리는 차.")]),
    dict(dur=4.5, bg="dark", photo="korean delivery rider on a motorbike at night talking on phone, worried, following a car",
         move="zoomin", lines=[("배달기사", "여기 음주운전 의심 차량이요. 지금 따라가고 있어요.")]),
    dict(dur=4.0, bg="dark", photo="two korean taxi drivers blocking a car safely at a red light at night, taxis around a sedan",
         move="zoomin", lines=[(None, "택시 기사들이 차를 앞뒤로 막아섰다."), ("택시기사", "시동 끄세요!")]),
    dict(dur=3.5, bg="dark", flash=True, photo="korean police car with flashing lights arriving at night street, officers stepping out",
         move="zoomin", sfx=[("삐용삐용!!", 560, 560, 100, 6)], lines=[(None, "곧이어 도착한 경찰.")]),
    dict(dur=5.0, bg="dark", photo=f"{JU}, blowing into a police breathalyzer, police officer holding device, night", move="zoomin",
         lines=[("경찰", "측정 결과 면허 취소 수치입니다."), ("주한량", "한 잔밖에 안 마셨다니까요!")]),
    dict(dur=4.5, bg="dark", photo=f"{JU}, sitting in the back of a police car, head down, defeated, night", move="zoomin",
         lines=[("경찰", "음주운전은 형사처벌에 면허 취소, 보험 처리도 어렵습니다.")]),
    dict(dur=4.5, bg="dark", photo="delivery rider and taxi drivers standing together at night street, relieved smiles", move="zoomin",
         lines=[("배달기사", "다친 사람 없어서 다행이에요."), (None, "한 잔도 운전대는 잡지 않는 것. 그게 상식이다.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 18,920개",
         comments=["시민 영웅들 최고", "한 잔도 안 됨 진짜", "말리지 않은 친구들도 문제", "배달기사님 존경",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 밤, 큰 사고 하나가 막혔다.")]),
    dict(dur=4.0, bg="dark", photo="korean man in his 40s, short messy black hair, black leather jacket, sitting nervously at a driving license test center",
         move="zoomin", lines=[(None, "그리고 같은 시각, 운전면허 시험장에 앉아 있는 낯익은 남자…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
