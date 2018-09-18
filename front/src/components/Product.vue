<template>
  <div class="product">
    <h3>{{product.product_name}}</h3>
    <img :src="product.image_url">
    <h3>Customers who bought this item also bought</h3>
    <div v-for="item in recommended" :key="item.id">
      <pr-list-item :product_id="item"></pr-list-item>
    </div>
  </div>
</template>

<script>
import ProductListItem from './ProductListItem'
export default {
  name: 'Product',
  data () {
    return {
      product: {
        image_url: 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg',
        product_name: 'Other product'
      },
      recommended: [],
      product_id: null,
      inCart: false
    }
  },
  created () {
    console.log(this)
    this.product_id = this.$route.params.id
    this.inCart = this.$root.$storage.get(this.product_id)
    this.$http.get('https://about-623b5.firebaseio.com/sh0p/' + this.product_id + '.json').then(response => {
      this.product = response.body
      if (this.product.image_url == null) {
        this.product.image_url = 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg'
      }
    }, response => {
    })

    this.$http.get(this.$root.config.api_url + this.product_id).then(response => {
      this.recommended = response.body
      console.log(this.recommended)
    }, response => {
    })
  },
  watch: {
    '$route' (to, from) {
      console.log(this)
      this.product_id = this.$route.params.id
      this.inCart = this.$root.$storage.get(this.product_id)
      this.$http.get('https://about-623b5.firebaseio.com/sh0p/' + this.product_id + '.json').then(response => {
        this.product = response.body
        if (this.product.image_url == null) {
          this.product.image_url = 'https://pp.userapi.com/c830708/v830708826/144215/i2d-32RUG9Y.jpg'
        }
      }, response => {
      })

      this.$http.get(this.$root.config.api_url + this.product_id).then(response => {
        this.recommended = response.body
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
  },
  components: {
    'pr-list-item': ProductListItem
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product {
    padding-top: 64px;
  }
</style>
