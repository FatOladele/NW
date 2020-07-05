<template>
  <v-navigation-drawer
    temporary
    right
    app
    v-model="drawer"
  >
    <v-list class="pa-1">
      <v-list-item>
        <v-row>
          <v-column>

          </v-column>
        </v-row>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  data () {
    return {
      
    }
  },
  computed: {
    ...mapState(['connected', 'game']),
    ...mapGetters(['username']),
    drawer: {
      get () {
        return this.$store.state.drawer
      },
      set (v) {
        return this.$store.commit('set_drawer', v)
      }
    }
  }
}
</script>

<style>
</style>
