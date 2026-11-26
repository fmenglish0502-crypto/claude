"""시집살이 4부: 유언장. 시누이 부부가 아버지를 몰래 모시고 가 '집은 딸에게' 각서에 도장을 받으려 한다.
게시 제목 안: "아픈 아버지 몰래 데려가 도장 받으려던 시누이 부부, 공증 변호사가 꺼낸 유언장에 무릎 꿇었다"
사이다: 이미 공증된 유언장(간병한 며느리에게 감사의 몫, 나머지는 법대로) + 판단력 흐린 사람에게 받은 각서는 효력이 없을 수 있다.
법 대사는 "~될 수 있다" 수준. 떡밥(5부): 고서방의 진짜 정체?
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
PART = ("시집살이", "4부")
END = ("5부 예고", "고서방의 진짜 정체?", "팔로우하고 다음 편 보기")

GO = "elderly korean old lady aged 65, wrinkled aged face, graying short tight permed hair, red lipstick, burgundy cardigan, gold necklace"
EUN = "korean woman in her early 30s, low ponytail, gentle face, beige blouse"
JUN = "korean man in his mid 30s, short neat hair, round face, navy polo shirt"
AUNT = "korean woman in her late 60s, gray hair in a bun, green quilted jacket"
SIS = "korean woman in her late 30s, long curled brown hair, designer clothes, sunglasses on her head"
SH = "korean man in his 40s, slicked back hair, thin mustache, white shirt, flashy gold watch"
FA = "frail korean man in his early 70s, thin white hair, gray pajamas"
LAWYER = "korean male notary lawyer in his 50s, gray side-parted hair, dark suit, holding a leather folder"

S = [
    dict(dur=3.0, photos=[f"{SH} pressing a stamp into the hand of {FA} at a table while {SIS} holds a paper",
                          f"close-up portrait of {SH}, greedy grin, single person!*"],
         lines=[("고서방", "장인어른, 여기 도장만 콱!")]),
    dict(dur=2.5, photos=[f"{EUN} bursting through a door, shocked"],
         lines=[("은서", "지금 뭐 하시는 거예요?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SIS}, defiant, single person!"],
         lines=[("시누이", "남의 집 일에 며느리가 왜 끼어?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, conflicted, single person"],
         lines=[("고정숙", "그래도 딸이 아빠 생각해서 그러는 거야…")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=[f"{SIS} helping {FA} into a car at night, looking around nervously"],
         lines=[("시누이", "아빠, 바람 쐬러 가요~")]),
    dict(dur=3.0, sepia=True, photos=["close-up of a handwritten memorandum saying the house goes to the daughter, a red stamp, no people"],
         lines=[("고서방", "집은 딸한테 준다, 이 한 줄이면 끝이야.")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {FA}, confused, drowsy, single person"],
         lines=[("시아버지", "여기가… 어디냐?")]),
    # --- 사이다 ---
    dict(dur=3.0, flash=True, photos=[f"{LAWYER} entering the living room, family turning around",
                                      f"close-up portrait of {LAWYER}, calm, single person"],
         lines=[("공증변호사", "아버님 유언장은, 이미 한 달 전에 공증을 마쳤습니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SH}, shocked, mouth open, single person!"],
         lines=[("고서방", "공… 공증이요?")]),
    dict(dur=3.0, photos=[f"close-up portrait of {LAWYER}, reading a document, single person"],
         lines=[("공증변호사", "판단이 흐린 분께 받은 각서는, 효력이 없을 수 있습니다.")]),
    dict(dur=3.0, photos=["close-up of an official notarized will document with a seal, no people",
                          f"close-up portrait of {LAWYER}, serious, single person"],
         lines=[("공증변호사", "간병한 며느리 은서 씨에게 감사의 몫을, 나머지는 법대로.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {SIS}, crying, furious, single person!"],
         lines=[("시누이", "며느리가 왜 받아! 남이잖아!")]),
    dict(dur=3.0, photos=[f"close-up portrait of {FA}, clear-eyed, firm, single person"],
         lines=[("시아버지", "아픈 애비 곁을 지킨 사람이, 남이냐?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {GO}, ashamed, tearful, single person"],
         lines=[("고정숙", "은서야… 그동안 미안했다.")]),
    dict(dur=3.0, photos=[f"{EUN} holding the hand of {FA} on a sunny porch", f"close-up portrait of {EUN}, gentle smile, single person"],
         lines=[("은서", "저는 돈보다, 아버님이 편하신 게 좋아요.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{SH} on the phone in a dark alley, sweating"],
         lines=[("고서방", "형님들, 돈은 조금만 더 기다려 주세요…")]),
    dict(dur=3.0, flash=True, photos=["close-up of a debt collection notice with a red stamp addressed to the husband, no people"],
         lines=[("준호", "고서방… 빚이 10억이라고?")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
