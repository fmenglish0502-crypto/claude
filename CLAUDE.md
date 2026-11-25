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
파일 번호와 화수가 하나씩 어긋남(01은 영상 없는 좀비 대본): 02=1화, 03=2화, 04=3화, 05=4화, 06=5화.
이야기는 한 시리즈로 이어짐: 매 화 엔딩 떡밥을 다음 화가 받는다. 서연·회장님 고정, 매 화 새 악역이 혼난다.
| 편 | 제목 | 대본 | 영상 | 게시 |
|---|---|---|---|---|
| 02 | 할머니를 밀친 여자의 충격적인 최후 | `scripts/02-karma-interview.md` | `output/02-karma-interview.mp4` | 유튜브 https://www.youtube.com/watch?v=xep_XDk6Ibs · 인스타 https://www.instagram.com/reel/DgHvfxTjwk5/ · 틱톡: 아래 참고 |
| 03 | 할머니 밀친 여자의 복수, 라이브로 자폭하다 | `video/episodes/ep03.py` | `output/03-jimin-revenge.mp4` | 유튜브 https://www.youtube.com/watch?v=jlTr04L14mo · 인스타 https://www.instagram.com/reel/DgHzJXiGbzD/ · 틱톡: 아래 참고 |
| 04 | 목걸이 도둑으로 몰린 신입, 회장님의 충격 고백 | `video/episodes/ep04.py` | `output/04-chairman-secret-x1.5.mp4`(1.5배 63초) | 유튜브 https://www.youtube.com/watch?v=U5N_-yPZQho · 인스타 https://www.instagram.com/reel/DgJkYWNI0ss/ · 틱톡 예약 post_cb70fa1f4528cdbb (2026-11-25 03:51Z, media med_57518f9011d5edcb) |
| 05 | 후계자 쫓아내려던 손자, 이사회에서 벌어진 일 | `video/episodes/ep05.py` | `output/05-grandson-revenge-x1.5.mp4`(1.5배 51초) | 유튜브 https://www.youtube.com/watch?v=P8ohcR7NP-Q · 인스타 https://www.instagram.com/reel/DgJsffih4AS/ · 틱톡 예약 post_a5b0cde23693eca2 (2026-11-25 05:02Z, media med_0c7639d9649c027f) |
| 06 | 손잡은 두 악녀? (05편 엔딩: 사모님이 지민에게 전화 "이제 네 차례야") | 아직 | | |

별도: `scripts/01-no-name-on-the-door.md`(좀비 벙커, 영상 없음), 소재 목록 `scripts/ideas.md`.

## 새 편 만드는 법 (그대로 따라 하면 됨)
1. `video/episodes/ep03.py`를 복사해 `epXX.py`를 만든다. TITLE(상단 2줄), END(엔딩 3줄), S(장면 목록)만 바꾼다.
   - 장면: dur, bg(bus/street/lobby/room/office/night/mansion/dark), chars[(이름,x,발y,크기,포즈,표정,왼쪽보기,움직임)], lines[(화자 또는 None=내레이션, 대사)]
   - 포즈: stand/walk/point/push/phone/help/shock/fall. 표정: normal/smile/smirk/angry/shock/sad/sweat/calm. 움직임: bob/shake/run/("slide",거리)/None
   - 휴대폰 화면: phone="views"(feed_title,feed_views,feed_comments) / "comments"(comments_head,comments) / "live"(chat) / "post"(post_title,post_body…) / "blackbox"
   - 연출: zoom=(시작,끝), flash=True(효과음 '둥'), fg=True(면접실 책상), sepia=True(회상), clock=False(거리 배경 시계 숨김), monitor="글자"(night 배경 모니터 글자)
   - 편 파일 안에 ROOM_TEXT / LOBBY_TEXT로 room·lobby 간판 글자를 바꿀 수 있음.
   - blackbox는 bb_label, bb_chars[(이름,포즈,표정,왼쪽보기,크기,x,y)], bb_circle로 CCTV처럼 바꿀 수 있음. phone="necklace"(가방 속 목걸이)
   - 새 캐릭터는 파일 안 CHARS에 추가. 새 화자는 `video/tts_karma.py`의 VOICE(F1~F5 여성, M1~M5 남성)에 추가.
2. 폰트: `pip download --no-deps koreanize-matplotlib` 후 whl을 풀면 NanumGothic ttf가 나옴 (스크래치 폴더에).
3. 목소리 + 영상:
   ```
   cd video && export EP=episodes/epXX.py HF_HUB_DISABLE_XET=1
   pip install supertonic==1.3.1   # 없으면
   python3 tts_karma.py <녹음폴더>
   VOICE_DIR=<녹음폴더> python3 make_karma.py <폰트폴더> ../output/XX-이름.mp4
   ```
4. **속도: 시청자 피드백 '느리다' → 1.5배속이 기본.** 완성 후 아래로 변환해서 올린다(목소리 높낮이 유지):
   `ffmpeg -i XX.mp4 -filter_complex "[0:v]setpts=PTS/1.5,fps=30[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -movflags +faststart XX-x1.5.mp4`
   02·03편 1.5배 버전: `output/02-karma-interview-x1.5.mp4`(64초), `output/03-jimin-revenge-x1.5.mp4`(68초). 틱톡에 이 버전 사용 중.
5. 장면 몇 개를 PNG로 뽑아 직접 눈으로 확인(`make_karma.py <폰트> <출력접두어> 2,5,9`)한 뒤 사용자에게 보낸다.

## 게시하는 법 (Uplika 커넥터)
- 계정(전부 active): 유튜브 레이지오너 `conn_80fcdb1e67921088`, 틱톡 동그란아보카도 `conn_a2e4d86dacf4fc0d`, 인스타 penguin.4736671 `conn_e7d4400461ac67f8`.
- 순서: media_presign → curl PUT(업로드 주소) → media_complete → **사용자에게 제목·설명·계정·시간 보여주고 "네" 받기** → publish(wait:true) → get_post로 링크 확인.
- 틱톡은 매번 get_publish_options 먼저. 공개 PUBLIC_TO_EVERYONE, isAigc true.
- 유튜브: title 필수, privacyStatus public, containsSyntheticMedia false(만화라서), madeForKids false(사용자가 채널 설정 변경함).
- 인스타: contentType reel, shareToFeed true, isAiGenerated true.
- publish가 시간 초과되면 다시 올리지 말고 list_posts / get_post로 먼저 확인(중복 방지).
- 틱톡 실패 코드 tiktok_creator_cap = Uplika 전체 한도 초과. scheduledAt 15분 뒤로 틱톡만 다시 publish하면 Uplika가 12시간 동안 매시간 자동 재시도. retry_post는 자동 재시도를 멈추니 쓰지 말 것.
- 틱톡은 1.5배 버전으로 교체함(옛 예약 2개는 삭제). 계속 tiktok_creator_cap(Uplika 쪽 한도)으로 실패 중.
  - 02편 1.5배: post_b39c6bbc216503fd (16:19Z 예약, media med_be0a8ba6b1b1b367)
  - 03편 1.5배: post_7f3645d9030ddf5e (16:34Z 예약, media med_6bfba9f6fd5c70a0)
  - 2026-11-25 03:30Z 기준 02·03 둘 다 아직 failed(자동 재시도는 각각 04:19Z, 04:34Z까지). 04편 틱톡도 위 표 참고.
  - 예약 후 12시간 동안 매시간 자동 재시도. 그 뒤에도 failed면: 옛 예약을 delete_post로 지우고 같은 media로 틱톡만 다시 예약 (media는 2026-11-26 15:58Z까지 유효, 지나면 다시 업로드).
  - 며칠째 계속 안 되면 사용자에게 "틱톡 앱에서 직접 올리기"를 제안(그때는 Uplika 예약을 먼저 지워서 중복 방지).
- scheduledAt은 반드시 '지금+20분'으로 (date 명령으로 계산 직후 바로 호출, 10분 미만이면 거절됨).
- 게시 설명 예시: 훅 한 줄 + "파트 N 보고 싶으면 댓글로 'OO'" + 해시태그(#인과응보 #사이다 #숏드라마 #막장드라마 #반전 #shorts)

## 클라우드 환경 (이미 설정됨)
허용된 주소: docs.vibemake.kr(자료 PDF), huggingface.co / us.aws.cdn.hf.co / cas-bridge.xethub.hf.co(목소리 모델), s3.us-west-004.backblazeb2.com(Uplika 업로드).
docs.vibemake.kr 자료(PDF 76개)는 사용자에게 zip으로 줬음. 남의 자료라 저장소에는 넣지 않는다.

## GitHub
저장소 `fmenglish0502-crypto/claude`(공개). 사용자가 main에 올리는 것을 승인함. 작업이 끝날 때마다 커밋하고 push.

## 다음 할 일
1. 02·03편 틱톡 예약 결과 확인 (list_posts). 실패했으면 다시 예약.
2. 06편 「손잡은 두 악녀?」(사모님+지민) 대본+영상 → 1.5배 → 승인 → 게시.
4. 반응 보기: 게시 후 하루 지나면 get_insights / list_replies로 조회수·댓글 정리해서 알려주기.
