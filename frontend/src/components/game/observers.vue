<template>
  <v-card v-if="oa && observers.length > 0" color="secondary" >
    <v-row >
      <v-col><h3 class="primary--text">OBSERVERS: </h3></v-col>
      <v-col v-for="i in observers" :key="i">
        <h3 class="primary--text" v-if="i === gamernick">YOU</h3>
        <h3 class="primary--text" v-else> {{i}}</h3>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import store from '../../store/index'
export default {
  name: 'observers',
  computed: {
    observers () {
      return store.getters.getobserve
    }
  },
  data () {
    return {
      oa: store.state.oa,
      gamernick: store.state.gamernick
    }
  }
}
</script>

<style scoped>
div{
  margin: auto;
}
</style>
