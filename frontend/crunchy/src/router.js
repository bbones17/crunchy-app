import { createMemoryHistory, createRouter, } from 'vue-router'
import MainComp from './components/main/MainComp.vue'
import ShoppingCart from './components/cart/ShoppingCartComp.vue';
import LoginComp from './components/user/LoginComp.vue';
import RegisterComp from './components/user/RegisterComp.vue';
import PayComp from './components/cart/PayComp.vue';
import ProfileComp from './components/user/ProfileComp.vue'


const routes = [
    { path: '/', component: LoginComp },
    { path: '/register', component: RegisterComp},
    { path: '/profile', component: ProfileComp},
    { path: '/', component: LoginComp},
    { path: '/main', component: MainComp},
    { path: '/cart', component: ShoppingCart},
    { path: '/pay', component: PayComp},

];

const router = createRouter({
    history: createMemoryHistory(),
    routes,
});

export default router