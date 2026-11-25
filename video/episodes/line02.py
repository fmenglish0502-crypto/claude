"""생활 민폐 빌런 2화: 엘리베이터 독점 빌런. 지어낸 이야기."""

TITLE = ("엘리베이터 붙잡고 수다 떨던 이웃", "자기가 급해지자 생긴 일")
END = ("다음 편", "복도에 짐 쌓는 이웃?", "팔로우하고 다음 편 보기")

UM = "talkative korean woman in her 50s, curly short perm hair, purple padded jacket, many shopping bags"
STU = "tired korean high school girl in school uniform with a backpack, holding a watch"

S = [
    dict(dur=3.5, bg="dark", photo=f"{UM}, holding the elevator door open while chatting on the phone, apartment lobby", move="zoomin",
         lines=[(None, "매일 아침 엘리베이터를 붙잡고 수다를 떠는 이웃, 엄여사.")]),
    dict(dur=4.5, bg="dark", photo=f"{UM}, blocking the elevator door with her foot, loading shopping bags slowly, laughing", move="zoomin",
         lines=[("엄여사", "잠깐만~ 짐 좀 싣고. 어머 그래서 걔가~"), (None, "10분째 멈춘 엘리베이터.")]),
    dict(dur=4.5, bg="dark", photo=f"{STU}, waiting on the 15th floor looking at the elevator floor display stuck, anxious", move="shake",
         lines=[("수험생", "모의고사 늦겠다…"), (None, "결국 15층 계단을 뛰어 내려갔다.")]),
    dict(dur=4.5, bg="dark", photo="korean apartment residents chatting in a lobby, one older man shrugging, others nodding", move="panr",
         lines=[("주민1", "그 집 아줌마 원래 그래~ 이웃끼리 좀 봐줘."), ("주민2", "학생이 좀 일찍 나오면 되지.")]),
    dict(dur=4.0, bg="dark", photo="notice paper on an apartment elevator wall about not holding doors, management office stamp", move="zoomin",
         lines=[(None, "관리사무소 공지도 소용없었다.")]),
    dict(dur=4.0, bg="dark", flash=True, photo=f"{UM}, panicking holding a phone in her apartment hallway, frightened face", move="shake",
         lines=[(None, "그런데 어느 날 밤, 엄여사에게 걸려온 전화."), ("엄여사", "남편이 쓰러졌다고요?!")]),
    dict(dur=4.0, bg="dark", photo=f"{UM}, pressing the elevator button repeatedly, the floor display stuck on another floor", move="shake",
         lines=[("엄여사", "왜 안 와! 빨리 좀!")]),
    dict(dur=4.5, bg="dark", photo="another resident holding the elevator door open on another floor, moving boxes, chatting", move="zoomin",
         lines=[(None, "다른 층에서, 누군가 엘리베이터를 붙잡고 있었다."), ("이웃", "잠깐만요~ 짐 좀 싣고~")]),
    dict(dur=4.5, bg="dark", photo=f"{STU}, running up to help a panicked older woman, guiding her to the stairs, night", move="zoomin",
         lines=[("수험생", "아주머니, 계단으로 같이 가요! 제가 119 불렀어요.")]),
    dict(dur=4.5, bg="dark", photo=f"{UM}, crying and thanking a high school girl in front of an ambulance, night", move="zoomin",
         lines=[("엄여사", "학생… 그동안 내가 미안했어."), ("수험생", "엘리베이터는 모두의 시간이니까요.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 11,034개",
         comments=["똑같이 당하니까 알지", "학생 너무 착하다ㅠ", "엘베 잡고 수다 진짜 민폐", "아저씨 괜찮으시길",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날 이후, 엄여사는 짐을 미리 내려놓고 엘리베이터를 부른다.")]),
    dict(dur=4.0, bg="dark", photo="narrow apartment hallway blocked by piles of boxes, bicycles and a refrigerator, fire exit sign hidden",
         move="zoomin", lines=[(None, "그런데 같은 층 복도엔, 점점 짐을 쌓아 올리는 이웃이…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
