"""알박기 빌런 4화: 알박기 뒤에 숨은 브로커. 지어낸 이야기. (1화 오만석 재등장)"""

TITLE = ("알박기만 골라 부추긴 브로커", "그 끝은 수갑이었다")
END = ("다음 편", "브로커의 진짜 보스?", "팔로우하고 다음 편 보기")

BRO = "slick korean man in his 40s, expensive gray suit, slicked hair, gold watch, smiling falsely"
OH = "greedy korean old man in his 60s, gray hair, thick eyebrows, brown cardigan"

S = [
    dict(dur=3.5, bg="dark", photo=f"{BRO}, sitting in a dark office with maps of redevelopment areas on the wall", move="zoomin",
         lines=[(None, "개발 예정지만 골라 다니는 남자, 부동산 브로커 백기만.")]),
    dict(dur=5.0, bg="dark", photo=f"{BRO} whispering to {OH} at a cafe table, papers between them", move="zoomin",
         lines=[("백기만", "열 배 부르세요. 버티면 무조건 줍니다."), ("백기만", "대신 수수료는 30%.")]),
    dict(dur=4.0, bg="dark", photo=f"{OH}, sitting alone in a dusty old house surrounded by construction walls, regretful", move="zoomin",
         lines=[(None, "그 말을 믿은 오만석은 결국 0원이 됐다.")]),
    dict(dur=4.5, bg="dark", photo=f"{BRO}, smiling at a seminar stage, crowd of people listening, banner about real estate investing",
         move="panr", lines=[("백기만", "버티는 자가 이깁니다!"), ("청중", "와아~ 역시 전문가!")]),
    dict(dur=4.5, bg="dark", photo=f"{OH}, visiting a police station, handing over a stack of documents and phone recordings", move="zoomin",
         lines=[("오만석", "이 사람이 시킨 거예요. 녹음도, 계약서도 다 있습니다.")]),
    dict(dur=4.0, bg="dark", photo="korean police investigators looking at a board connecting many photos and maps, investigation room",
         move="zoomin", lines=[("수사관", "알박기마다 같은 브로커가 있었네요. 전국에 스무 곳.")]),
    dict(dur=3.5, bg="dark", flash=True, photo="korean police officers entering a fancy office, man in gray suit standing up shocked",
         move="zoomin", lines=[("수사관", "백기만 씨, 사기와 부동산 관련 법 위반 혐의로 체포합니다.")]),
    dict(dur=4.5, bg="dark", photo=f"{BRO}, in handcuffs, being led out of a building by police, reporters taking photos",
         move="shake", lines=[("백기만", "나는 조언만 했을 뿐이야!"), ("기자", "피해자가 스무 명이 넘는데요!")]),
    dict(dur=4.5, bg="dark", photo=f"{OH}, standing in front of his old house, calm, a kind government official next to him", move="zoomin",
         lines=[("오만석", "욕심에 귀가 먼저 멀었지요."), ("박주무관", "늦었지만, 용기 내주셔서 감사합니다.")]),
    dict(dur=4.0, bg="dark", photo="news broadcast screen in korea about a real estate broker arrest, anchor desk", move="zoomin",
         lines=[(None, "전국의 알박기 피해자들이 하나둘 목소리를 냈다.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 22,410개",
         comments=["1화 할아버지 다시 나와서 소름", "브로커가 진짜 빌런이었네", "수수료 30%ㅋㅋ", "알박기 시리즈 완전 재밌다",
                   "다음 편 빨리"], chars=[], lines=[(None, "욕심을 파는 사람이, 가장 먼저 무너졌다.")]),
    dict(dur=4.0, bg="dark", photo="silhouette of a powerful man in a luxury penthouse looking at city lights, phone in hand, night",
         move="zoomin", lines=[(None, "그런데 구치소로 걸려온 전화 한 통. \"입 다물고 있어.\"")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
