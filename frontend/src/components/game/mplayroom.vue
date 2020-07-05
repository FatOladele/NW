<template >
  <v-card class ="d-inline-block mainroom" color = "white">
    <v-card class= "d-inline-flex align-center justify-center">
      <minfo v-if="isPlayer==='player'" :id= 'player["id"]' :nick = 'gamernick' :col = 'colourcode[player["id"]]' :score = 'player["score"]'></minfo>
      <minfo v-if='onick.length > 0' :id= 'opponent[onick[0]]["id"]' :nick = 'onick[0]' :col = 'colourcode[opponent[onick[0]]["id"]]' :score = 'opponent[onick[0]]["score"]'></minfo>
      <minfo v-if='onick.length > 1'  :id= 'opponent[onick[1]]["id"]' :nick = 'onick[1]' :col = 'colourcode[opponent[onick[1]]["id"]]' :score = 'opponent[onick[1]]["score"]'></minfo>
      <minfo v-if='onick.length > 2'  :id= 'opponent[onick[2]]["id"]' :nick = 'onick[2]' :col = 'colourcode[opponent[onick[2]]["id"]]' :score = 'opponent[onick[2]]["score"]'></minfo>
      <minfo v-if='onick.length > 3'  :id= 'opponent[onick[3]]["id"]' :nick = 'onick[3]' :col = 'colourcode[opponent[onick[3]]["id"]]' :score = 'opponent[onick[3]]["score"]'></minfo>
    </v-card>
    <v-card class = "d-inline-block">
      <boardm :key = "turn + refresh"></boardm>
    </v-card>
    <v-card color= "white"  flat align = "center" justify = "center" v-if= "isPlayer === 'player'" >
      <prack :col = 'colourcode[player["id"]]' :key = "turn + refresh"></prack>
    </v-card>
    <v-card class = "d-flex flex-column" color = "secondary">
      <v-card color = "white" flat class= "d-inline-flex align-center justify-center" v-if="isPlayer==='player'">
        <v-row v-if = "turn == player['id']">
          <v-col align="center"
              justify="center" v-if= "createSwap">
            <srack @cancel = 'cancel' @swapped = 'swapped'></srack>
          </v-col>
          <v-col align="center"
              justify="center" v-else>
            <botton @clicked = 'refreshtable' @swapb = 'swap'></botton>
          </v-col>
        </v-row>
        <v-row align = "center" justify = "center" v-else-if="turn == 5">
          <v-col align = "center" >
            <h3 class = "secondary--text">PROBE?</h3>
          </v-col>
          <v-col>
            <v-btn color="secondary" @click.prevent="probe('yes')" >YES</v-btn>
          </v-col>
          <v-col>
            <v-btn color="secondary" @click.prevent="probe('no')" >NO</v-btn>
          </v-col>
        </v-row>
      </v-card>
      <v-card class= "d-inline-flex align-center justify-center" >
        <v-row align = "center" justify = "center">
          <v-col align = "center" justify = "center">
            <span align = "center" justify = "center" class="secondary--text">{{activities[0]}}</span>
          </v-col>
        </v-row>
      </v-card>
    </v-card>
    <blankselector v-show='selector'>
    </blankselector>
    <endgame v-show="endgame">
    </endgame>
  </v-card>
</template>

<script>
// @ is an alias to /src
import store from '../../store/index'
import botton from './bottons'
import Boardm from './Boardm'
import srack from './srack'
import prack from './prack'
import axios from 'axios'
import minfo from '../player/minfo'
import blankselector from './blankselector'
import endgame from './endgame'
export default {
  name: 'Room',
  components: {
    botton,
    srack,
    blankselector,
    endgame,
    Boardm,
    prack,
    minfo
  },
  computed: {
    turn () {
      return store.getters.getturn
    },
    letter () {
      return store.getters.getrack.length
    },
    selector () {
      return store.getters.bsgetter
    },
    endgame () {
      return store.getters.getend
    },
    activities () {
      return store.getters.actgetters
    }
  },
  data () {
    return {
      player: store.state.player,
      onick: Object.keys(store.state.opponent),
      opponent: store.state.opponent,
      refresh: 0,
      createSwap: false,
      gamernick: store.state.gamernick,
      isPlayer: store.state.gtype,
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      }
    }
  },
  methods: {
    refreshtable () {
      store.dispatch('cleartiles')
      this.refresh++
    },
    swap () {
      this.createSwap = true
    },
    cancel () {
      store.dispatch('clearswaptile')
      this.createSwap = false
      this.refresh++
    },
    swapped () {
      if (store.state.swaptiles.length < 1) {
        alert('YOU HAVE NOT SELECTED ANY LETTER TO SWAPPED')
      } else {
        const payload = { room: store.state.gameId, rack: store.state.rack, swaptiles: store.state.swaptiles }
        const path = this.$myhost + '/api/swap'
        axios.post(path, payload).then((res) => {
          if (res.data.status === 'success') {
            const gdata = { gamer: store.state.gamernick, room: store.state.gameId, nswap: store.state.swaptiles.length }
            this.$socket.emit('swapped', gdata)
            store.dispatch('swapped', res.data.rack)
            this.createSwap = false
            this.refresh++
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    probe (res) {
      store.dispatch('proberes')
      const gdata = { gamer: store.state.gamernick, room: store.state.gameId, response: res }
      this.$socket.emit('res_probe', gdata)
    }
  }
}
</script>

<style scoped>
  .mainroom {
  }
</style>
