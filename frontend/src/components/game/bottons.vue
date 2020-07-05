<template>
  <v-container>
    <v-row align="center" justify= "center">
      <v-col>
        <v-btn @click.prevent = "toswap" :disabled = 'allowswap' block color = "secondary">
          swap
        </v-btn>
      </v-col>
      <v-col>
        <v-btn @click.prevent = 'play' block color = "secondary">
          play
        </v-btn>
      </v-col>
      <v-col>
        <v-btn @click.prevent = "pass" block color = "secondary">
          pass
        </v-btn>
      </v-col>
      <v-col>
        <v-btn @click.prevent="onClear" block color = "secondary">
          clear
        </v-btn>
      </v-col>
    </v-row>
    <v-row align = "center" justify = "center" v-if = "msg !== ''">
      <v-col align = "center" justify = "center">
        <h4 color = "red">{{msg}}</h4>
      </v-col>
    </v-row>
  </v-container>
  <!-- <div>
    <div>
      <Span>
        <button @click.prevent = 'play'>
          PLAY
        </button>
      </Span>
      <Span>
        <button @click.prevent = "toswap" :disabled = 'allowswap' >
          SWAP
        </button>
      </Span>
      <Span>
        <button @click.prevent = "pass">
          PASS
        </button>
      </Span>
      <Span>
        <button @click.prevent="onClear" >
          CLEAR
        </button>
      </Span>
    </div> -->
    <!-- <div v-if = "msg !== ''"> {{msg}} </div> -->
    <!-- <div v-if = "playedwords.length !== 0">
      <p v-for = "i in playedwords.length" :key ='i' >{{playedwords[i - 1]}}</p>
    </div> -->
  <!-- </div> -->
</template>

<script>
import store from '../../store/index'
import axios from 'axios'
export default {
  computed: {
    playcheck () {
      return store.getters.noT
    },
    allowswap () {
      if (store.state.bag > 10) {
        return false
      } else {
        return true
      }
    }
  },
  data () {
    return {
      msg: '',
      // playedwords: [],
      pwt: store.getters.noT,
      played: 'disabled',
      bag: store.state.bag
    }
  },
  methods: {
    play () {
      if (Object.keys(store.state.tonboard).length > 0) {
        const payload = { board: store.state.boardl, tiles: store.state.tonboard, rule: store.state.settings.rules, language: store.getters.getlanguage }
        const path = this.$myhost + '/api/played'
        axios.post(path, payload).then((res) => {
          if (res.data.status === 'failed') {
            this.msg = res.data.msg
          } else if (res.data.status === 'success') {
            this.msg = 'You Played'
            const gdata = { gamer: store.state.gamernick, room: store.state.gameId, tiles: store.state.tonboard, pwords: res.data.words, score: res.data.score, rule: store.state.settings.rules }
            this.$socket.emit('played_game', gdata)
            store.dispatch('playtilea')
            // this.playedwords = res.data.words
          }
        }).catch((error) => {
          console.log(error)
        })
      } else {
        this.msg = 'You have not played'
      }
    },
    onClear (event) {
      this.$emit('clicked')
    },
    toswap () {
      this.$emit('swapb')
    },
    pass () {
      const gdata = { gamer: store.state.gamernick, room: store.state.gameId }
      this.$socket.emit('passed', gdata)
    }
  }
}
</script>
