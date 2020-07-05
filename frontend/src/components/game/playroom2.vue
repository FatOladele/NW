<template >
  <v-container>
    <v-content>
      <v-row block>
        <v-col>
          <v-card>
            <v-row>
              <v-col>
                <v-row>
                  <v-col>
                    <vpinfo v-if = 'onick.length > 1' :id= 'opponent[onick[1]]["id"]' :nick = 'onick[1]'></vpinfo>
                  </v-col>
                </v-row>
                <v-row block>
                  <v-col>
                    <vpinfo v-if = 'onick.length > 0' :id= 'opponent[onick[0]]["id"]' :nick = 'onick[0]'></vpinfo>
                  </v-col>
                  <v-col>
                    <vpinfo></vpinfo>
                  </v-col>
                  <v-col>
                    <Table :key = 'refresh + letter'></Table>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <vpinfo></vpinfo>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card>
            <v-row v-if="isPlayer==='player'">
              <v-col>
                <v-card>
                  <v-row v-if = "turn == player['id']">
                    <v-col v-if= "createSwap">
                      <srack @cancel = 'cancel' @swapped = 'swapped'></srack>
                    </v-col>
                    <v-col v-else>
                      <botton @clicked = 'refreshtable' @swapb = 'swap'></botton>
                    </v-col>
                  </v-row>
                  <v-row v-else-if="turn == 5">
                    <v-col align = "center">
                      <h3 class = "primary--text align-center" >PROBE?</h3>
                    </v-col>
                    <v-col>
                      <v-btn color = "primary" @click.prevent="probe('yes')" >YES</v-btn>
                    </v-col>
                    <v-col>
                      <v-btn color = "primary" @click.prevent="probe('no')" >NO</v-btn>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <blankselector v-show='selector'>
      </blankselector>
      <endgame v-show="endgame">
      </endgame>
    </v-content>
  </v-container>
</template>

<script>
// @ is an alias to /src
import Table from './Table.vue'
import store from '../../store/index'
import vpinfo from '../player/vpinfo'
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
    endgame
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
  .game td{
    height: 5rem;
    width: 5rem;
    border: 2px ;
    text-align: center;
    font-size: 2rem;
    align-items: center;
    /*padding: 2px;*/
  }
  .game{
    width: 100%;
    height: 100%;
    margin: auto;
    /* background-color: rgb(157, 157, 219); */
    align-items: center;
    vertical-align: center;
  }
  .main{
    width: 920px;
    height:920px;
    margin: 5px;
    background-color: rgb(157, 157, 219);
    align-items: center;
    border: 3px solid black;
  }
  span{
    margin-right: 5px;
    display: inline-block
  }
</style>
