<template>
  <v-card class = " d-flex align-center justify-center" color= "white">
    <v-card color= "white" flat>
        <vrack v-if = 'onick.length > 0' :col = 'colourcode[opponent[onick[0]]["id"]]'></vrack>
    </v-card>
    <v-card color= "white" flat class ="d-flex flex-column">
      <v-card color= "white" flat >
        <hrack v-if = 'onick.length > 1' :col = 'colourcode[opponent[onick[1]]["id"]]'></hrack>
      </v-card>
      <v-card color= "white" flat class ="d-flex">
        <board :key = turn></board>
      </v-card>
      <v-card color= "white" flat class ="d-flex align-center justify-center" >
        <v-card color= "white"  flat align = "center" justify = "center" v-if= "isPlayer === 'player'" >
          <prack :col = 'colourcode[player["id"]]' :key = turn></prack>
        </v-card>
        <v-card color= "white" flat align = "center" justify = "center" v-else>
          <hrack v-if = 'onick.length > 3' :col = 'colourcode[opponent[onick[3]]["id"]]'></hrack>
        </v-card>
      </v-card>
    </v-card>
    <v-card color= "white" flat class="d-flex">
      <vrack v-if = 'onick.length > 2' :col = 'colourcode[opponent[onick[2]]["id"]]'></vrack>
    </v-card>
  </v-card>
</template>

<script>
import Board from './Board.vue'
import hrack from './hrack.vue'
import vrack from './vrack.vue'
import prack from './prack.vue'
import store from '../../store/index'
export default {
  name: 'Table',
  components: {
    Board,
    hrack,
    vrack,
    prack
  },
  computed: {
    turn () {
      return store.getters.getturn
    }
  },
  data () {
    return {
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      },
      onick: Object.keys(store.state.opponent),
      opponent: store.state.opponent,
      player: store.state.player,
      isPlayer: store.state.gtype
    }
  }
}
</script>

<style scoped>
  table {
    border-collapse: collapse ;
    border: 3px rgb(78, 33, 33) solid ;
    border-collapse: collapse ;
    background: rgb(78, 33, 33);
  }
  .table{
    height: 710px;
    width: 710px;
  }
  .board{
    height: 600px;
    width: 600px;
    align-items: center;
  }
  .vrack{
    width: 50px;
    height: 600px;
  }
  .hrack{
    height: 50px;
    width: 700px;
  }
  .table td {
    border: 1px solid rgb(78, 33, 33);
    text-align: center;
    font-size: 1rem;
    margin: auto;
    /*padding: 2px;*/
  }
</style>
