import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import "vue-connect-wallet/dist/style.css";
import "./style.css";
import vue3GoogleLogin from 'vue3-google-login';

let app = createApp(App);

app.use(router);
app.use(vue3GoogleLogin, {
    clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID
});
app.mount("#app");
