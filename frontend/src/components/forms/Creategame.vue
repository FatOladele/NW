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
              <v-checkbox v-model="oa" color = "secondary" >
                <template v-slot:label>
                  <div class="secondary--text">Allow Observers</div>
                </template>
              </v-checkbox>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn
            block
            color="secondary"
            large
            @click="cwroom"
            :disabled="!connection"
            id="create-btn"
          >Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import store from '../../store/index'

export default {
  name: 'creategame',
  data () {
    return {
      rules: 'Standard',
      language: 'English',
      time: 60,
      oa: false
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
    cwroom () {
      const gdata = { creator: this.gamernick, time: this.time, rules: this.rules, observer: this.oa, language: this.language }
      store.dispatch('setgtype', 'player')
      this.$socket.emit('create', gdata)
    }
  }
}
</script>
