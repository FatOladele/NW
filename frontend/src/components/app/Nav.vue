<template>
  <v-bottom-navigation
    app
    grow
    :style = "{'background': $vuetify.theme.themes.light.background}"
  >
    <v-btn v-if="isConnected && !isLogin" class="primary--text" >
      <span class="primary--text">Log in</span>
      <v-icon medium class="primary--text">mdi-alert</v-icon>
    </v-btn>
    <v-btn
      color="red darken-3"
      v-if="!isConnected"
      value="false"
      class="primary--text"
    >
      <span>Not Connected</span>
      <v-icon medium>mdi-alert</v-icon>
    </v-btn>

    <v-btn
      v-else
    >
      <span class="primary--text">{{gamernick}}</span>
      <v-badge
        color="primary"
        class="primary--text"

      >
        <v-icon medium>mdi-account</v-icon>
      </v-badge>
    </v-btn>
    <v-btn @click.stop="drawer = !drawer" class="primary--text">
      <span class="primary--text">Menu</span>
      <v-icon medium class="primary--text">mdi-menu</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import store from '../../store/index'
export default {
  computed: {
    isConnected () {
      return store.getters.getconnection
    },
    gamernick () {
      return store.state.gamernick
    },
    isLogin () {
      return store.state.gatlogin
    }
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
