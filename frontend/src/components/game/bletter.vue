<template>
  <v-card>
    <div :class="[letcode, letcol, 'letter']" :style = "{ 'background-image' : 'url('+ require('../../assets/Alphabet/' + language +'/' + letcode.slice(1) + '.jpg') + ')' }" >
      <slot/>
    </div>
  </v-card>
</template>

<script>
import store from '../../store/index'
export default {
  props: ['letcode', 'letcol'],
  computed: {
    language () {
      return store.getters.getlanguage
    }
  }
}
</script>

<style scoped>
  .letter{
    min-width: 35px;
    min-height: 35px;
    width: 100%;
    height: 100%;
    padding: 0;
    /* background-color: green; */
    margin: auto;
    background-size: 100% 100%;
    background-repeat: no-repeat;
  }
  .y{
    border: 3px solid orange;
  }
  .b{
    border: 3px solid blue;
  }
  .g{
    border: 3px solid green;
  }
  .r{
    border: 3px solid red;
  }
  .p{
    border: 3px solid brown;
  }
  /* .L200{
    background-image: url("../../assets/Alphabet/200.jpg");
    background-repeat: no-repeat;
  }
  .L211{
    background-image: url("../../assets/Alphabet/211.jpg");
    background-repeat: no-repeat;
  }
  .L212{
    background-image: url("../../assets/Alphabet/212.jpg");
    background-repeat: no-repeat;
  }
  .L213{
    background-image: url("../../assets/Alphabet/213.jpg");
    background-repeat: no-repeat;
  }
  .L214{
    background-image: url("../../assets/Alphabet/214.jpg");
    background-repeat: no-repeat;
  }
  .L215{
    background-image: url("../../assets/Alphabet/215.jpg");
    background-repeat: no-repeat;
  }
  .L216{
    background-image: url("../../assets/Alphabet/216.jpg");
    background-repeat: no-repeat;
  }
  .L217{
    background-image: url("../../assets/Alphabet/217.jpg");
    background-repeat: no-repeat;
  }
  .L218{
    background-image: url("../../assets/Alphabet/218.jpg");
    background-repeat: no-repeat;
  }
  .L219{
    background-image: url("../../assets/Alphabet/219.jpg");
    background-repeat: no-repeat;
  }
  .L220{
    background-image: url("../../assets/Alphabet/220.jpg");
    background-repeat: no-repeat;
  }
  .L221{
    background-image: url("../../assets/Alphabet/221.jpg");
    background-repeat: no-repeat;
  }
  .L222{
    background-image: url("../../assets/Alphabet/222.jpg");
    background-repeat: no-repeat;
  }
  .L223{
    background-image: url("../../assets/Alphabet/223.jpg");
    background-repeat: no-repeat;
  }
  .L224{
    background-image: url("../../assets/Alphabet/224.jpg");
    background-repeat: no-repeat;
  }
  .L225{
    background-image: url("../../assets/Alphabet/225.jpg");
    background-repeat: no-repeat;
  }
  .L226{
    background-image: url("../../assets/Alphabet/226.jpg");
    background-repeat: no-repeat;
  }
  .L227{
    background-image: url("../../assets/Alphabet/227.jpg");
    background-repeat: no-repeat;
  }
  .L228{
    background-image: url("../../assets/Alphabet/228.jpg");
    background-repeat: no-repeat;
  }
  .L229{
    background-image: url("../../assets/Alphabet/229.jpg");
    background-repeat: no-repeat;
  }
  .L230{
    background-image: url("../../assets/Alphabet/230.jpg");
    background-repeat: no-repeat;
  }
  .L231{
    background-image: url("../../assets/Alphabet/231.jpg");
    background-repeat: no-repeat;
  }
  .L232{
    background-image: url("../../assets/Alphabet/232.jpg");
    background-repeat: no-repeat;
  }
  .L233{
    background-image: url("../../assets/Alphabet/233.jpg");
    background-repeat: no-repeat;
  }
  .L234{
    background-image: url("../../assets/Alphabet/234.jpg");
    background-repeat: no-repeat;
  }
  .L235{
    background-image: url("../../assets/Alphabet/235.jpg");
    background-repeat: no-repeat;
  }
  .L236{
    background-image: url("../../assets/Alphabet/236.jpg");
    background-repeat: no-repeat;
  }
  .L237{
    background-image: url("../../assets/Alphabet/237.jpg");
    background-repeat: no-repeat;
  }
  .L238{
    background-image: url("../../assets/Alphabet/238.jpg");
    background-repeat: no-repeat;
  }
  .L239{
    background-image: url("../../assets/Alphabet/239.jpg");
    background-repeat: no-repeat;
  }
  .L240{
    background-image: url("../../assets/Alphabet/240.jpg");
    background-repeat: no-repeat;
  }
  .L241{
    background-image: url("../../assets/Alphabet/241.jpg");
    background-repeat: no-repeat;
  }
  .L242{
    background-image: url("../../assets/Alphabet/242.jpg");
    background-repeat: no-repeat;
  }
  .L243{
    background-image: url("../../assets/Alphabet/243.jpg");
    background-repeat: no-repeat;
  }
  .L244{
    background-image: url("../../assets/Alphabet/244.jpg");
    background-repeat: no-repeat;
  }
  .L245{
    background-image: url("../../assets/Alphabet/245.jpg");
    background-repeat: no-repeat;
  }
  .L246{
    background-image: url("../../assets/Alphabet/246.jpg");
    background-repeat: no-repeat;
  }
  .L247{
    background-image: url("../../assets/Alphabet/247.jpg");
    background-repeat: no-repeat;
  }
  .L248{
    background-image: url("../../assets/Alphabet/248.jpg");
    background-repeat: no-repeat;
  }
  .L249{
    background-image: url("../../assets/Alphabet/249.jpg");
    background-repeat: no-repeat;
  } */
</style>
