import path from "path";
import vueSvg from "vite-svg-loader";
import vue from "@vitejs/plugin-vue";
import vitePages from "vite-plugin-pages";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  clearScreen: false,
  server: {
    port: 3000,
  },
  plugins: [
    vue(),
    vueSvg(),
    // https://github.com/hannoeru/vite-plugin-pages#configuration
    vitePages({
      dirs: "src/**/pages",
    }),
  ],
  resolve: {
    alias: {
      process: "process/browser",
      stream: "stream-browserify",
      zlib: "browserify-zlib",
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
