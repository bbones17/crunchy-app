import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import router from './router'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { BootstrapIconsPlugin } from "bootstrap-icons-vue";
import App from './App.vue'

const store = createPinia()


createApp(App).use(router).use(store).use(BootstrapIconsPlugin).mount('#app')
