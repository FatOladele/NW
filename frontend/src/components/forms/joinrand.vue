<template>
  <v-fade-transition appear>
    <v-form>
      <v-card>
        <v-card-text>
          <v-row>
            <v-col>
              <v-container>
                <h3 class="secondary--text">Rules</h3>
                <v-row>
                  <v-col>
                    <v-checkbox
                    color = "secondary"
                    value="Standard"
                    v-model = "rules"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">Standard</div>
                    </template>
                  </v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox
                    value="Custom"
                    color = "secondary"
                    v-model = "rules"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">Basic</div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
            </v-container>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <!-- <v-slider
                v-model="slider"
                class="align-center"
                :max="max"
                :min="min"
                hide-details
              >
              </v-slider> -->
              <v-select
                :items= "['English', 'Yoruba']"
                :menu-props="{ offsetY: true }"
                label="Language"
                hint = "Select your language"
                color = "secondary"
                class="secondary--text"
                v-model="language"
              ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <input class="secondary--text" diasbled = "disabled" colour = "secondary" v-model.number = 'time' type="number" name="ptime" id="ptime" min = "60" max= "120" step="10" placeholder="60">
              <label class="secondary--text" for="ptime"> Seconds per turn</label>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-row>
                <v-col>
                  <h3 class="secondary--text">HOW MANY PLAYERS?</h3>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox
                    value= '2'
                    color = "secondary"
                    v-model = "players"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">2 Players</div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox
                    value= '3'
                    color = "secondary"
                    v-model = "players"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">3 Players</div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox
                    value= '4'
                    color = "secondary"
                    v-model = "players"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">4 Players</div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn
            block
            color="secondary"
            large
            @click="joinrand"
            :disabled="!connection"
          >Join</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import store from '../../store/index'

export default {
  name: 'joinrand',
  data () {
    return {
      rules: ['Standard'],
      language: 'English',
      time: 60,
      players: ['2']
    }
  },
  computed: {
    connection () {
      return store.state.connection
    },
    gamernick () {
      return store.state.gamernick
    }
  },
  methods: {
    joinrand () {
      if (this.players.length < 1) {
        alert('You must select a least one from number of players option')
      } else if (this.rules.length < 1) {
        alert('You must select at least one rule type')
      } else {
        const gdata = { player: this.gamernick, time: this.time, rules: this.rules, noofplayers: this.players, language: this.language }
        store.dispatch('setgtype', 'player')
        this.$socket.emit('randgame', gdata)
      }
    }
  }
}
</script>
