<template>
  <v-container >
    <v-content >
      <v-row justify="center" align="center">
        <v-col justify="center" align="center">
          <v-card elevation = "12" align = "center">
            <v-row>
              <v-col v-if = "isHost" >
                <v-card color="secondary">
                  <h3>Click slot to Toggle between Human, Computer, and None</h3>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-card color="secondary">
                  <v-row>
                    <v-col>
                      <h4>GAME ID: {{gameId}}</h4>
                    </v-col>
                    <v-col>
                      <h4>TIME: {{setting['time']}}Seconds</h4>
                    </v-col>
                    <v-col>
                      <h4>RULES: {{setting['rules']}}</h4>
                    </v-col>
                    <v-col>
                      <h4>Language: {{language}}</h4>
                    </v-col>
                    <v-col>
                      <h4 v-if="oa"> OBSERVERS: Allowed</h4>
                      <h4 v-else> OBSERVERS: Not Allowed</h4>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
            <v-row class = "srow">
              <v-col class = "scol">
                <v-card elevation = "12"  color = "secondary">
                  <v-row>
                    <v-col>
                      <div class = "prac y" :style = "{ 'background-image' : 'url('+ require('../assets/pics/human.jpg') + ')' }">
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col align = "center">
                      <h3 v-if="slot['slot1']['nick']=== gamerNick"> YOU</h3>
                      <h3 v-else-if="slot['slot1']['nick']!== ''">{{slot['slot1']['nick']}}</h3>
                      <h3 v-else> Human</h3>
                    </v-col>
                  </v-row>
                  <v-row >
                    <v-col align = "center">
                      <h3>{{slot['slot1']['status']}}</h3>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
              <v-col class = "scol">
                <v-card elevation = "12"  color = "secondary" @click.stop @click.prevent = "stoggle('slot2')">
                  <v-row>
                    <v-col>
                      <div class = "prac g" :style = "{ 'background-image' : 'url('+ require('../assets/pics/human.jpg') + ')' }">
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col align = "center">
                      <h3 v-if="slot['slot2']['nick']=== gamerNick"> YOU</h3>
                      <h3 v-else-if="slot['slot2']['nick']!== ''">{{slot['slot2']['nick']}}</h3>
                      <h3 v-else> Human</h3>
                    </v-col>
                  </v-row>
                  <v-row >
                    <v-col align = "center">
                      <h3>{{slot['slot2']['status']}}</h3>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
              <v-col class = "scol">
                <v-card elevation = "12"  color = "secondary"  @click.stop @click.prevent = "stoggle('slot3')">
                  <v-row>
                    <v-col>
                      <div class = "prac b" :style = "{ 'background-image' : 'url('+ require('../assets/pics/human.jpg') + ')' }">
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col align = "center">
                      <h3 v-if="slot['slot3']['nick']=== gamerNick"> YOU</h3>
                      <h3 v-else-if="slot['slot3']['nick']!== ''">{{slot['slot3']['nick']}}</h3>
                      <h3 v-else> Human</h3>
                    </v-col>
                  </v-row>
                  <v-row >
                    <v-col align = "center">
                      <h3>{{slot['slot3']['status']}}</h3>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
              <v-col class = "scol">
                <v-card elevation = "12"  color = "secondary"  @click.stop @click.prevent = "stoggle('slot4')">
                  <v-row>
                    <v-col>
                      <div class = "prac r"  :style = "{ 'background-image' : 'url('+ require('../assets/pics/human.jpg') + ')' }">
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col align = "center">
                      <h3 v-if="slot['slot4']['nick']=== gamerNick"> YOU</h3>
                      <h3 v-else-if="slot['slot4']['nick']!== ''">{{slot['slot4']['nick']}}</h3>
                      <h3 v-else> Human</h3>
                    </v-col>
                  </v-row>
                  <v-row >
                    <v-col align = "center">
                      <h3>{{slot['slot4']['status']}}</h3>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn color = "red" @click="leaveroom" block>
                  Leave Room
                </v-btn>
              </v-col>
              <v-col >
                <v-btn v-if= "isHost" color = "secondary" block @click='startgame'> Start Game</v-btn>
                <v-btn v-else-if = "isPlayer==='player' && slot[myslot].status !== 'Ready'" color = "secondary" block  @click = 'playerready'> Ready</v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <observers></observers>
      </v-row>
    </v-content>
  </v-container>

</template>

<script>
import store from '../store/index'
import observers from '@/components/game/observers.vue'
export default {
  name: 'wroom',
  components: {
    observers
  },
  computed: {
    slot () {
      const slot = store.state.slot
      return slot
    },
    myslot () {
      const slot = store.state.slot
      if (slot.slot1.nick === store.state.gamernick) {
        return 'slot1'
      } else if (slot.slot2.nick === store.state.gamernick) {
        return 'slot2'
      } else if (slot.slot3.nick === store.state.gamernick) {
        return 'slot3'
      } else if (slot.slot4.nick === store.state.gamernick) {
        return 'slot4'
      } else {
        return 'slot9'
      }
    }
  },
  data () {
    return {
      isHost: store.state.isHost,
      gamerNick: store.state.gamernick,
      gameId: store.state.gameId,
      setting: store.state.settings,
      language: store.getters.getlanguage,
      isPlayer: store.state.gtype,
      oa: store.state.oa,
      complevel: 5,
      imgUrl: '../assets/pics/human.jpg'
    }
  },
  created () {
  },
  methods: {
    stoggle: function (sslot) {
      const type = this.slot[sslot].type
      if (this.isHost && (this.slot[sslot].nick === 'Computer' || this.slot[sslot].nick === 'Closed' || this.slot[sslot].nick === '')) {
        var newtype = {}
        if (type === 'Human') {
          newtype = { type: 'Computer', status: 'Ready', nick: 'Computer', level: this.complevel }
        } else if (type === 'Computer') {
          newtype = { type: 'None', status: 'Closed', nick: 'Closed' }
        } else if (type === 'None') {
          newtype = { type: 'Human', status: 'Waiting', nick: '' }
        }
        const gdata = { room: store.state.gameId, slot: sslot, info: newtype }
        this.$socket.emit('toggle_slot', gdata)
      }
    },
    leaveroom: function () {
      if (confirm('Are you sure you want to leave the room')) {
        const gdata = { room: store.state.gameId, gamerid: this.gamerNick }
        this.$socket.emit('leave_room', gdata)
      }
    },
    playerready () {
      const gdata = { room: store.state.gameId, gamerid: this.gamerNick }
      this.$socket.emit('p_ready', gdata)
    },
    startgame () {
      var pslot = store.state.slot
      var readySlot = ['slot1']
      var canStart = true
      var hPlayer = 1
      var cPlayer = 0
      Object.keys(pslot).forEach((key) => {
        if (pslot[key].nick === '') {
          alert('You must close all empty slot before starting the game')
          canStart = false
        }
        if (pslot[key].type === 'Computer') {
          readySlot = [...readySlot, key]
          cPlayer = cPlayer + 1
          if (cPlayer > 1) {
            canStart = false
            alert('There must be at most ONE computer player')
          }
        }
        if (pslot[key].status === 'Not Ready') {
          alert('Can not start unit all players are ready')
          canStart = false
        }
        if (pslot[key].type === 'Human' && pslot[key].status === 'Ready') {
          readySlot = [...readySlot, key]
          hPlayer = hPlayer + 1
        }
      })
      if ((hPlayer < 2) && canStart) {
        canStart = false
        alert('There must be at least TWO player')
      }
      if (canStart) {
        const gdata = { room: store.state.gameId, slot: readySlot }
        this.$socket.emit('start_game', gdata)
        console.log(readySlot)
      }
    }
  }
}
</script>

<style scoped>
*{
  margin: 10px;
}
.observe {
  padding: 10px;
  margin: auto;
  border: 10px;
}
.mbox{
  display: inline-flex;
  align-items: center;
  width: 800px;
  height: 350px;
  margin: auto;
}
.main{
  padding: 5px;
  background-color: rgba(134, 124, 124, 0.212);
  width: 1000px;
  max-height: 500px;
  margin: auto;
  display: block
}
.boxi{
  width: 25%;
}
h3, h4 {
  color: white
}
.srow {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(200px,auto));
}
.scol .v-card {
  height: 400px
}
.pbtn{
  width: 100px;
  height: 100px;
  cursor: pointer;
  border: none;
}
.prac{
  width: 120px;
  height: 120px;
  margin: auto;
  border-radius: 50%;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-image: url('../assets/pics/human.jpg')
}
.y{
  border: 2px solid orange;
}
.b{
  border: 2px solid blue;
}
.g{
  border: 2px solid green
}
.r{
  border: 2px solid red;
}
</style>
