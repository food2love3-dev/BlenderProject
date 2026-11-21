# Windows 환경설정: 직접 해야 하는 일

저장소 골격은 이미 만들어 두었습니다. 아래 항목은 **사용자 PC나 계정에서 직접** 해야 하는 작업입니다.

## 1. 필수 설치

| 프로그램 | 버전 | 설치 방법 | 확인 명령 |
|---|---|---|---|
| Git for Windows | 최신 | https://git-scm.com/download/win | `git --version` |
| Node.js | 24 LTS (22 이상이면 됨) | https://nodejs.org 또는 `winget install OpenJS.NodeJS.LTS` | `node -v`, `npm -v` |
| VS Code | 최신 | https://code.visualstudio.com | 저장소를 열면 추천 확장이 안내됨 |
| Blender | 4.x LTS 권장 | https://www.blender.org/download/lts/ | `blender --version` (PATH에 추가한 경우) |

## 2. 저장소 받기와 실행

```powershell
git clone https://github.com/food2love3-dev/BlenderProject.git C:\AI\Projects\BlenderProject
cd C:\AI\Projects\BlenderProject
npm install
npm run dev
```

브라우저에 어두운 원형 아레나와 회전하는 캡슐이 보이면 정상입니다. **Shift**를 누르고 있으면 0.25배 감속이 적용됩니다(감속 테스트용).

> [!NOTE]
> 예전에 받아 둔 로컬 폴더가 있다면, 이번 정리로 파일이 삭제된 상태가 됩니다. `git pull`을 하거나, 폴더를 지우고 다시 clone하세요. 정리 전 상태는 `backup/pre-reset-2026-11-20` 태그로 남겨 두었습니다.

## 3. 선택 사항 (필요할 때 연결)

- **Blender MCP**: AI 에이전트가 실행 중인 Blender Scene을 직접 확인하거나 조작하려면 PC에 Blender MCP 애드온과 서버를 설치하고 에이전트 도구에 연결해야 합니다. 연결하지 않으면 Blender 작업은 스크립트 작성 + 사용자 실행 방식으로 진행합니다.
- **Git LFS**: `.blend`, 텍스처, 오디오 파일이 커지면(수십 MB 이상) `git lfs install` 후 LFS 추적을 켜는 것을 권장합니다. 지금은 꺼져 있습니다.
- **GitHub Pages / CI**: 빌드 결과를 웹에 올려 공유하거나, PR마다 자동으로 타입 검사를 하려면 GitHub Actions를 추가합니다. 원하시면 요청해 주세요.
- **GitHub 저장소 이름**: 지금 저장소는 웹 게임과 Blender를 함께 담고 있지만 이름은 `BlenderProject`입니다. 이름을 바꾸려면 GitHub 저장소 Settings → Rename에서 바꾸면 됩니다.

## 4. Blender → 게임 에셋 흐름 (예정)

1. `blender/source/*.blend`에서 작업합니다.
2. `blender/scripts/`의 내보내기 스크립트로 `.glb`를 만들어 `game/public/assets/models/`에 둡니다.
3. 게임 코드에서 `GLTFLoader`로 불러옵니다.

> 웹 프로토타입에서는 단위 1 = 1m, Y-up(glTF 기본값), 적용된 트랜스폼(스케일 1)을 기준으로 합니다.
