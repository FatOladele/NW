<template>
  <div color= "secondary">
    <div class = "pwords" >
      <h2> WORDS PLAYED</h2>
      <table class = "maint">
        <tr v-for= "i in wordsplayed" :key = "'a' + i.id + i" :class = 'colourcode[i.id]' >
          <td>
            <table>
              <tr v-for= "w in i.words" :key= "'r' + w">
                <td>
                  <bletter v-if = 'w.length > 0' :letcode = "'L' + w[0]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 1' :letcode = "'L' + w[1]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 2' :letcode = "'L' + w[2]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 3' :letcode = "'L' + w[3]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 4' :letcode = "'L' + w[4]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 5' :letcode = "'L' + w[5]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 6' :letcode = "'L' + w[6]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 7' :letcode = "'L' + w[7]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
    <div>
      <div>
        <table class = "maint">
          <tr align = "center" justify = "center" v-for= "o in opponents" :key= "'tr' + o.id" :class = "colourcode[o.id]">
            <td>
              <span>
                Score: {{o.score}}
              </span>
              <span v-if= "o.id === turn" >
                Timer: {{cdt}}
              </span>
              <span v-else>
                Timer: {{o.time}}
              </span>
            </td>
            <br>
          </tr>
        </table>
      </div>
    </div>
    <div v-if="isPlayer === 'player'" align = "center" justify = "center" :class = "colourcode[player.id]">
      <span>
        Score: {{player.score}}
      </span>
      <span v-if= "player.id === turn" >
        Timer: {{cdt}}
      </span>
      <span v-else>
        Timer: {{player.time}}
      </span>
    </div>
    <div :key ='cbag' align = "center" justify = "center">
      <span> Tiles left: {{cbag}} </span>
    </div>
    <div class = "alog" align = "center" justify = "center">
      <h3>ACTIVITIES</h3>
      <table>
        <tr align = "center" justify = "center" v-for= "i in activities.length" :key = 'i' >
          <td>
            {{activities[i-1]}}
          </td>
        </tr>
      </table>
    </div>
    <!-- <div>
      <table>
        <tr>
          <td class = "tw">
          </td>
          <td>
            <h2>x3</h2>
          </td>
        </tr>
        <tr>
          <td class = "dw">
          </td>
          <td>
            <h2>x2</h2>
          </td>
        </tr>
        <tr>
          <td class = "tl">
          </td>
          <td>
            <h2>x3</h2>
          </td>
        </tr>
        <tr>
          <td class = "dl">
          </td>
          <td>
            <h2>x2</h2>
          </td>
        </tr>
      </table>
    </div> -->
  </div>
</template>

<script>
import store from '../../store/index'
import bletter from './bletter.vue'
export default {
  name: 'info',
  components: {
    bletter
  },
  computed: {
    cbag () {
      return store.getters.baggetters
    },
    activities () {
      return store.getters.actgetters
    },
    wordsplayed () {
      return store.getters.getwords
    }
  },
  data () {
    return {
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      },
      opponents: store.state.opponent,
      player: store.state.player,
      cbt: store.getters.getPtime,
      cdt: 580,
      turn: store.state.turn,
      isPlayer: store.state.gtype
    }
  }
}
</script>

<style scoped>
.pwords, .alog{
  margin: 10px;
  min-height: 320px;
  max-height: 350px;
  max-width: 200px;
  overflow-y: auto;
  overflow-x: auto;
  padding: 5px;
  background: whitesmoke
  /* background-color: azure; */
}
.alog tr{
  width: 100%;
}
h2{
  text-decoration-color: black;
  padding: 3px;
  margin: 2px;
}
h3{
  text-decoration-color: black;
  padding: 3px;
  margin: 2px;
}
.pwords tr{
  padding: 3px solid red;
  width: 100%;
}
.y{
  background-color: rgb(245, 245, 160)
}
.b{
  background-color: rgb(179, 179, 248)
}
.g{
  background-color: rgb(168, 253, 168)
}
.r{
  background-color: rgb(255, 163, 163)
}
span{
  padding: 3px;
  margin-bottom: 10px;
}
.maint{
  width: 90%;
  margin: 10px;
}
table td{
  margin: 10px;
}
div table tr{
  border: 10px;
}
.tl {
  background-color: purple;
  min-height: 35px;
  min-width: 35px;
  height: 35px;
  width: 35px;
}
.dl{
  background-color: lightskyblue;
  min-height: 35px;
  min-width: 35px;
  height: 35px;
  width: 35px;
}
.tw{
  background-color: orangered;
  min-height: 35px;
  min-width: 35px;
  height: 35px;
  width: 35px;
}
.dw{
  background-color: orange;
  min-height: 35px;
  min-width: 35px;
  height: 35px;
  width: 35px;
}
</style>
