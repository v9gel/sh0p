<template>
  <div class="product-list">
    <div v-for="item in items" :key="item.id">
      <pr-list-item :product_id="item"></pr-list-item>
    </div>
  </div>
</template>

<script>
import ProductListItem from './ProductListItem'
export default {
  name: 'ProductList',
  data: function () {
    return {
      items: []
    }
  },
  components: {
    'pr-list-item': ProductListItem
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product-list {
    padding-top: 64px;
  }
</style>
