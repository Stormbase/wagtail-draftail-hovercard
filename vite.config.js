import { defineConfig } from "vite";
import path from "path";

export default defineConfig({
  build: {
    outDir: path.resolve("./wagtail_draftail_hovercard/static/wagtail_draftail_hovercard/"),
    emptyOutDir: true,
    lib: {
      entry: "./client/entrypoint.js",
      name: "wagtail-draftail-hovercard",
      formats: ["umd"],
      fileName: () => "wagtail-draftail-hovercard.js",
    },
  },
});
