import * as THREE from 'three';

/** Placeholder arena: circular floor, a ring of pillars and dim lighting. */
export function createArena(scene: THREE.Scene): void {
  scene.background = new THREE.Color(0x0b0a09);
  scene.fog = new THREE.Fog(0x0b0a09, 20, 60);

  const floor = new THREE.Mesh(
    new THREE.CircleGeometry(18, 72),
    new THREE.MeshStandardMaterial({ color: 0x2a2622, roughness: 0.95 }),
  );
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  const pillarGeo = new THREE.CylinderGeometry(0.6, 0.7, 6, 12);
  const pillarMat = new THREE.MeshStandardMaterial({ color: 0x4a443c, roughness: 0.9 });
  for (let i = 0; i < 12; i++) {
    const a = (i / 12) * Math.PI * 2;
    const pillar = new THREE.Mesh(pillarGeo, pillarMat);
    pillar.position.set(Math.cos(a) * 16, 3, Math.sin(a) * 16);
    pillar.castShadow = true;
    scene.add(pillar);
  }

  scene.add(new THREE.HemisphereLight(0x8a8070, 0x1a1612, 0.6));
  const moon = new THREE.DirectionalLight(0xd8cdb8, 1.4);
  moon.position.set(8, 16, 6);
  moon.castShadow = true;
  moon.shadow.mapSize.set(2048, 2048);
  Object.assign(moon.shadow.camera, { left: -20, right: 20, top: 20, bottom: -20 });
  scene.add(moon);
}
