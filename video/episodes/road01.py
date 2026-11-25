"""보복운전 빌런 참교육 1화 (AI 실사 그림체). 지어낸 이야기. 대본: scripts/road01.md
만들기: gen_photos.py로 장면 그림 → tts_karma.py로 목소리 → PHOTO_DIR, VOICE_DIR 주고 make_karma.py
"""

TITLE = ("매일 클락션 울리던 보복운전러", "결국 임자 만났다")
END = ("다음 편", "버스 쩍벌 빌런?", "팔로우하고 다음 편 보기")

SANG = "angry korean man in his 40s, short messy black hair, black leather jacket, gold necklace"
SUA = "young korean woman in her 20s, long brown hair, white blouse"
GANG = "three huge intimidating korean men in black suits and sunglasses, tattoos on arms"

S = [
    dict(dur=3.5, bg="dark", photo=f"{SANG}, driving a red sports car fast on a busy seoul road, smirking, motion blur",
         move="zoomin", lines=[(None, "출근길마다 클락션을 울려대는 남자, 강상철.")]),
    dict(dur=4.0, bg="dark", photo=f"{SANG}, inside a car, shouting with mouth open, honking the horn, view through windshield",
         move="shake", sfx=[("빵빵빵!!", 600, 520, 110, -8)],
         lines=[("강상철", "초보면 버스나 타!")]),
    dict(dur=4.0, bg="dark", photo="rear view of a small white car with a beginner driver sticker, red car cutting in front very close, city road",
         move="zoomin", sfx=[("끼익!!", 560, 600, 120, 6)],
         lines=[(None, "일부러 앞에 끼어들어 급정거까지."), ("수아", "꺄악!")]),
    dict(dur=5.0, bg="dark", photo="traffic jam on seoul road, annoyed drivers leaning out of car windows, honking, daytime",
         move="panr", lines=[("운전자1", "거기서 왜 서요!"), ("운전자2", "초보가 길 막네!")]),
    dict(dur=4.0, bg="dark", photo=f"{SUA}, sitting in driver seat, teary eyes, looking at dashcam screen, sad",
         move="zoomin", lines=[("수아", "내가 잘못한 게 아닌데…")]),
    dict(dur=3.5, bg="dark", photo=f"{SANG}, inside a car behind a black luxury sedan, yelling and honking, arrogant",
         move="shake", sfx=[("빵빵!!", 640, 520, 110, 8)], lines=[("강상철", "비켜! 비키라고!")]),
    dict(dur=3.0, bg="dark", flash=True, photo="a black luxury sedan stopped suddenly on the road, red sports car stopped right in front of it, tense",
         move="zoomin", lines=[(None, "그리고 또 급정거.")]),
    dict(dur=4.5, bg="dark", photo=f"{GANG}, slowly getting out of a black sedan on a road, menacing, low angle shot",
         move="zoomout", lines=[("형님", "방금 우리 차 앞에서 브레이크 밟은 거, 일부러야?")]),
    dict(dur=4.0, bg="dark", photo=f"{SANG}, terrified, pale face, sweating, raising both hands, standing by red car",
         move="shake", lines=[("강상철", "아, 아니 그게… 형님들 오해십니다…")]),
    dict(dur=5.0, bg="dark", photo="huge korean man in black suit and sunglasses holding a smartphone, calm, serious, roadside",
         move="zoomin", lines=[("형님", "우리 법 지키며 사는 사람들이야."), ("형님", "블랙박스 영상, 방금 신고했다.")]),
    dict(dur=6.0, bg="dark", photo="korean police officer in uniform talking to a scared man in leather jacket next to a red car, police car lights",
         move="zoomin", lines=[("경찰", "어제 신고된 영상에도 이 차가 있네요."),
                               ("경찰", "보복운전은 형사처벌에 면허 정지, 취소까지 됩니다.")]),
    dict(dur=5.0, bg="dark", photo=f"{SUA}, standing on sidewalk, relieved gentle smile, people clapping in background",
         move="zoomin", lines=[("운전자1", "어제 그 초보 잘못 아니었네…"), ("수아", "도로는 혼자 쓰는 게 아니에요.")]),
    dict(dur=4.0, bg="lobby", phone="comments", comments_head="댓글 15,820개",
         comments=["형님들 준법정신 레전드", "클락션 빌런 우리 동네에도 있음", "초보 괴롭히는 거 진짜 싫다", "블랙박스는 필수",
                   "다음 편 빨리"], chars=[], lines=[(None, "그날, 강상철의 면허는 취소됐다.")]),
    dict(dur=4.5, bg="dark", photo=f"{SANG}, sitting on a crowded city bus, annoyed, a man next to him sitting with legs spread wide taking two seats",
         move="zoomin", lines=[(None, "면허를 잃고 버스를 탄 상철. 그런데 옆자리에…")]),
    dict(dur=3.0, bg="dark", end=True, chars=[], lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
