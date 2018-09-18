<template>
  <div class="product-list">
    <slider></slider>
    <div v-for="item in items" :key="item.id">
      <pr-list-item :product_id="item"></pr-list-item>
    </div>
  </div>
</template>

<script>
import ProductListItem from './ProductListItem'

export default {
  name: 'Home',
  data: function () {
    return {
      items: null,
      cart: [],
      flag: 0
    }
  },
  components: {
    'pr-list-item': ProductListItem
  },
  watch: {
    cart: function () {
      for (var i = this.flag - 1; i < this.cart.length; i++) {
        this.$http.get(this.$root.config.api_url + this.cart[i]).then(response => {
          this.items = this.items.concat(response.body)
          this.items = unique(this.items)
          console.log(this.items)
        }, response => {
        })
      }
    }
  },
  methods: {
    scroll (item) {
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight
        if (bottomOfWindow) {

          this.cart = this.cart.concat(this.$root.$storage.keys())
          this.cart = unique(this.cart)

          this.cart = this.cart.reverse()
          this.cart = this.cart.reverse()
          this.flag = this.cart.length
        }
      }
    }
  },
  mounted () {
    this.scroll(this.item)
  },
  created () {
    this.$http.get(this.$root.config.api_url).then(response => {
      this.items = response.body
      console.log(this.items)
    }, response => {
    })
  }
}

function unique (arr) {
  var obj = {}

  for (var i = 0; i < arr.length; i++) {
    var str = arr[i]
    obj[str] = true // запомнить строку в виде свойства объекта
  }

  return Object.keys(obj) // или собрать ключи перебором для IE8-
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product-list {
    padding-top: 64px;
  }
</style>
