<script setup>
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';
</script>
<script>
import { mapState, /*mapActions*/ } from 'pinia'

export default {
  name: 'sidebar-comp',
  data() {
    return {
    }
  },
  computed: {
    ...mapState(useMenuesPedidos, { menuesPedidos: 'getMenuesPedidos' }),
  },
  methods: {
    goToOrder() {
      this.$router.push('/cart')
    },
  },

}
</script>

<template>
  <div id="sidebar-comp">
    <div class="row mt-3 justify-content-center">
      <h4>Pedido</h4>
      <ul class="list-group" v-for="item in menuesPedidos" :key="item.id">
        <li class="list-group-item text-start m-2 p-2">
          {{ item.cantidad + " x " + item.nombre }}

        </li>
      </ul>
    </div>
    <div class="row mt-3 justify-content-center">
      <button type="button" class="btn btn-primary w-50 mb-5 " v-on:click="goToOrder">Finalizar</button>
    </div>
  </div>
</template>