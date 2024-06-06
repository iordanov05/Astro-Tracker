import { createApp } from 'vue'
import { createWebHistory, createRouter } from 'vue-router'
import App from './App.vue'

import Home from './pages/Home.vue'
import Contacts from './pages/Contacts.vue'
import Error from './pages/Error.vue'
import ServiceInf from './pages/ServiceInf.vue'

const app = createApp(App)

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/contacts', name: 'Contacts', component: Contacts },
    { path: '/service', name: 'ServiceInf', component: ServiceInf},
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: Error },
  ]

const router = createRouter({
    history: createWebHistory(),
    routes
})

app.use(router)

app.mount('#app')
