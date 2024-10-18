import App from "@/App.vue";
import router from "./router/index.js";
import { createApp } from "vue";

import vue3GoogleLogin from "vue3-google-login";

import "vue-connect-wallet/dist/style.css";
import "./style.css";

const app = createApp(App);

app.use(router);
app.use(vue3GoogleLogin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
});
app.mount("#app");
