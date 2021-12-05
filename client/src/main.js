import Vue from 'vue'
import App from './App.vue'
import router from './utils/routes'
import { BootstrapVue} from 'bootstrap-vue'

Vue.config.productionTip = false

Vue.use(router);
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
