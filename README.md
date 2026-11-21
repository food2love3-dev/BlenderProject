# Magic Circle RPG (웹 프로토타입)

마법진 조립 실시간 액션 RPG를 **Three.js + TypeScript + Vite** 웹 프로토타입으로 검증하는 모노레포입니다.

> [!CAUTION]
> `docs/`의 기획·설계 자료는 AI와 함께 작성한 초안이라 오류나 모순이 있을 수 있습니다. 구현하면서 계속 검증하고 고쳐 나갑니다.

## 폴더 구조

```
game/                 웹 게임 (Vite + TypeScript + three.js)
  src/core/           게임 루프 (scaled / unscaled 델타 분리)
  src/scene/          씬 구성 (임시 아레나)
  public/assets/      런타임 에셋 (Blender에서 내보낸 .glb 위치)
blender/
  source/             .blend 원본
  scripts/            Blender Python 스크립트 (생성, 검증, 내보내기)
docs/                 설계 문서, 환경설정 가이드
```

## 빠른 시작 (Windows)

```powershell
git clone https://github.com/food2love3-dev/BlenderProject.git C:\AI\Projects\BlenderProject
cd C:\AI\Projects\BlenderProject
npm install
npm run dev        # 브라우저에서 http://localhost:5173 이 자동으로 열림
```

| 명령 | 설명 |
|---|---|
| `npm run dev` | 개발 서버 실행 (코드를 저장하면 바로 반영) |
| `npm run typecheck` | TypeScript 타입 검사 |
| `npm run build` | 배포용 빌드 (`game/dist`) |

필요한 프로그램 설치와 연결 방법은 [docs/SETUP_WINDOWS.md](docs/SETUP_WINDOWS.md)를 참고하세요.
