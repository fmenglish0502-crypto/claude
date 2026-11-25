"""알박기 빌런 3화: 골목길 통행료 받는 땅 주인. 지어낸 이야기."""

TITLE = ("골목길 막고 통행료 받던 땅 주인", "결국 길이 바뀌었다")
END = ("다음 편", "알박기 뒤에 숨은 브로커?", "팔로우하고 다음 편 보기")

GU = "greedy korean old man in his 70s, flat cap, gray vest, standing next to a chain blocking a narrow alley"

S = [
    dict(dur=3.5, bg="dark", photo=f"{GU}, smug, residential alley in korea", move="zoomin",
         lines=[(None, "동네 주민 모두가 쓰던 골목길. 그 땅을 산 남자, 구두쇠 영감.")]),
    dict(dur=4.5, bg="dark", photo=f"{GU}, holding out his hand for money, residents trying to pass the alley", move="zoomin",
         lines=[("영감", "내 땅이니까 지나가려면 한 번에 천 원."), ("주민", "여기 30년 다닌 길인데요?")]),
    dict(dur=4.5, bg="dark", photo="elderly korean woman with a shopping cart taking a very long detour around a block, tired", move="panr",
         lines=[(None, "학교 가는 아이들도, 장 보는 할머니도 먼 길을 돌아가야 했다.")]),
    dict(dur=4.5, bg="dark", photo="korean neighbors arguing, some blaming a young woman with documents", move="shake",
         lines=[("주민1", "천 원 내면 되지, 왜 시끄럽게 해?"), ("주민2", "젊은 사람이 유난이야.")]),
    dict(dur=4.0, bg="dark", photo="young korean woman reading land documents and maps at a desk, determined", move="zoomin",
         lines=[("수정", "이 길 없으면 우리 집은 밖으로 나갈 길이 없어요.")]),
    dict(dur=4.0, bg="dark", photo="korean lawyer explaining documents to residents in a community center", move="zoomin",
         lines=[("변호사", "다른 길이 없는 땅에는 법이 통행할 권리를 인정합니다.")]),
    dict(dur=3.5, bg="dark", flash=True, photo="korean courtroom, judge announcing ruling, residents in audience", move="zoomin",
         lines=[("판사", "주민들의 통행권을 인정한다. 통행료 요구는 부당하다.")]),
    dict(dur=4.5, bg="dark", photo=f"{GU}, shocked, chain being removed from the alley by city workers", move="shake",
         lines=[("영감", "내 땅인데 왜 맘대로 못 해!"), ("구청직원", "그리고 구청에서 옆으로 새 길을 냅니다.")]),
    dict(dur=4.0, bg="dark", photo="new wide paved walkway next to an old narrow alley, children walking happily, sunny", move="zoomout",
         lines=[(None, "새 길이 생기자, 아무도 그 골목으로 다니지 않았다.")]),
    dict(dur=4.0, bg="dark", photo=f"{GU}, sitting alone by an empty alley, nobody passing, lonely", move="zoomin",
         lines=[(None, "결국 그 땅은 아무도 사지 않는 땅이 됐다.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 10,876개",
         comments=["통행권 이런 게 있구나", "천 원 받다 땅값 0원ㅋㅋ", "수정 씨 최고", "새 길 낸 구청 칭찬해",
                   "다음 편 빨리"], chars=[], lines=[("수정", "길은 같이 쓰라고 있는 거예요.")]),
    dict(dur=4.0, bg="dark", photo="shadowy korean man in an expensive suit making phone calls in a dark office, maps on the wall",
         move="zoomin", lines=[(None, "그런데 이 모든 알박기 뒤에서, 전화를 거는 남자가 있었다…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
