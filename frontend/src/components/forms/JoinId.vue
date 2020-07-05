<template>
  <v-fade-transition appear>
    <v-form
      ref="form"
    >
      <v-card>
        <v-card-text>
          <v-row
            align="center"
            justify="center"
            class="secondary--text"
          >
            <h1 >Join With ID</h1>
          </v-row>
          <v-row dense align="center"
            justify="center">
            <v-col>
              <v-text-field
                label="Game ID"
                placeholder="Enter Game ID..."
                v-model="jgameid"
                outlined
                block
                color="secondary"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn
                block
                color="secondary"
                large
                @click.prevent="jwroom" :disabled = "!(connection && jgameid !== '')"
              >As player</v-btn>
            </v-col>
            <v-col>
              <v-btn
                block
                color="secondary"
                large
                @click.prevent="ojoin" :disabled = "!(connection && jgameid !== '')"
              >As Observer</v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import store from '../../store/index'
export default {
  name: 'JoinId',
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
      jgameid: ''
    }
  },
  methods: {
    jwroom () {
      const gdata = { room: this.jgameid, gamer: this.gamernick }
      store.dispatch('setgtype', 'player')
      this.$socket.emit('join', gdata)
    },
    ojoin () {
      const gdata = { room: this.jgameid, gamer: this.gamernick }
      store.dispatch('setgtype', 'observer')
      this.$socket.emit('ojoin', gdata)
    }
  }
}
</script>
