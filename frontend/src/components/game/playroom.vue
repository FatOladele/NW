<template >
  <v-card class ="d-flex mainroom" color = "white">
    <v-card class = "d-flex flex-column" color = "secondary">
      <v-card class= "d-flex flex-column flex-nowrap" flat color = "green">
        <v-card class = "d-flex align-center justify-center" flat  color = "white">
          <hpinfo v-if = 'onick.length > 1' :id= 'opponent[onick[1]]["id"]' :nick = 'onick[1]'></hpinfo>
        </v-card>
        <v-card class = "d-flex" flat>
          <v-card class = " d-flex align-center justify-center" flat color = "white">
            <vpinfo v-if = 'onick.length > 0' :id= 'opponent[onick[0]]["id"]' :nick = 'onick[0]'></vpinfo>
          </v-card>
          <v-card class = "d-flex align-center justify-center" color = "white">
            <Table :key = 'refresh + letter'></Table>
          </v-card>
          <v-card class = "d-flex align-center justify-center" flat color = "white">
            <vpinfo v-if = 'onick.length > 2' :id= 'opponent[onick[2]]["id"]' :nick = 'onick[2]'></vpinfo>
          </v-card>
        </v-card>
        <v-card class = "d-flex align-center justify-center" flat color = "white">
          <v-card v-if="isPlayer==='player'" flat>
            <hpinfo :id= 'player["id"]' :nick = 'gamernick'></hpinfo>
          </v-card>
          <v-card class = "d-flex align-center justify-center" flat color = "white" v-else>
            <hpinfo v-if = 'onick.length > 3' :id= 'opponent[onick[3]]["id"]' :nick = 'onick[3]'></hpinfo>
          </v-card>
        </v-card>
      </v-card>
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
            <h3 class = "primary--text">PROBE?</h3>
          </v-col>
          <v-col>
            <v-btn color="secondary" @click.prevent="probe('yes')" >YES</v-btn>
          </v-col>
          <v-col>
            <v-btn color="secondary" @click.prevent="probe('no')" >NO</v-btn>
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
import Table from './Table.vue'
import store from '../../store/index'
import vpinfo from '../player/vpinfo'
import hpinfo from '../player/hpinfo'
import botton from './bottons'
import srack from './srack'
import axios from 'axios'
import blankselector from './blankselector'
import endgame from './endgame'
export default {
  name: 'Room',
  components: {
    Table,
    vpinfo,
    botton,
    srack,
    blankselector,
    endgame,
    hpinfo
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
      isPlayer: store.state.gtype
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
    min-width: 700px;
  }
</style>
