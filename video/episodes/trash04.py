"""종량제 봉투 빌런 4화: 잠긴 옥상의 비밀 (공용 옥상 사유화). 지어낸 이야기.

3화 떡밥("옥상은 이제 내 거야")을 받는다. 한미숙이 공용 옥상을 잠그고 장독대·텃밭으로 쓴다.
오해: 소방 점검 때 지원이 신고했다며 이웃들이 원망. 사이다: 소방관 "옥상은 비상시 대피 공간, 잠그면 안 된다" + 불난 척 훈련에서 잠긴 문 확인.
"""

STYLE = "ref"
PHOTO_MODEL = "rv"
TITLE = ("", "")
END = ("다음 편", "한미숙 자매의 마지막 카드?", "팔로우하고 다음 편 보기")

HAN = "middle-aged korean woman in her late 50s, wrinkled aged face, sagging cheeks, short curly permed hair, leopard print blouse"
MJ = "rich elderly korean woman in her 60s, wrinkled face, elegant gray bob hair, fur coat, pearl earrings, arrogant"
JI = "korean woman in her 20s, long straight black hair, white shirt"
NB1 = "elderly korean woman in her late 60s, wrinkled face, gray streaked short permed hair, purple blouse"
NB2 = "elderly korean man in his late 60s, wrinkled face, gray hair, beige cardigan"
FF = "korean male firefighter in his 40s, orange fire uniform, helmet under arm"

S = [
    # --- 첫 장면: 대화 훅 ---
    dict(dur=3.0, photos=[f"{HAN} blocking a locked rooftop door with her arms spread, {JI} in front of her, narrow staircase",
                          f"extreme close-up of {HAN}, hostile glare!"],
         lines=[("한미숙", "내 장독 건드리기만 해 봐!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {JI}, serious, worried"],
         lines=[("지원", "옥상은 모두가 쓰는 공간이에요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB2}, irritated, waving his hand"],
         lines=[("이웃2", "아이고, 장독 몇 개 갖고 또 싸워?")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB1}, tired sigh"],
         lines=[("이웃1", "지원 씨, 이번엔 좀 그냥 넘어가.")]),
    # --- 회상 ---
    dict(dur=3.0, sepia=True, photos=["villa rooftop covered with many korean traditional jars and vegetable pots, private garden, no people"],
         lines=[(None, "한미숙은 공용 옥상을 장독대와 텃밭으로 바꿔 버렸다.")]),
    dict(dur=3.0, sepia=True, photos=[f"{HAN} snapping a padlock shut on the rooftop door, satisfied smile"],
         lines=[(None, "그리고 문을 잠갔다. 열쇠는 한미숙에게만 있었다.")]),
    dict(dur=2.5, sepia=True, photos=[f"close-up portrait of {JI}, worried, looking up at a locked door"],
         lines=[("지원", "불이라도 나면 어디로 피하지…")]),
    # --- 소방 점검 날 ---
    dict(dur=3.0, flash=True, photos=[f"{FF} walking up a villa staircase with a clipboard", f"close-up portrait of {FF}, serious"],
         lines=[("소방관", "정기 소방 점검 나왔습니다. 옥상 문 열어 주세요.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, angry, pointing at someone off-screen!"],
         lines=[("한미숙", "너지? 네가 신고했지?!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {NB1}, glaring sideways, suspicious"],
         lines=[("이웃1", "결국 일을 키웠구먼…")]),
    dict(dur=3.0, photos=[f"close-up portrait of {FF}, firm, holding a clipboard"],
         lines=[("소방관", "신고 아닙니다. 정기 점검이에요.")]),
    dict(dur=3.0, photos=["close-up of a heavy padlock and chain on a rooftop door, firefighter gloved hand touching it",
                          f"close-up portrait of {FF}, stern"],
         lines=[("소방관", "옥상은 불이 났을 때 대피하는 공간입니다. 잠그시면 안 됩니다.")]),
    dict(dur=3.0, photos=[f"extreme close-up of {HAN}, shocked, speechless!", "close-up of a written fire safety violation notice, no people"],
         lines=[("소방관", "바로 열어 두시고, 옥상 물건도 치우셔야 합니다.")]),
    dict(dur=2.5, photos=[f"close-up portrait of {HAN}, flustered, desperate"],
         lines=[("한미숙", "우리 언니가 건물주라고!")]),
    dict(dur=2.5, photos=[f"close-up portrait of {FF}, calm, unimpressed"],
         lines=[("소방관", "건물주라도 마찬가지입니다.")]),
    dict(dur=3.0, photos=[f"{NB2} carrying jars down from the rooftop with other residents, rooftop door open, daylight",
                          f"close-up portrait of {NB2}, embarrassed smile"],
         lines=[("이웃2", "지원 씨 말이 맞았네. 우리 다 위험할 뻔했어.")]),
    dict(dur=3.0, photos=[f"{JI} standing on an open clean villa rooftop at sunset, wind in her hair, peaceful"],
         lines=[("지원", "모두의 길은, 모두를 위해 열어 둬야죠.")]),
    # --- 떡밥 ---
    dict(dur=3.0, photos=[f"{HAN} and {MJ} whispering together in a dark car, scheming"],
         lines=[(None, "그날 밤, 한미숙 자매는 몰래 만났다.")]),
    dict(dur=3.0, flash=True, photos=[f"extreme close-up of {MJ}, cold smile, holding a sale contract document"],
         lines=[("한미자", "이 빌라, 통째로 팔아 버리면 되지.")]),
    dict(dur=3.0, end=True, lines=[]),
]
for _s in S:
    _s.setdefault("chars", [])
    _s.setdefault("bg", "dark")
