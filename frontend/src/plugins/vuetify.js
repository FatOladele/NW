import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#ffffff',
        secondary: '#008753',
        third: '#ffffff',
        background: '#008753'
      }
    }
  }
})
