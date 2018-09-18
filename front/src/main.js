// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'
import 'mint-ui/lib/style.css'
import Mint from 'mint-ui'
import Storage from 'vue-web-storage'

Vue.use(Storage)
Vue.use(Mint)
Vue.use(VueResource)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  data: {
    config: {
      api_url: 'http://localhost:5000/api/',
      bd_url: 'https://about-623b5.firebaseio.com/sh0p/'
    }
  },
  components: { App },
  template: '<App/>'
})
