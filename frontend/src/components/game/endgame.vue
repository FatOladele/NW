<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <h1> GAME HAS ENDED </h1>
      </header>
      <section class="modal-body">
        <div v-for='i in enddata.length' :key ='i'>{{enddata[i-1]}}</div>
        <v-btn
          replace
          to="/"
          @click.prevent = "closegame"
        ><span>Close game</span>
      <v-icon medium>mdi-home</v-icon></v-btn>
      </section>
    </div>
  </div>
</template>

<script>
import store from '../../store/index'
export default {
  name: 'endgame',
  computed: {
    enddata () {
      return store.getters.getenddata
    }
  },
  data () {
    return {
    }
  },
  methods: {
    closegame () {
      store.dispatch('setDefaultState')
    }
  }
}
</script>

<style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }
  td {
    width: 32px;
    height: 32px;
    border: 3px solid black
  }
</style>
