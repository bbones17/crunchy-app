<script setup>
import { BIconCart4, BIconPersonLinesFill, BIconXLg } from 'bootstrap-icons-vue';
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';

</script>

<script>
import { mapState, /*mapActions*/ } from 'pinia'
export default {
  name: 'header-comp',
  data() {
    return {
      active: false,
      username: "Martin",

    }
  }, computed: {
    ...mapState(useMenuesPedidos, { menuesPedidos: 'getMenuesPedidos' }),
  
    cant_pedidos() {
      return this.menuesPedidos.length;
    },

  },
  methods: {
    goToProfile(){
      this.$router.push('/profile')

    },
    goToLogout(){
      this.$router.push('/')
    },

    activateDesactivate() {
      this.active = !this.active;
    },
  }
}
</script>

<template>
  <div id="header-comp">

    <div class="row m-3">
      <div class="col d-flex justify-content-end">
        <button v-on:click="$emit('mostrarOcultarCarrito')" class="btn btn-outline-primary  me-3 h-100">
          <BIconCart4 /> {{ cant_pedidos }}
        </button>

        <button v-on:click="activateDesactivate"  v-bind:class="{'btn btn-outline-primary me-3':!active,'btn btn-primary me-3':active}" type="button">
          <BIconPersonFill /> {{ username }}
        </button>

        <div v-if="active" class=" d-block">
          <button v-on:click="goToProfile" class="btn btn-outline-primary me-1" type="button">
            <BIconPersonLinesFill/> Profile
          </button>
          <button v-on:click="goToLogout" class="btn btn-outline-primary" type="button">
            <BIconXLg  /> Logout
          </button>

        </div>
      </div>




    </div>





    <!-- <router-link to="/">Login</router-link>
 <router-link to="/register/">Registrar</router-link>
 <router-link to="/main">App</router-link>
  <router-link to="/cart">Cart</router-link> -->


  </div>
</template>