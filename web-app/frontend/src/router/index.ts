// @ts-expect-error: Vue router routes import from directory structure
import routes from "~pages";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
