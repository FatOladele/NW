<template>
  <v-fade-transition appear>
    <v-form>
      <v-card>
        <v-card-text>
          <v-row>
            <v-col>
              <v-radio-group
                v-model="rules"
                label="Rules"
                color = "primary"
              >
                <template v-slot:label>
                  <h3 class="secondary--text">Rules</h3>
                </template>
                <v-row>
                  <v-col>
                    <v-radio
                    color = "secondary"
                    value="Standard"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">Standard</div>
                    </template>
                  </v-radio>
                </v-col>
                <v-col>
                  <v-radio
                    value="Custom"
                    color = "secondary"
                  >
                    <template v-slot:label>
                      <div class="secondary--text">Basic</div>
                    </template>
                  </v-radio>
                </v-col>
              </v-row>
            </v-radio-group>
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
            <input class="secondary--text" colour = "secondary" v-model.number = 'time' type="number" name="ptime" id="ptime" min = "60" max= "120" step="10" placeholder="60">
            <label class="secondary--text" for="ptime"> Seconds per turn</label>
          </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-slider
                v-model="level"
                class="align-center"
                :max="5"
                :min="1"
                color="secondary"
              >
                <template v-slot:label>
                    <div class="secondary--text">Computer Level</div>
                  </template>
              </v-slider>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn
            block
            color="secondary"
            large
            @click="startvscomp"
            :disabled="!connection"
          >Start Game</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import store from '../../store/index'

export default {
  name: 'playcomp',
  data () {
    return {
      rules: 'Standard',
      language: 'English',
      time: 60,
      level: 1
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
    startvscomp () {
      store.dispatch('setgtype', 'player')
      const data = { creator: this.gamernick, time: this.time, rules: this.rules, language: this.language }
      store.dispatch('vscomp', data)
      this.$socket.emit('vscomputer', { player: this.gamernick, time: this.time, rules: this.rules, level: this.level, language: this.language })
    }
  }
}
</script>
