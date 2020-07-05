<template>
  <div>
    <div>
      <div v-if="gamemode === 'join'">
        <button @click="creategame"> CREATE GAME</button>
        <br>
        <button @click="vscomputer"> PLAY WITH COMPUTER</button>
        <br>
        <span>JOIN GAME</span>
        <br>
        <label for="gameid">GAME ID</label>
        <input v-model ='jgameid' type="text" name = "gameid" placeholder="Enter Game ID">
        <br>
        <button @click.prevent="jwroom" :disabled = "!(connection && jgameid !== '')"> AS PLAYER </button>
        <button @click.prevent="ojoin" :disabled = "!(connection && jgameid !== '')"> AS OBSERVER </button>
      </div>
      <div v-else-if="gamemode === 'create'">
        <div>
          <h4>Rules</h4>
          <div>
            <input value = 'Standard' v-model = 'cgrules' type="radio" name="Standard" id="Stardard" checked = "checked">
            <label for="Standard"> Standard</label>
            <input value = 'Custom' v-model = 'cgrules' type="radio" name="Custom" id="Custom" >
            <label for="Custom" > Custom</label>
          </div>
          <div>
            <input v-model.number = 'cgtime' type="number" name="ptime" id="ptime" min = "5" max= "10" placeholder="5">
            <label for="ptime"> mins For each player</label>
          </div>
          <div>
            <input type="checkbox" name="observers" id="observers" v-model="observer">
            <label for="observers"> Allow observers</label>
          </div>
          <div>
            <button @click="back"> BACK</button>
            <button :disabled = '!connection' @click = 'cwroom'> CREATE</button>
          </div>
        </div>
      </div>
      <div v-else-if="gamemode === 'computer'">
        <h4>Rules</h4>
        <div>
          <input type="radio" name="Standard" id="Stardard" value = "Standard" v-model="vscomps" checked = "checked">
          <label for="Standard"> Standard (No dictionary, limited time)</label>
          <input type="radio" name="Custom" id="Custom"  value = "Custom" v-model="vscomps">
          <label for="Basic" disabled = "disabled"> Basic (Dictionary, unlimited time)</label>
        </div>
        <div v-if="vscomps === 'Standard'">
          <input v-model.number = 'cgtime' type="number" name="ptime" id="ptime" min = "5" max= "10" placeholder="5">
          <label for="ptime"> mins</label>
        </div>
        <div>
          <input type="range" name="complevel" id="complevel"  min = "1" max= "5" step="1" v-model="complevel" >
          <label for="complevel"> Computer difficulty</label>
        </div>
        <div>
          <button @click="back"> BACK</button>
          <button :disabled = '!connection' @click="startvscomp"> PLAY</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '../../store/index'
export default {
  name: 'setting',
  computed: {
    connection () {
      return store.state.connection
    },
    gamernick () {
      return store.state.gamernick
    }
  },
  data () {
    return {
      gamemode: 'join',
      vscomps: 'Standard',
      cgrules: 'Standard',
      cgtime: 5,
      observer: false,
      jgameid: '',
      complevel: 1
    }
  },
  methods: {
    creategame () {
      this.gamemode = 'create'
    },
    vscomputer () {
      this.gamemode = 'computer'
    },
    vscop (e) {
    },
    back () {
      this.gamemode = 'join'
    },
    cwroom () {
      const gdata = { creator: this.gamernick, time: this.cgtime, rules: this.cgrules, observer: this.observer }
      store.dispatch('setgtype', 'player')
      this.$socket.emit('create', gdata)
    },
    jwroom () {
      const gdata = { room: this.jgameid, gamer: this.gamernick }
      store.dispatch('setgtype', 'player')
      this.$socket.emit('join', gdata)
    },
    ojoin () {
      const gdata = { room: this.jgameid, gamer: this.gamernick }
      store.dispatch('setgtype', 'observer')
      this.$socket.emit('ojoin', gdata)
    },
    startvscomp () {
      store.dispatch('setgtype', 'player')
      const data = { creator: this.gamernick, time: this.cgtime, rules: this.vscomps }
      store.dispatch('vscomp', data)
      this.$socket.emit('vscomputer', { player: this.gamernick, time: this.cgtime, rules: this.vscomps, level: this.complevel })
    }
  }
}
</script>

<style scoped>
*{
  margin: 5px
}
input[type=radio]:disabled+label {
  /* and changes its color to gray */
  color: gray;
}
input[type=checkbox]:disabled+label {
  /* and changes its color to gray */
  color: gray;
}
</style>
