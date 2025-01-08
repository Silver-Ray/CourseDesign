import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  base: './', // 配置静态文件的公共路径
  build: {
    outDir: 'dist', // 输出目录
    assetsDir: 'assets', // 静态资源目录
  },
  plugins: [vue()],
});
