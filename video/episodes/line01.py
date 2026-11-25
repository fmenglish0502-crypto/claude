"""생활 민폐 빌런 1화: 새치기 빌런. 지어낸 이야기. 대본: scripts/series-batch-01.md 2번."""

TITLE = ("새치기 밥 먹듯 하던 남자", "은행 창구에서 생긴 일")
END = ("다음 편", "엘리베이터 독점 빌런?", "팔로우하고 다음 편 보기")

GU = "smug korean man in his 30s, slicked side-part hair, beige trench coat, cutting in line"
TELLER = "young korean female bank teller in navy uniform, neat bun hair, calm professional"

S = [
    dict(dur=3.5, bg="dark", photo=f"{GU}, cutting in front of people in a long line at a convenience store, people annoyed", move="zoomin",
         lines=[(None, "줄 서는 건 손해라고 믿는 남자, 구태만.")]),
    dict(dur=4.0, bg="dark", photo=f"{GU}, sneaking to the front of a long queue outside a popular korean restaurant, fake smile", move="panr",
         lines=[("구태만", "아, 제 일행이 앞에 있어서요~")]),
    dict(dur=4.5, bg="dark", photo=f"young korean woman in a white sweater pointing politely at the end of the line, {GU} ignoring her", move="zoomin",
         lines=[("손님", "저기요, 줄 서세요."), ("구태만", "바쁜 사람이 먼저지!")]),
    dict(dur=4.5, bg="dark", photo="korean people in a queue glaring at a young woman, whispering, outside a restaurant", move="shake",
         lines=[("손님2", "그냥 넘어가요, 시끄럽게…"), (None, "오히려 그녀가 눈치를 받았다.")]),
    dict(dur=3.5, bg="dark", photo=f"{GU}, entering a korean bank lobby holding loan documents, number ticket machine nearby", move="zoomin",
         lines=[(None, "다음 날, 인생이 걸린 대출 심사 날.")]),
    dict(dur=4.0, bg="dark", photo=f"{GU}, ignoring the number ticket machine and walking straight to the bank counter, rude", move="shake",
         lines=[("구태만", "저 급해요, 먼저 해주세요!")]),
    dict(dur=4.0, bg="dark", flash=True, photo=f"{TELLER}, at the bank counter, raising her eyes with a knowing look", move="zoomin",
         lines=[("직원", "…어제 맛집 줄에서 뵀죠? 저, 맨 앞에 있던 사람이에요.")]),
    dict(dur=4.0, bg="dark", photo=f"{TELLER}, pointing politely at a number ticket machine, bank interior", move="zoomin",
         lines=[("직원", "번호표 뽑고 기다리세요. 순서는 모두에게 같습니다.")]),
    dict(dur=4.0, bg="dark", photo=f"{GU}, sitting impatiently in a bank waiting area, clock on wall showing closing time", move="zoomin",
         lines=[(None, "차례가 왔을 땐, 오늘 심사가 이미 마감된 뒤였다.")]),
    dict(dur=4.0, bg="dark", photo=f"{GU}, shocked reading a notice about interest rate increase at the bank, pale", move="shake",
         lines=[("구태만", "하루 만에 금리가 올랐다고요?!")]),
    dict(dur=4.0, bg="dark", photo=f"young korean woman in a white sweater standing in a neat line, smiling, people nodding at her", move="zoomin",
         lines=[("손님", "줄은 서로의 시간을 지키는 약속이에요.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 9,105개",
         comments=["번호표 사이다ㅋㅋ", "일행이 앞에 있어요 레전드", "새치기 진짜 싫다", "직원분 최고", "다음 편 빨리"],
         chars=[], lines=[(None, "그날 이후, 구태만은 번호표부터 뽑는다.")]),
    dict(dur=4.0, bg="dark", photo="korean apartment elevator with its door held open by a woman with many shopping bags, people waiting in the lobby annoyed",
         move="zoomin", lines=[(None, "그런데 그날 밤, 엘리베이터 문을 붙잡고 놓지 않는 이웃이…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
