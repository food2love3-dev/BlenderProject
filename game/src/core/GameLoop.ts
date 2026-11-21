/**
 * Frame timing with separate scaled / unscaled delta.
 * Gameplay should use `dt` (affected by timeScale, e.g. 0.25 slow-down);
 * camera, UI and input aggregation should use `unscaledDt`.
 */
export interface FrameTime {
  dt: number;
  unscaledDt: number;
  elapsed: number;
  timeScale: number;
}

export type FrameCallback = (time: FrameTime) => void;

const MAX_DT = 0.1; // clamp long frames (tab switch, breakpoints)

export class GameLoop {
  timeScale = 1;
  private elapsed = 0;
  private last = 0;
  private rafId = 0;

  constructor(private readonly onFrame: FrameCallback) {}

  start(): void {
    this.last = performance.now();
    const tick = (now: number) => {
      const unscaledDt = Math.min((now - this.last) / 1000, MAX_DT);
      this.last = now;
      const dt = unscaledDt * this.timeScale;
      this.elapsed += dt;
      this.onFrame({ dt, unscaledDt, elapsed: this.elapsed, timeScale: this.timeScale });
      this.rafId = requestAnimationFrame(tick);
    };
    this.rafId = requestAnimationFrame(tick);
  }

  stop(): void {
    cancelAnimationFrame(this.rafId);
  }
}
