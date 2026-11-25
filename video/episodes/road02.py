"""보복운전/도로 빌런 2화: 버스 쩍벌 빌런. 지어낸 이야기. (1화 떡밥: 버스 탄 상철 옆자리)"""

TITLE = ("버스에서 두 자리 차지한 쩍벌남", "면접장에서 생긴 일")
END = ("다음 편", "깜빡이 없이 끼어드는 빌런?", "팔로우하고 다음 편 보기")

DO = "rude korean man in his 30s, slicked back hair, navy suit, sitting on a city bus with legs spread very wide"
SANG = "korean man in his 40s, short messy black hair, black leather jacket"
PREG = "pregnant korean woman in her 30s, office blazer, holding a handbag, tired"

S = [
    dict(dur=4.0, bg="dark", photo=f"{DO}, taking two seats, bag on the next seat, crowded bus interior", move="zoomin",
         lines=[(None, "면허를 잃고 버스를 탄 상철. 옆자리엔 두 자리를 차지한 남자가 있었다.")]),
    dict(dur=4.0, bg="dark", photo=f"{SANG}, squeezed into a small space on a bus seat, annoyed face", move="shake",
         lines=[("강상철", "저기요, 다리 좀 오므리시죠."), ("도만수", "내 다리 내 마음이지.")]),
    dict(dur=4.5, bg="dark", photo="bus passengers glaring at a man in a black leather jacket, whispering, crowded bus",
         move="panr", lines=[("승객1", "저 사람, 보복운전 영상 그 사람 아니야?"), ("승객2", "또 시비 거네…")]),
    dict(dur=4.5, bg="dark", photo=f"{PREG}, standing and holding a bus handle, looking at a man spreading legs on seat",
         move="zoomin", lines=[(None, "그때 탄 임산부."), ("도만수", "(못 본 척 휴대폰만 본다)")]),
    dict(dur=4.0, bg="dark", photo=f"{SANG}, standing up and offering his seat to a pregnant woman on a bus, awkward gentle smile",
         move="zoomin", lines=[("강상철", "여기 앉으세요."), (None, "상철이 처음으로 양보를 했다.")]),
    dict(dur=3.5, bg="dark", photo=f"{DO}, walking into a modern office building lobby, confident smirk, holding a resume", move="zoomin",
         lines=[(None, "그날 오후, 도만수는 꿈에 그리던 회사 최종 면접에 갔다.")]),
    dict(dur=3.5, bg="dark", flash=True, photo=f"{PREG}, sitting at the center of an interview panel table, calm serious face",
         move="zoomin", lines=[(None, "면접관 자리에 앉아 있던 사람은…")]),
    dict(dur=5.0, bg="dark", photo=f"{DO}, shocked pale face, sitting alone in an interview chair, sweating", move="shake",
         lines=[("면접관", "오늘 아침 버스에서 뵀죠? 다리 넓게 앉으시던 분."), ("도만수", "아, 그게…")]),
    dict(dur=5.0, bg="dark", photo=f"{PREG}, closing a resume folder, gentle but firm expression, office", move="zoomin",
         lines=[("면접관", "우리 회사는 같이 일하는 사람을 배려하는 사람을 뽑아요."), ("면접관", "오늘은 여기까지 하죠.")]),
    dict(dur=4.0, bg="dark", photo=f"{SANG}, sitting on a bus, small proud smile, other passengers nodding at him", move="zoomin",
         lines=[("승객1", "아까 그 아저씨, 자리 양보하던데?"), ("강상철", "…자리는 나눠 쓰는 거니까.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 9,844개",
         comments=["쩍벌남 참교육 레전드", "상철이 철들었네ㅋㅋ", "면접관 등장 소름", "버스 두 자리 진짜 민폐",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 이후, 도만수는 버스에서 다리를 모으고 앉는다.")]),
    dict(dur=4.0, bg="dark", photo="a white luxury car cutting in front of other cars without turn signal on a highway, aggressive",
         move="panr", lines=[(None, "그런데 도로 위엔, 깜빡이 한 번 안 켜고 끼어드는 차가…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
