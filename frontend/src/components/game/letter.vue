<template>
  <div :id= lid :class="[letcode, 'letter']" :draggable="draggable" @dragstart="dragStart" @mousedown="aboutdrag" @dragover.stop @dragend.prevent="check" @click.stop @click.prevent = "selected" :style = "{ 'background-image' : 'url('+ require('../../assets/Alphabet/' + language +'/' + letcode.slice(1) + '.jpg') + ')' }">
    <v-card>
      <slot/>
    </v-card>
  </div>
</template>

<script>
import store from '../../store/index'
export default {
  props: ['lid', 'draggable', 'letcode'],
  computed: {
    language () {
      return store.getters.getlanguage
    }
  },
  data () {
    return {
      initialpos: 'a'
    }
  },
  methods: {
    dragStart: e => {
      const target = e.target
      e.dataTransfer.setData('letterID', target.id)
      setTimeout(() => {
        target.style.display = 'none'
      }, 0)
      const letter = e.target.classList
      var lclass = letter.toString().substring(1)
      lclass = parseInt(lclass)
      if (lclass > 199) {
        e.target.classList = 'L200 letter'
      }
    },
    aboutdrag: e => {
      let parent = e.target.parentElement.id
      if (self.initialpos !== '') {
        if (parent[0] === 'l') {
          parent = e.target.parentElement.parentElement.id
          self.initialpos = parent
        } else {
          self.initialpos = parent
        }
      }
    },
    selected: e => {
      const target = e.target
      let parent = e.target.parentElement.id
      if (parent[0] === 'l') {
        parent = e.target.parentElement.parentElement.id
      }
      store.dispatch('selectedtile', { cid: target.id, pid: parent })
    },
    check: e => {
      const parent = e.target.parentElement.id
      if (parent === self.initialpos) {
        // const slot = document.getElementById(self.initialpos)
        // slot.appendChild(e.target)
        e.target.style.display = 'inline-block'
      } else {
        const slotId = self.initialpos
        var slot = slotId.toString()
        if (slot[0] === 'B') {
          slot = slot.substring(1)
          store.dispatch('removetilea', slot)
        } else if (slot[1] === 's') {
          const letter = e.target.classList
          var lclass = letter.toString().substring(1)
          store.dispatch('removeswaptile', lclass)
        }
      }
    }
  }
}
</script>

<style scoped>
  .letter{
    min-width: 25px;
    min-height: 25px;
    width: 100%;
    height: 100%;
    padding: 0;
    margin: auto;
    border: 3px;
    /* background-color: green; */
    cursor: pointer;
    display : inline-block;
    background-size: 100% 100%;
    background-repeat: no-repeat;
  }
  .selected {
    border: 3px solid black;
  }
  /* .L119{
    background-image: url("../../assets/Alphabet/119.jpg");
    background-repeat: no-repeat;
  }
  .L200{
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
    background-size: 100% 100%;
  }
  .L213{
    background-image: url("../../assets/Alphabet/213.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L214{
    background-image: url("../../assets/Alphabet/214.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L215{
    background-image: url("../../assets/Alphabet/215.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
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
