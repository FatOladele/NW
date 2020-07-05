<template>
  <v-card class= "d-flex flex-column flex-nowrap">
    <v-card color= brown class= "d-flex flex-nowrap" v-for= "(value, key) in boardcode.rows" :key = "key">
      <v-card v-for= "j in boardcode.columns" :key = "j" :id= "key + j" class = "boardcard" >
        <v-card v-if = 'letonboard[value - 1][j -1] !== 0' class = "cslot" elevation= "10">
          <bletter :letcode = "'L' + letonboard[value - 1][j -1]['lp']" :letcol = "colourcode[letonboard[value - 1][j -1]['pl']]"  >
              <!-- nothing -->
          </bletter>
        </v-card>
        <v-card v-else class = "cslot" elevation= "10">
          <bslot :bid ="'B' + key + j" >
          </bslot>
        </v-card>
      </v-card>
    </v-card>
  </v-card>
</template>

<script>
import bslot from './bslot.vue'
import store from '../../store/index'
import bletter from './bletter.vue'
export default {
  name: 'Board',
  components: {
    bslot,
    bletter
  },
  computed: {
    letonboard () {
      return store.getters.getboard
    }
  },
  data () {
    return {
      boardcode: {
        rows: {
          A: 1,
          B: 2,
          C: 3,
          D: 4,
          E: 5,
          F: 6,
          G: 7,
          H: 8,
          I: 9,
          J: 10,
          K: 11,
          L: 12,
          M: 13,
          N: 14,
          O: 15
        },
        columns: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
      },
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r',
        5: 'p'
      }
      // letonboard: store.getters.getboard
    }
  },
  method: {
  }
}
</script>

<style  scoped>
  table {
    table-layout: fixed ;
    width: 100% ;
    height: 100%;
    border-collapse: collapse ;
    border: 1px black solid ;
    margin-top: 2px solid black;
    margin-bottom: 2px solid black;
  }
  .board{
    height: 600px;
    width: 600px;
    background: black;
  }
  .boardcard {
    display: inline-block;
    height: 35px;
    width: 35px;
    text-align: center;
    font-size: 1rem;
    /*padding: 2px;*/
  }
  .board td bslot {
    display: inline-block;
  }
  .cslot{
    opacity: 1;
    background-color: burlywood;
    display: inline-block;
    height: 35px;
    width: 35px;
  }
  #BB6, #BB10, #BF2, #BF6, #BF10, #BF14, #BJ2, #BJ6, #BJ10, #BJ14, #BN6, #BN10 {
    background-color: purple;
    background-image: url("../../assets/pics/tl.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  #BA4, #BA12, #BC7, #BC9, #BD1, #BD8, #BD15, #BG3, #BG7, #BG9, #BG13, #BH4, #BH12, #BI3, #BI7, #BI9, #BI13, #BL1, #BL8, #BL15, #BM7, #BM9, #BO4, #BO12{
    background-color: lightskyblue;
    background-image: url("../../assets/pics/dl.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  #BA1, #BA8, #BA15, #BH1, #BH15, #BO1, #BO8, #BO15{
    background-color: orangered;
    background-image: url("../../assets/pics/tw.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  #BB2, #BC3, #BD4, #BE5, #BH8, #BK11, #BL12, #BM13, #BN14, #BB14, #BC13, #BD12, #BE11, #BK5, #BL4, #BM3, #BN2{
    background-color: orange;
    background-image: url("../../assets/pics/dw.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  #BH8 {
    background-image: url("../../assets/Alphabet/ST.png");
    background-repeat: no-repeat;
    background-size: 100% 100;
  }
</style>
