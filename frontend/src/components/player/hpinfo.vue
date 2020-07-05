<template>
  <v-container class=" card d-inline-flex" color ="white" flat>
    <v-container  class=" card d-inline-flex" :class = 'colourcode[id]' >
      <v-row>
        <v-col>
          <div class = "prac" :style = "{ 'background-image' : 'url('+ require('../../assets/pics/human.jpg') + ')' }">
          </div>
        </v-col>
        <v-col>
          <v-row align = "center" justify = "center">
            <v-row>
              <h4 :class = 'colourcode[id]'>{{nickn}}</h4>
            </v-row>
            <v-row v-if = "turn == id">
              <h4 v-if = "id == pid" :class = 'colourcode[id]'>Your Turn</h4>
              <h4 v-if = "id != pid" :class = 'colourcode[id]'>Thinking...</h4>
            </v-row>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
  <!-- <div :class = 'colourcode[id]'>
    <table>
      <tr>
        <td>
          <P>{{nickn}}</P>
          <P>({{id}})</P>
          <div v-if = "turn == id">
            <p v-if = "id == pid">Your Turn</p>
            <p v-if = "id != pid">Thinking...</p>
          </div>
        </td>
      </tr>
    </table>
  </div> -->
</template>

<script>
import store from '../../store/index'
export default {
  props: ['id', 'nick'],
  computed: {
    turn () {
      return store.getters.getturn
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
      pid: store.state.player.id,
      nickn: this.nick,
      imgUrl: '../../assets/pics/human.jpg'
    }
  }
}
</script>

<style scoped>
.prac{
  width: 50px;
  height: 50px;
  margin: auto;
  border-radius: 50%;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
.y .prac{
  border: 2px solid orange;
}
.y h4 {
  color: orange;
}
.b .prac{
  border: 2px solid blue;
}
.b h4 {
  color: blue
}
.g .prac{
  border: 2px solid green;
}
.g h4 {
  color: green
}
.r .prac{
  border: 2px solid red;
}
.r h4 {
  color: red
}
</style>
