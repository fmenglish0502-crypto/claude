# 인계 메모 (새 세션은 여기만 읽고 바로 시작)

## 시작 의식
1. `.claude/skills/fable-playbook/SKILL.md`를 먼저 읽는다.
2. 이번 일에 몇 단계를 따를지 사용자에게 한 줄로 말하고 바로 시작한다.

## 사용자
- 한국어, 쉬운 말. 코딩 모름. 터미널 명령을 시키지 말고 내가 직접 한다.
- 쉽게 지친다. 선택지 나열 대신 하나 추천하고 바로 해준다.
- Claude 앱(클라우드 세션)으로 쓴다.

## 목표
로블록스풍 블록 캐릭터 숏폼 드라마를 만들어 유튜브 쇼츠 / 인스타 릴스 / 틱톡에 꾸준히 올리기.
사용자가 제일 좋아하는 장르: **중국 숏폼식 인과응보 막장 드라마** (주변이 다 오해 → 분노 → 한 방에 사이다 → 다음 편 떡밥).
대본은 남의 영상을 베끼지 않고 새 이야기로 쓴다.

## 시리즈 현황 (인과응보 시리즈: 서연 / 지민 / 할머니=한결그룹 회장)
| 편 | 제목 | 대본 | 영상 | 게시 |
|---|---|---|---|---|
| 02 | 할머니를 밀친 여자의 충격적인 최후 | `scripts/02-karma-interview.md` | `output/02-karma-interview.mp4` | 유튜브 https://www.youtube.com/watch?v=xep_XDk6Ibs · 인스타 https://www.instagram.com/reel/DgHvfxTjwk5/ · 틱톡: 아래 참고 |
| 03 | 할머니 밀친 여자의 복수, 라이브로 자폭하다 | `video/episodes/ep03.py` | `output/03-jimin-revenge.mp4` | 아직 (Uplika 업로드 완료 media id med_63f225a413b28cf2, 2026-11-26까지 유효. 승인 대기) |
| 04 | 회장님의 진짜 정체? (03편 엔딩 떡밥) | 아직 | | |

별도: `scripts/01-no-name-on-the-door.md`(좀비 벙커, 영상 없음), 소재 목록 `scripts/ideas.md`.

## 새 편 만드는 법 (그대로 따라 하면 됨)
1. `video/episodes/ep03.py`를 복사해 `epXX.py`를 만든다. TITLE(상단 2줄), END(엔딩 3줄), S(장면 목록)만 바꾼다.
   - 장면: dur, bg(bus/street/lobby/room/office/night/dark), chars[(이름,x,발y,크기,포즈,표정,왼쪽보기,움직임)], lines[(화자 또는 None=내레이션, 대사)]
   - 포즈: stand/walk/point/push/phone/help/shock/fall. 표정: normal/smile/smirk/angry/shock/sad/sweat/calm. 움직임: bob/shake/run/("slide",거리)/None
   - 휴대폰 화면: phone="views"(feed_title,feed_views,feed_comments) / "comments"(comments_head,comments) / "live"(chat) / "post"(post_title,post_body…) / "blackbox"
   - 연출: zoom=(시작,끝), flash=True(효과음 '둥'), fg=True(면접실 책상)
   - 새 캐릭터는 파일 안 CHARS에 추가. 새 화자는 `video/tts_karma.py`의 VOICE(F1~F5 여성, M1~M5 남성)에 추가.
2. 폰트: `pip download --no-deps koreanize-matplotlib` 후 whl을 풀면 NanumGothic ttf가 나옴 (스크래치 폴더에).
3. 목소리 + 영상:
   ```
   cd video && export EP=episodes/epXX.py HF_HUB_DISABLE_XET=1
   pip install supertonic==1.3.1   # 없으면
   python3 tts_karma.py <녹음폴더>
   VOICE_DIR=<녹음폴더> python3 make_karma.py <폰트폴더> ../output/XX-이름.mp4
   ```
4. 장면 몇 개를 PNG로 뽑아 직접 눈으로 확인(`make_karma.py <폰트> <출력접두어> 2,5,9`)한 뒤 사용자에게 보낸다.

## 게시하는 법 (Uplika 커넥터)
- 계정(전부 active): 유튜브 레이지오너 `conn_80fcdb1e67921088`, 틱톡 동그란아보카도 `conn_a2e4d86dacf4fc0d`, 인스타 penguin.4736671 `conn_e7d4400461ac67f8`.
- 순서: media_presign → curl PUT(업로드 주소) → media_complete → **사용자에게 제목·설명·계정·시간 보여주고 "네" 받기** → publish(wait:true) → get_post로 링크 확인.
- 틱톡은 매번 get_publish_options 먼저. 공개 PUBLIC_TO_EVERYONE, isAigc true.
- 유튜브: title 필수, privacyStatus public, containsSyntheticMedia false(만화라서), madeForKids false(사용자가 채널 설정 변경함).
- 인스타: contentType reel, shareToFeed true, isAiGenerated true.
- publish가 시간 초과되면 다시 올리지 말고 list_posts / get_post로 먼저 확인(중복 방지).
- 틱톡 실패 코드 tiktok_creator_cap = Uplika 전체 한도 초과. scheduledAt 15분 뒤로 틱톡만 다시 publish하면 Uplika가 12시간 동안 매시간 자동 재시도. retry_post는 자동 재시도를 멈추니 쓰지 말 것.
- 02편 틱톡: 예약 post_66a15d3b0b8a2b6d (10:49Z 첫 시도 실패, 2026-11-24 22:49Z까지 자동 재시도). 그 뒤에도 failed면 다시 예약.
- 게시 설명 예시: 훅 한 줄 + "파트 N 보고 싶으면 댓글로 'OO'" + 해시태그(#인과응보 #사이다 #숏드라마 #막장드라마 #반전 #shorts)

## 클라우드 환경 (이미 설정됨)
허용된 주소: docs.vibemake.kr(자료 PDF), huggingface.co / us.aws.cdn.hf.co / cas-bridge.xethub.hf.co(목소리 모델), s3.us-west-004.backblazeb2.com(Uplika 업로드).
docs.vibemake.kr 자료(PDF 76개)는 사용자에게 zip으로 줬음. 남의 자료라 저장소에는 넣지 않는다.

## GitHub
저장소 `fmenglish0502-crypto/claude`(공개). 사용자가 main에 올리는 것을 승인함. 작업이 끝날 때마다 커밋하고 push.

## 다음 할 일
1. 03편 게시 승인받고 3곳에 올리기.
2. 04편 「회장님의 진짜 정체?」 대본+영상 → 승인 → 게시.
3. 02편 틱톡 재시도 결과 확인.
4. 반응 보기: 게시 후 하루 지나면 get_insights / list_replies로 조회수·댓글 정리해서 알려주기.
