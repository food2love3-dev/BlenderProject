import { defineConfig } from 'vite';

export default defineConfig({
  server: { port: 5173, open: true },
  // three.js alone is ~500 kB minified, so the default warning is just noise.
  build: { target: 'es2022', sourcemap: true, chunkSizeWarningLimit: 1000 },
});
