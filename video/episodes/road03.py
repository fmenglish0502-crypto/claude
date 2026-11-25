"""보복운전/도로 빌런 3화: 깜빡이 없이 끼어드는 빌런. 지어낸 이야기."""

TITLE = ("깜빡이 없이 끼어들던 외제차", "하필 그 차 앞이었다")
END = ("다음 편", "음주운전 빌런?", "팔로우하고 다음 편 보기")

CHA = "arrogant korean woman in her 40s, big sunglasses, designer handbag, driving a white luxury car"

S = [
    dict(dur=3.5, bg="dark", photo=f"{CHA}, smirking behind the wheel, city traffic", move="zoomin",
         lines=[(None, "깜빡이는 장식이라고 생각하는 여자, 차여사.")]),
    dict(dur=4.0, bg="dark", photo="a white luxury car suddenly cutting in very close in front of a small car on a busy road, near collision",
         move="shake", sfx=[("끼익!!", 560, 600, 120, 6)], lines=[(None, "깜빡이도 없이 칼치기."), ("운전자", "어어어!")]),
    dict(dur=4.5, bg="dark", photo=f"{CHA}, laughing on the phone while driving, careless", move="zoomin",
         lines=[("차여사", "깜빡이 켜면 안 끼워줘, 그냥 들이밀어야지~")]),
    dict(dur=4.5, bg="dark", photo="annoyed korean drivers honking in traffic jam, one young driver looking shocked",
         move="panr", lines=[("운전자1", "저 차 때문에 사고 날 뻔했네!"), ("운전자2", "근데 뒤에서 클락션 울린 사람이 더 나빠 보이던데?")]),
    dict(dur=3.5, bg="dark", photo="ordinary dark gray sedan driving calmly on a highway, nothing special about it", move="zoomin",
         lines=[(None, "그리고 그날, 차여사가 끼어든 차는 평범해 보이는 회색 세단이었다.")]),
    dict(dur=3.5, bg="dark", flash=True, photo="hidden blue and red police lights flashing from the windshield of an unmarked gray sedan, highway",
         move="zoomin", sfx=[("삐용삐용!!", 560, 560, 100, -6)], lines=[(None, "회색 세단 앞유리에서 번쩍이는 경광등.")]),
    dict(dur=4.0, bg="dark", photo="korean highway patrol police officer in uniform at a car window, holding a ticket book, serious",
         move="zoomin", lines=[("경찰", "고속도로 순찰대 암행 차량입니다. 방향지시등 미사용, 끼어들기 위반입니다.")]),
    dict(dur=4.5, bg="dark", photo=f"{CHA}, taking off sunglasses, shocked and embarrassed, sitting in her car", move="shake",
         lines=[("차여사", "아니, 다들 이렇게 해요!"), ("경찰", "블랙박스 확인해보니 오늘만 일곱 번이네요.")]),
    dict(dur=4.0, bg="dark", photo="close up of a traffic violation ticket paper and a stack of fines, dramatic lighting", move="zoomin",
         lines=[(None, "과태료와 벌점이 한꺼번에 쏟아졌다.")]),
    dict(dur=4.5, bg="dark", photo="young korean driver smiling with relief, holding steering wheel, sunny road", move="zoomin",
         lines=[("운전자", "깜빡이 하나면 서로 안전한데."), (None, "방향지시등은 양보를 부탁하는 인사다.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 12,551개",
         comments=["암행순찰차 레전드", "깜빡이 안 켜는 차 진짜 많음", "오늘만 일곱 번ㅋㅋㅋ", "깜빡이는 인사다 명언",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 이후, 차여사는 깜빡이부터 켠다.")]),
    dict(dur=4.0, bg="dark", photo="korean man in his 30s stumbling out of a bar at night holding car keys, drunk, neon lights",
         move="zoomin", lines=[(None, "그런데 그날 밤, 술집 앞에서 차 키를 꺼내는 남자가…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
