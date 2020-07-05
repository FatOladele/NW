<template>
  <v-container class="home">
    <!-- <app-drawer></app-drawer> -->
    <v-content>
      <v-container>
        <v-row justify="center">
          <v-col
            cols="12"
            sm="8"
            md="8"
            lg="6"
            xl="6"
            justify="center"
          >
            <v-row justify="center">
              <v-avatar
                tile
                size="128"
              >
                <img alt="Vue logo" src="../assets/logo.png">
              </v-avatar>
            </v-row>
            <v-row
              align="center"
              justify="center"
            >
              <h1 class="cn-text">Nigeria Words</h1>
            </v-row>
            <div v-if = "gtype === 'jid'">
              <v-row>
                <v-col class="py-1">
                  <v-btn
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                    @click="setgtype('cg')"
                  >
                    Create Game
                  </v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="py-1">
                  <v-btn
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                    @click="setgtype('pc')"
                  >
                    Play with computer
                  </v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="py-1">
                  <JoinId></JoinId>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="py-1">
                  <v-btn
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                    @click="setgtype('jr')"
                  >
                    Join random game
                  </v-btn>
                </v-col>
              </v-row>
            </div>
            <div v-else-if="gtype === 'cg'">
              <v-row>
                <v-col>
                  <Creategame></Creategame>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn @click = "setgtype('jid')"
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                  >
                    back
                  </v-btn>
                </v-col>
              </v-row>
            </div>
            <div v-else-if="gtype === 'pc'">
              <v-row>
                <v-col>
                  <playcomp></playcomp>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn @click = "setgtype('jid')"
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                  >
                    back
                  </v-btn>
                </v-col>
              </v-row>
            </div>
            <div v-else-if="gtype === 'jr'">
              <v-row>
                <v-col>
                  <joinrand></joinrand>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn @click = "setgtype('jid')"
                    block
                    color="third"
                    large
                    id="create-btn"
                    class="secondary--text"
                  >
                    back
                  </v-btn>
                </v-col>
              </v-row>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <app-nav></app-nav>
  </v-container>
</template>

<script>
// @ is an alias to /src
import AppNav from '@/components/app/Nav'
import JoinId from '@/components/forms/JoinId'
import Creategame from '@/components/forms/Creategame'
import playcomp from '@/components/forms/playcomp'
import joinrand from '@/components/forms/joinrand'
// import AppDrawer from "@/components/app/Drawer";

export default {
  name: 'Home',
  components: {
    AppNav,
    JoinId,
    Creategame,
    playcomp,
    joinrand
  },
  data () {
    return {
      gtype: 'jid'
    }
  },
  methods: {
    setgtype (type) {
      this.gtype = type
    }
  }
}
</script>
