<template>
  <v-app id = "nigeriawords" :style = "{'background': $vuetify.theme.themes.light.background}">
    <v-content class = "d-inline-block">
      <v-container
        fluid
        fill-height
        pa-0
        class="align-start"
      >
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
// import AppNav from '@/components/app/Nav'
// import AppDrawer from "@/components/app/Drawer";

export default {
  name: 'App',

  components: {
    // AppNav
  },

  data: () => ({
    //
  })
}
</script>

<style>
  /* .L111{
    background-image: url("./assets/Alphabet/111.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L112{
    background-image: url("./assets/Alphabet/112.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L113{
    background-image: url("./assets/Alphabet/113.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L114{
    background-image: url("./assets/Alphabet/114.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L115{
    background-image: url("./assets/Alphabet/115.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L116{
    background-image: url("./assets/Alphabet/116.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L117{
    background-image: url("./assets/Alphabet/117.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L118{
    background-image: url("./assets/Alphabet/118.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L119{
    background-image: url("./assets/Alphabet/119.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L120{
    background-image: url("./assets/Alphabet/120.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L121{
    background-image: url("./assets/Alphabet/121.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L122{
    background-image: url("./assets/Alphabet/122.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L123{
    background-image: url("./assets/Alphabet/123.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L124{
    background-image: url("./assets/Alphabet/124.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L125{
    background-image: url("./assets/Alphabet/125.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L126{
    background-image: url("./assets/Alphabet/126.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L127{
    background-image: url("./assets/Alphabet/127.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L128{
    background-image: url("./assets/Alphabet/128.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L129{
    background-image: url("./assets/Alphabet/129.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L130{
    background-image: url("./assets/Alphabet/130.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L131{
    background-image: url("./assets/Alphabet/131.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L132{
    background-image: url("./assets/Alphabet/132.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L133{
    background-image: url("./assets/Alphabet/133.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L134{
    background-image: url("./assets/Alphabet/134.jpg");
    background-repeat: no-repeat;
  }
  .L135{
    background-image: url("./assets/Alphabet/135.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L136{
    background-image: url("./assets/Alphabet/136.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L137{
    background-image: url("./assets/Alphabet/137.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L138{
    background-image: url("./assets/Alphabet/138.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L139{
    background-image: url("./assets/Alphabet/139.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L140{
    background-image: url("./assets/Alphabet/140.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L141{
    background-image: url("./assets/Alphabet/141.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L142{
    background-image: url("./assets/Alphabet/142.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L143{
    background-image: url("./assets/Alphabet/143.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L144{
    background-image: url("./assets/Alphabet/144.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L145{
    background-image: url("./assets/Alphabet/145.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L146{
    background-image: url("./assets/Alphabet/146.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L147{
    background-image: url("./assets/Alphabet/147.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L148{
    background-image: url("./assets/Alphabet/148.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .L149{
    background-image: url("./assets/Alphabet/149.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  } */

</style>
