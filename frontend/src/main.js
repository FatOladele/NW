import VueSocketio from 'vue-socket.io'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
// Vue.prototype.$myhost = 'http://864db28c27f2.ngrok.io'
Vue.prototype.$myhost = 'http://127.0.0.1:5000'
// Vue.prototype.$myhost = 'http://192.168.43.90:5000/'
Vue.use(new VueSocketio({
  debug: true,
  // connection: 'http://192.168.43.90:5000',
  // connection: 'http://864db28c27f2.ngrok.io',
  connection: 'http://127.0.0.1:5000',
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  },
  options: { pingTimeout: 300000 }
}))
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
