"""시집살이 3부: 쓰러진 시아버지 간병은 은서 혼자. 시누이는 병문안 사진만 찍어 올리고 '효녀' 행세, 생신상도 자기가 차렸다고 생색.
게시 제목 안: "병간호는 며느리한테 떠넘기고 SNS엔 효녀 코스프레한 시누이, 아버님 한마디에 얼어붙었다"
사이다: 시아버지가 직접 "매일 온 건 은서야" + 병원 방문 기록. 떡밥: 시아버지가 변호사를 부른다(유언장).
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("시집살이", "3부")
END = ("4부 예고", "아버님의 유언장?", "팔로우하고 다음 편 보기")

GO = "korean woman in her early 60s, sharp narrow face, tight short dark permed hair, red lipstick, burgundy cardigan, gold necklace"
EUN = "korean woman in her early 30s, low ponytail, gentle face, beige blouse"
JUN = "korean man in his mid 30s, short neat hair, round face, navy polo shirt"
AUNT = "korean woman in her late 60s, gray hair in a bun, green quilted jacket"
SIS = "korean woman in her late 30s, long curled brown hair, designer clothes, sunglasses on her head"
SH = "korean man in his 40s, slicked back hair, thin mustache, white shirt, flashy gold watch"
FA = "frail korean man in his early 70s, thin white hair, gray pajamas"

S = [
    dict(dur=3.0, photos=[f"{SIS} posing for a selfie beside a hospital bed while {EUN} holds a bedpan behind her",
                          f"close-up portrait of {SIS}, fake sweet smile, holding a phone, single person!*"],
         lines=[("시누이", "올케, 사진 찍게 좀 비켜 봐~")]),
    dict(dur=2.5, photos=[f"close-up portrait of {EUN}, tired, dark circles, single person"],
         lines=[("은서", "아가씨, 한 달 만에 오셨잖아요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, irritated, single person!"],
         lines=[("고정숙", "바쁜 애가 와 준 게 어디야!")]),
    dict(dur=2.5, photos=["close-up of a smartphone screen showing a social media post with hospital photo and many likes, no people"],
         lines=[("시고모", "어머, 우리 조카가 효녀네~")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{EUN} feeding porridge to {FA} in a hospital room at night",
                                      f"close-up portrait of {FA}, weak grateful eyes, single person"],
         lines=[("시아버지", "아가… 오늘도 왔구나.")]),
    dict(dur=3.0, sepia=True, photos=[f"{EUN} cooking a birthday table with seaweed soup in a kitchen at dawn"],
         lines=[("은서", "아버님 생신상은… 제가 차려야지.")]),
    dict(dur=3.0, sepia=True, photos=[f"close-up portrait of {SIS}, smug, in front of a birthday table, single person"],
         lines=[("시누이", "아빠 생신상, 내가 새벽부터 차렸어~")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{FA} sitting up in the hospital bed, family gathered around",
                                      f"close-up portrait of {FA}, stern, single person"],
         lines=[("시아버지", "그만들 해라.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {FA}, serious, pointing, single person"],
         lines=[("시아버지", "석 달 동안 매일 온 사람은, 은서 하나였다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SIS}, shocked, pale, single person!"],
         lines=[("시누이", "아빠! 나도 왔잖아!")]),
    dict(dur=3.0, photos=["close-up of a hospital visitor log book with handwritten names and dates, no people",
                          f"close-up portrait of {JUN}, reading a notebook, serious, single person"],
         lines=[("준호", "방문 기록에… 누나는 딱 두 번이네.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {FA}, sad, single person"],
         lines=[("시아버지", "생신상 미역국 맛도, 내가 모를 줄 알았니?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, guilty, looking down, single person"],
         lines=[("고정숙", "은서야… 내가 너무했다.")]),
    dict(dur=3.0, photos=[f"close-up portrait of {EUN}, tearful gentle smile, single person"],
         lines=[("은서", "사진보다, 곁에 있는 게 효도예요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{FA} handing a business card to {JUN} in a hospital room"],
         lines=[("시아버지", "준호야, 변호사 좀 불러다오.")]),
    dict(dur=3.0, flash=True, photos=[f"{SIS} and {SH} whispering in a dark hospital hallway, scheming"],
         lines=[("고서방", "유언장 쓰기 전에… 손 써야겠는데?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
