<template>
  <div class="product-list">
    <div  v-if="items.length != 0">
      <h3>You cart</h3>
      <div v-for="item in items" :key="item.id">
        <pr-list-item :product_id="item"></pr-list-item>
      </div>
      <h3>Customers who bought items in your cart also bought</h3>
      <div v-for="item in recommended" :key="item.id">
        <pr-list-item :product_id="item"></pr-list-item>
      </div>
    </div>
    <mt-cell title="Your cart is empty :(" v-if="items.length === 0"></mt-cell>
  </div>
</template>

<script>
import ProductListItem from './ProductListItem'
export default {
  name: 'Cart',
  data: function () {
    return {
      items: null,
      recommended: null
    }
  },
  watch: {
    items: function () {
      this.$http.get(this.$root.config.api_url + this.items.toString()).then(response => {
        this.recommended = response.body
        console.log(this.recommended)
      }, response => {
      })
    }
  },
  components: {
    'pr-list-item': ProductListItem
  },
  created () {
    this.items = this.$root.$storage.keys()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product-list {
    padding-top: 64px;
  }
</style>
