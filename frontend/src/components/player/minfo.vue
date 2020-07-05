<template>
  <v-card>
    <v-container :class = 'col'>
      <v-row class = "ma-0 pa-0 align-center justify-center ">
        <v-col class = "ma-0 pa-0 align-center justify-center ">
          <v-badge color = "black" v-if = "turn == id">
            <div class = "prac" :style = "{ 'background-image' : 'url('+ require('../../assets/pics/human.jpg') + ')' }">
          </div>
          </v-badge>
          <div v-else class = "prac" :style = "{ 'background-image' : 'url('+ require('../../assets/pics/human.jpg') + ')' }">
          </div>
        </v-col>
      </v-row>
      <v-row class = "ma-0 pa-0 align-center justify-center ">
        <v-col class = "ma-0 pa-0 align-center justify-center ">
          <span :class = 'col'>{{nick}}</span>
        </v-col>
      </v-row>
      <v-row class = "ma-0 pa-0 align-center justify-center ">
        <v-col class = "ma-0 pa-0 align-center justify-center ">
          <span>{{score}}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import store from '../../store/index'
export default {
  props: ['id', 'nick', 'col', 'score'],
  computed: {
    turn () {
      return store.getters.getturn
    }
  }
}
</script>

<style scoped>
.prac{
  width: 30px;
  height: 30px;
  margin: auto;
  border-radius: 50%;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
.y .prac{
  border: 2px solid orange;
}
.y span {
  color: orange;
}
.b .prac{
  border: 2px solid blue;
}
.b span {
  color: blue
}
.g .prac{
  border: 2px solid green;
}
.g span {
  color: green
}
.r .prac{
  border: 2px solid red;
}
.r span {
  color: red
}
</style>
