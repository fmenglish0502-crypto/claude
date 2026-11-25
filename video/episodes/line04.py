"""생활 민폐 빌런 4화: 남의 택배 뜯는 이웃. 지어낸 이야기."""

TITLE = ("남의 택배를 몰래 뜯던 이웃", "CCTV에 찍힌 얼굴")
END = ("다음 편", "구태만이 이사 왔다?", "팔로우하고 다음 편 보기")

HONG = "nosy korean woman in her 40s, ponytail, pink cardigan, sneaky expression, holding a delivery box"
JI = "young korean man in his 20s, hoodie, worried, standing in front of an apartment door"

S = [
    dict(dur=3.5, bg="dark", photo=f"{HONG}, peeking into a delivery box in front of someone else's apartment door", move="zoomin",
         lines=[(None, "남의 택배가 궁금해 견딜 수 없는 이웃, 홍여사.")]),
    dict(dur=4.5, bg="dark", photo=f"{JI}, looking at an opened and resealed delivery box with tape, confused", move="zoomin",
         lines=[("지훈", "택배가 또 뜯겨 있네…"), (None, "안에 든 물건이 하나씩 없어졌다.")]),
    dict(dur=4.5, bg="dark", photo=f"{HONG}, gossiping with neighbors in an apartment lobby, pointing upstairs", move="panr",
         lines=[("홍여사", "그 총각, 택배 기사님을 의심한대~"), ("주민", "어머, 기사님한테 그러면 안 되지!")]),
    dict(dur=4.5, bg="dark", photo="korean delivery driver looking hurt and embarrassed, holding boxes, apartment entrance", move="zoomin",
         lines=[("택배기사", "저는 문 앞에 잘 두고 갔어요…"), (None, "애꿎은 택배 기사님까지 의심받았다.")]),
    dict(dur=4.0, bg="dark", photo=f"{JI}, installing a small security camera next to his apartment door, determined", move="zoomin",
         lines=[("지훈", "누군지 확인해야겠어.")]),
    dict(dur=3.5, bg="dark", flash=True, photo=f"security camera view at night, {HONG} opening a box in front of a door, grainy CCTV look",
         move="zoomin", lines=[(None, "그날 밤, 카메라에 찍힌 얼굴은…")]),
    dict(dur=4.5, bg="dark", photo="korean police officer showing a phone screen to a woman at her apartment door, hallway", move="zoomin",
         lines=[("경찰", "남의 택배를 열고 가져가는 건 범죄입니다."), ("홍여사", "그, 그냥 뭐가 왔나 궁금해서…")]),
    dict(dur=4.5, bg="dark", photo=f"{HONG}, embarrassed, neighbors staring at her in the apartment lobby", move="shake",
         lines=[("주민", "택배 기사님 탓하더니…"), ("지훈", "가져간 물건 전부 돌려주세요.")]),
    dict(dur=4.5, bg="dark", photo=f"{HONG}, bowing and apologizing to a delivery driver, apartment entrance", move="zoomin",
         lines=[("홍여사", "기사님, 죄송했어요."), ("택배기사", "앞으로는 남의 상자는 안 여시는 걸로요.")]),
    dict(dur=4.0, bg="dark", photo=f"{JI} and a korean delivery driver fist-bumping and smiling, apartment entrance", move="zoomin",
         lines=[("지훈", "남의 문 앞은 남의 집이에요.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 13,880개",
         comments=["택배 뜯는 이웃 소름", "기사님 의심받은 거 너무해", "CCTV는 진리", "총각 잘했다", "다음 편 빨리"],
         chars=[], lines=[(None, "그날 이후, 문 앞 택배는 무사했다.")]),
    dict(dur=4.0, bg="dark", photo="smug korean man in his 30s, slicked side-part hair, beige trench coat, carrying moving boxes into an apartment building",
         move="zoomin", lines=[(None, "그런데 다음 날, 이 아파트로 이사 온 남자는… 새치기의 그 남자였다.")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
