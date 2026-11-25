"""알박기 빌런 2화: 재개발 상가 알박기. 지어낸 이야기. (1화 떡밥: 옆 동네 알박기 준비하는 여자)"""

TITLE = ("재개발 상가에 알박기한 사장님", "법원 판결 한 줄에 끝났다")
END = ("다음 편", "골목길 통행료 받는 땅 주인?", "팔로우하고 다음 편 보기")

MA = "smug korean woman in her 50s, permed hair, gold earrings, red cardigan, standing in front of a small shop"

S = [
    dict(dur=3.5, bg="dark", photo=f"{MA}, arms crossed, old shopping street under redevelopment, other shops closed", move="zoomin",
         lines=[(None, "재개발 상가 거리. 마지막까지 버티는 가게 하나.")]),
    dict(dur=5.0, bg="dark", photo=f"{MA} and a korean redevelopment association staff in a suit at a table, papers", move="zoomin",
         lines=[("조합직원", "다른 상인분들은 다 합의하셨어요."), ("마금자", "권리금 20억. 그 전엔 못 나가.")]),
    dict(dur=4.5, bg="dark", photo="small shop owners in korea sitting worried in temporary stores, waiting, sad", move="panr",
         lines=[(None, "공사가 멈추자, 먼저 합의한 상인들은 갈 곳 없이 기다려야 했다.")]),
    dict(dur=4.5, bg="dark", photo="korean residents on a street complaining loudly at redevelopment association office", move="shake",
         lines=[("주민1", "조합은 일을 왜 이렇게 못 해!"), ("주민2", "사장님 한 명 못 설득해?")]),
    dict(dur=4.0, bg="dark", photo=f"{MA}, sipping coffee at her shop, smiling smugly, watching construction stopped", move="zoomin",
         lines=[("마금자", "버틸수록 돈이 되는 거야.")]),
    dict(dur=4.0, bg="dark", photo="korean lawyer in a suit filing documents at a courthouse, determined", move="zoomin",
         lines=[("변호사", "법에 정해진 절차대로, 매도청구 소송을 냅니다.")]),
    dict(dur=3.5, bg="dark", flash=True, photo="korean courtroom, judge reading a ruling, wooden gavel", move="zoomin",
         lines=[("판사", "감정평가된 시세대로 매도하라.")]),
    dict(dur=4.5, bg="dark", photo=f"{MA}, shocked, holding a court ruling paper, standing in courthouse hallway", move="shake",
         lines=[("마금자", "20억이… 시세대로라고?"), ("변호사", "그동안 거절하신 제안이 시세의 세 배였죠.")]),
    dict(dur=4.0, bg="dark", photo="construction resuming, excavators working at a redevelopment site, sunny day", move="zoomout",
         lines=[(None, "공사는 다시 시작됐다. 버틴 만큼, 손해만 남았다.")]),
    dict(dur=4.5, bg="dark", photo="happy small shop owners in korea opening new stores in a modern building, smiling", move="zoomin",
         lines=[("상인", "다 같이 버텼으면 다 같이 잘 됐을 텐데."), (None, "욕심은 이웃의 시간까지 빼앗는다.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 14,302개",
         comments=["세 배 제안 거절ㅋㅋ", "매도청구 처음 알았다", "합의한 상인들만 불쌍", "알박기 시리즈 사이다",
                   "다음 편 빨리"], chars=[], lines=[(None, "마금자는 처음 제안의 3분의 1만 받았다.")]),
    dict(dur=4.0, bg="dark", photo="narrow alley in a korean residential area blocked by a chain and a sign, an old man guarding it",
         move="zoomin", lines=[(None, "그런데 다른 동네 골목길엔, 통행료를 받는 땅 주인이…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
