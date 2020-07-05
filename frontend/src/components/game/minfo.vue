<template>
  <v-container>
    <v-row>
      <v-col>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    activities () {
      return store.getters.actgetters
    }
  }
}
</script>