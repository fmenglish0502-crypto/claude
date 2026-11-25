"""알박기 빌런 참교육 1화 (AI 실사). 지어낸 이야기. 대본: scripts/series-batch-01.md 1번."""

TITLE = ("국가사업에 알박기한 집주인", "결국 0원 된 사연")
END = ("다음 편", "상가 알박기 빌런?", "팔로우하고 다음 편 보기")

OH = "greedy korean old man in his 60s, gray hair, thick eyebrows, brown cardigan, arms crossed, smug"
PARK = "korean male government official in his 30s, neat suit and tie, glasses, holding documents"

S = [
    dict(dur=3.5, bg="dark", photo=f"{OH}, standing in front of an old single house, construction site and excavators around, daytime",
         move="zoomin", lines=[(None, "새 도로가 지나갈 자리에, 딱 한 집이 버티고 있었다.")]),
    dict(dur=5.0, bg="dark", photo=f"{PARK} and {OH} sitting across a table in a meeting room, negotiation, documents on table",
         move="zoomin", lines=[("박주무관", "시세의 두 배 드리겠습니다."), ("오만석", "열 배 아니면 안 팔아.")]),
    dict(dur=4.0, bg="dark", photo="stack of negotiation documents and contracts on a desk, office, dramatic lighting",
         move="panr", lines=[(None, "협상만 일곱 번. 금액은 계속 올랐지만…"), ("오만석", "더 내놔!")]),
    dict(dur=4.5, bg="dark", photo="angry korean neighborhood residents complaining to a government official in front of a construction fence",
         move="shake", lines=[("주민1", "왜 도로 공사를 안 해요!"), ("주민2", "공무원들이 일을 안 하네!")]),
    dict(dur=5.5, bg="dark", photo=f"{OH}, signing a document with a pen at a table, smirking, close up on hands and paper",
         move="zoomin", lines=[("박주무관", "최종 매매 거부하시면, 이후 일은 책임지지 않는다는 각서에 서명해주세요."),
                               ("오만석", "써주지, 뭐.")]),
    dict(dur=3.5, bg="dark", photo="government meeting room, korean officials looking at a road blueprint map on a big table",
         move="zoomin", lines=[("국장", "설계 변경합니다. 그 집 피해서 도로 냅니다.")]),
    dict(dur=4.0, bg="dark", flash=True, photo="aerial view of a small old house completely surrounded by a new elevated highway and construction walls",
         move="zoomout", lines=[(None, "도로는 그 집을 둥글게 피해서 지어졌다.")]),
    dict(dur=4.0, bg="dark", photo=f"{OH}, shocked and angry, standing in dust and noise, blocked entrance by construction walls",
         move="shake", sfx=[("쿵쾅쿵쾅!!", 560, 520, 100, -6)], lines=[("오만석", "이게 뭐야! 집에 들어갈 길이 없잖아!")]),
    dict(dur=4.0, bg="dark", photo=f"{OH}, standing in a korean courtroom, pointing angrily, lawyers in background",
         move="zoomin", lines=[("오만석", "국가가 내 재산권을 침해했다!")]),
    dict(dur=6.0, bg="dark", photo="korean judge in black robe at the bench reading documents, courtroom, serious",
         move="zoomin", lines=[("판사", "일곱 차례 협상 기록, 그리고 본인이 서명한 각서가 있네요."), ("판사", "청구를 기각합니다.")]),
    dict(dur=4.0, bg="dark", photo=f"{OH}, sitting alone on the floor of a dusty old house, defeated, head down",
         move="zoomin", lines=[(None, "결국 0원. 남은 건 소음과 먼지뿐이었다.")]),
    dict(dur=5.0, bg="dark", photo=f"{PARK}, smiling gently, neighborhood residents happily walking on a new road behind him, sunny",
         move="zoomin", lines=[("주민1", "공무원분들 오해해서 미안해요."), ("박주무관", "욕심엔 끝이 없지만, 기회는 끝이 있죠.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 21,304개",
         comments=["각서에 사인한 게 신의 한 수", "욕심이 화를 부른다", "알박기 참교육 레전드", "공무원 오해해서 미안",
                   "다음 편 빨리"], chars=[], lines=[(None, "욕심의 끝은, 아무것도 없었다.")]),
    dict(dur=4.0, bg="dark", photo="smug korean middle-aged woman standing in front of a small shop on a redevelopment street, arms crossed, dusk",
         move="zoomin", lines=[(None, "그런데 그 옆 동네에도, 알박기를 준비하는 사람이 있었다…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
