# 인계 메모 (새 세션은 여기부터 읽기)

## 시작 의식
1. `.claude/skills/fable-playbook/SKILL.md`를 먼저 읽는다.
2. 이번 일에 몇 단계를 따를지 사용자에게 먼저 말하고 시작한다.

## 사용자
- 한국어로, 쉬운 말로 설명한다. 코딩을 잘 모르니 터미널 명령은 꼭 필요할 때만, 어디에 입력하는지까지 알려준다.
- 쉽게 지친다. 선택지를 늘어놓기보다 하나를 추천하고 바로 해준다.
- 주 사용: Claude 앱(클라우드 세션). 사용자 컴퓨터에는 Claude Code 터미널 환경이 없다고 보고 안내한다.

## 목표
- 로블록스 캐릭터로 만드는 "In this town…" 스타일 스토리 숏폼을 유튜브 쇼츠 / 인스타 릴스 / 틱톡에 올리기.
- 대본은 남의 영상을 베끼지 않고 같은 형식의 새 이야기로 쓴다.
- 관심 소재: 현실에 없을 법한 설정, 좀비/벙커/실험체 반전, 중국 숏폼식 인과응보(처음엔 주변이 다 오해 → 분노 → 사이다).

## 지금까지 된 것 (2026-11-24)
- fable-playbook 스킬: 이 저장소 `main`에 있음.
- Uplika: claude.ai 커넥터로 연결됨. 사용자가 Uplika에 유튜브, 틱톡, 인스타(릴스) 계정을 추가해 둠.
  게시·예약·댓글·DM은 반드시 내용·계정·시간을 보여주고 "네"를 받은 뒤 실행한다.
  계정 확인은 `list_accounts`부터.
- 클라우드 환경 네트워크에 `docs.vibemake.kr` 허용됨. 그 사이트 자료 76개(PDF)를 zip으로 받아서 사용자에게 줬음.
  자료는 저장소에 넣지 않는다(남의 자료라 공개 저장소에 올리지 않음).
  필요하면 `https://docs.vibemake.kr/downloads/<파일명>`으로 다시 받는다.
  예: reels-automation-5step.pdf, uplika-yt-start.pdf, video-6channels.pdf
- 대본 1편 완성: `scripts/01-no-name-on-the-door.md`
- 인과응보 편 대본 `scripts/02-karma-interview.md` + 영상 `output/02-karma-interview.mp4`(97초, 목소리 있음).
  영상은 `video/make_karma.py`로 만든다(블록 캐릭터 + 자막, 나눔고딕 폰트는 pip의 koreanize-matplotlib 패키지에서 꺼내 씀).
  목소리: `video/tts_karma.py`(Supertonic 오픈소스 한국어 TTS, 목소리 F1~F5/M1~M5) → 녹음 폴더를 VOICE_DIR로 주고 make_karma.py 실행.
  모델 받기는 HF_HUB_DISABLE_XET=1 필요. 네트워크에 huggingface.co, us.aws.cdn.hf.co, cas-bridge.xethub.hf.co 허용됨.
  사용자 반응: 인과응보 막장 드라마를 아주 좋아함 → 이 장르 위주로.

## 게시 기록
- 02편 (2026-11-24): 유튜브 https://www.youtube.com/watch?v=xep_XDk6Ibs , 인스타 https://www.instagram.com/reel/DgHvfxTjwk5/
  틱톡은 Uplika 틱톡 한도(tiktok_creator_cap)로 실패 → 예약 게시 post_66a15d3b0b8a2b6d 로 Uplika가 자동 재시도 중. get_post로 확인.
- 업로드: media_presign → curl PUT(네트워크에 s3.us-west-004.backblazeb2.com 허용됨) → media_complete → publish.
- 유튜브 채널의 "아동용 여부"가 미설정 → 사용자가 YouTube Studio(설정→채널→고급 설정)에서 정해야 함.
- GitHub 저장소는 공개. 사용자가 올리는 것 승인함.

## 다음 할 일 후보
- 목소리 버전 피드백 받기(목소리 바꾸기, 속도, 길이 줄이기)
- 인과응보 편 파트 2(지민의 복수)
- 1편 파트 2, 또는 다른 인과응보 대본 (소재 목록은 `scripts/ideas.md`)
- 대본 → 영상 만들기 방법 정하기 (로블록스 녹화 + 음성 + 자막)
- Uplika로 첫 영상 올리기 (먼저 보여주고 승인받기)
