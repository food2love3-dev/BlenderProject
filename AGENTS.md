\# Blender Project Agent Rules



\## General



항상 작업 전에 현재 Blender Scene을 확인한다.



사용자가 요청하지 않은 기존 오브젝트는 삭제하지 않는다.



큰 작업은 여러 단계로 나누어 수행한다.



작업 완료 후 Scene 상태를 검증한다.



\## Subagent Delegation



모델링 작업:

blender\_modeler



재질 및 셰이더:

blender\_material



조명:

blender\_lighting



카메라 및 구도:

blender\_camera



최종 검수:

blender\_qa



\## Workflow



일반적인 Blender 제작 작업은 다음 순서를 고려한다.



1\. Scene 분석

2\. 모델링

3\. 재질

4\. 카메라

5\. 조명

6\. QA



서로 독립적인 작업은 가능한 경우 병렬화한다.



의존성이 있는 작업은 순차적으로 실행한다.



최종 작업 전에 blender\_qa를 사용하여 Scene을 검수한다.



QA에서 ERROR가 발견되면 문제를 수정한 뒤 다시 검수한다.



\## Blender MCP



Blender MCP를 사용할 수 있는 경우 실제 Blender Scene을 기준으로 작업한다.



단순히 Python 코드를 작성하고 작업이 완료되었다고 가정하지 않는다.



실제 Scene 상태를 확인한다.

