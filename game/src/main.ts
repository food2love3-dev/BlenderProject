import * as THREE from 'three';
import { GameLoop } from './core/GameLoop';
import { createArena } from './scene/createArena';

const canvas = document.querySelector<HTMLCanvasElement>('#game')!;
const debug = document.querySelector<HTMLDivElement>('#debug')!;

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, 1, 0.1, 200);
camera.position.set(0, 6, 12);
camera.lookAt(0, 1, 0);

createArena(scene);

// Placeholder player capsule
const player = new THREE.Mesh(
  new THREE.CapsuleGeometry(0.4, 1.0, 4, 12),
  new THREE.MeshStandardMaterial({ color: 0xb08a5a, roughness: 0.7 }),
);
player.position.y = 0.9;
player.castShadow = true;
scene.add(player);

function resize(): void {
  const { innerWidth: w, innerHeight: h } = window;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}
window.addEventListener('resize', resize);
resize();

const loop = new GameLoop(({ dt, unscaledDt, timeScale }) => {
  player.rotation.y += dt * 0.8; // scaled: slows down with timeScale
  renderer.render(scene, camera);
  debug.textContent = `fps ${(1 / Math.max(unscaledDt, 1e-4)).toFixed(0)}\ntimeScale ${timeScale}`;
});

// Temporary: hold Shift to preview 0.25x slow-down
window.addEventListener('keydown', (e) => e.key === 'Shift' && (loop.timeScale = 0.25));
window.addEventListener('keyup', (e) => e.key === 'Shift' && (loop.timeScale = 1));

loop.start();
