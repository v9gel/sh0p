<template>
  <div>
      <mt-cell class="pli" :title="'   ' + product.product_name">
        <img class="product-image" slot="icon" :src="product.image_url" width="64" height="64">
        <mt-button class="pli-button" size="small" type="primary" v-on:click="addToCart" v-if="!inCart">Add to Cart</mt-button>
        <mt-button class="pli-button" size="small" type="danger" v-on:click="removeFromCart" v-if="inCart">Remove</mt-button>
        &nbsp;
        <router-link :to="'/product/' + product_id">
          <mt-button class="pli-button" size="small" type="default">More</mt-button>
        </router-link>
      </mt-cell>
  </div>
</template>

<script>
export default {
  name: 'ProductListItem',
  data () {
    return {
      product: {
        image_url: 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg',
        product_name: 'Other product'
      },
      inCart: false
    }
  },
  props: ['product_id'],
  created () {
    this.inCart = this.$root.$storage.get(this.product_id)
    this.$http.get('https://about-623b5.firebaseio.com/sh0p/' + this.product_id + '.json').then(response => {
      this.product = response.body
      if (this.product.image_url == null) {
        this.product.image_url = 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg'
      }
    }, response => {
    })
  },
  watch: {
    product_id: function () {
      this.inCart = this.$root.$storage.get(this.product_id)
      this.$http.get('https://about-623b5.firebaseio.com/sh0p/' + this.product_id + '.json').then(response => {
        this.product = response.body
        if (this.product.image_url == null) {
          this.product.image_url = 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg'
        }
      }, response => {
      })
    }
  },
  methods: {
    addToCart () {
      this.inCart = true
      this.$root.$storage.set(this.product_id, true)
      this.$root.$children[0].updateCount()
    },
    removeFromCart () {
      this.inCart = false
      this.$root.$storage.remove(this.product_id)
      this.$root.$children[0].updateCount()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product-image {
    margin: 4px;
  }

  .pli {
    z-index: 5;
  }
  .pli-button {
    z-index: 6;
  }
</style>
