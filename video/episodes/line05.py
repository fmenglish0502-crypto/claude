"""생활 민폐 빌런 5화: 구태만이 이사 왔다 (독서실 자리 맡기). 지어낸 이야기.

참조 스타일(STYLE="ref") 2차 시험판:
- 첫 장면은 두 사람이 맞붙는 대화(위아래 나눈 화면)로 시작 → "세 시간 전" 회상 → 사이다 → 떡밥.
- 얼굴 컷은 사용자가 드리미나로 만든 배우 사진(output/cast/), 배경 컷만 직접 그린 그림(=번호).
- 대사 한 장면에 한 줄 → 말하는 사람 얼굴이 그때그때 나온다.
"""

STYLE = "ref"
TITLE = ("", "")
END = ("다음 편", "입주자 대표 구태만?", "팔로우하고 다음 편 보기")

# 배우 사진 (output/cast/)
CAST = {
    "gu": "m40_slick_smirk.jpg",      # 구태만 (빌런)
    "ji": "m20_navy.jpg",             # 지훈
    "stu": "f20_longhair.jpg",        # 수험생
    "mgr": "m50_turtleneck.jpg",      # 관리소장
    "aj1": "f60_purple_scream.jpg",   # 주민 (소리치는 아주머니)
    "aj2": "f60_leopard.jpg",         # 주민2
}

S = [
    # --- 첫 장면: 한창 싸우는 중 (훅) ---
    dict(dur=3.0, photos=["@gu|@ji", "@gu!"], lines=[("구태만", "네까짓 게 뭔데 내 가방에 손을 대?!")]),
    dict(dur=2.5, photos=["@ji"], lines=[("지훈", "여긴 다 같이 쓰는 독서실이에요.")]),
    dict(dur=2.5, photos=["@gu!"], lines=[("구태만", "내가 먼저 맡았으면 내 자리야!")]),
    dict(dur=2.5, photos=["@aj1!"], lines=[("주민", "새로 온 총각이 남의 가방을 뒤졌대!")]),
    dict(dur=2.5, photos=["@aj2", "@ji"], lines=[("아주머니", "어머, 젊은 사람이 왜 그래?")]),
    # --- 회상: 세 시간 전 ---
    dict(dur=3.5, sepia=True, photos=["=01_1", "=02_0"], lines=[(None, "사건은 세 시간 전, 독서실 문이 열리자마자 시작됐다.")]),
    dict(dur=3.0, sepia=True, photos=["@gu", "=01_1"], lines=[("구태만", "공짜 독서실? 자리부터 맡아야지.")]),
    dict(dur=3.0, sepia=True, photos=["=02_0", "=03_1"], lines=[(None, "가방 다섯 개로 자리 다섯 개를 맡고 사라졌다.")]),
    dict(dur=3.0, sepia=True, photos=["@stu", "=03_1"], lines=[("수험생", "자리가 하나도 없네… 시험이 내일인데.")]),
    dict(dur=3.0, sepia=True, photos=["@ji", "=04_1"], lines=[("지훈", "30분 넘게 비운 자리는 정리해도 된대요.")]),
    # --- 다시 지금: 사이다 ---
    dict(dur=3.0, flash=True, photos=["@mgr", "=07_1"], lines=[("관리소장", "잠깐만요. 출입 기록 확인했습니다.")]),
    dict(dur=3.0, photos=["@mgr", "@gu"], lines=[("관리소장", "구태만 씨, 아침 7시에 들어와 1분 만에 나가셨네요.")]),
    dict(dur=3.0, photos=["=07_1", "@gu!"], lines=[("관리소장", "자리만 맡고 여섯 시간 비우셨어요.")]),
    dict(dur=2.5, photos=["@mgr"], lines=[("관리소장", "규정상 한 달 이용 정지입니다.")]),
    dict(dur=2.5, photos=["@gu!"], lines=[("구태만", "아니, 바쁜 사람이 먼저지!")]),
    dict(dur=2.5, photos=["@aj1"], lines=[("주민", "바쁘면 줄을 서세요! 총각, 오해해서 미안해요.")]),
    dict(dur=3.0, photos=["@ji", "@stu"], lines=[("지훈", "자리는 맡는 게 아니라, 쓰는 거예요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=["=11_0"], lines=[(None, "그런데 며칠 뒤, 엘리베이터에 붙은 공고.")]),
    dict(dur=3.0, flash=True, photos=["@gu"], lines=[(None, "입주자 대표 후보… 구태만?!")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
