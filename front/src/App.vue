<template>
  <div>
    <mt-header title="sh0p" fixed >
      <router-link to="/" slot="left" v-if="$route.path != '/'">
        <mt-button icon="back">back</mt-button>
      </router-link>
      <router-link to="/cart" slot="right">
       <mt-button class="bt-cart" ><ion-icon class="cart" name="md-cart"></ion-icon><mt-badge v-if="count" class="quanty" size="small" type="error">{{count}}</mt-badge></mt-button>
      </router-link>
    </mt-header>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      count: 0
    }
  },
  created () {
    this.count = this.$root.$storage.length()
  },
  methods: {
    updateCount () {
      this.count = this.$root.$storage.length()
    }
  }
}
</script>

<style>
  body {
    display: block;
    margin: 0px;
  }

  ion-icon.cart {
    font-size: 40px;
    width: 60px;
  }

  .quanty {
    left: 34px;
    position: absolute;
    top: 22px;
    font-size: 7px;
  }

  .bt-cart {
    border: 10px;
  }
</style>
