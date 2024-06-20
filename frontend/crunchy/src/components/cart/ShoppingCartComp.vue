<script setup>
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';
</script>

<script>
import { mapWritableState, mapActions } from 'pinia'
import HeaderComp from '../common/HeaderComp.vue';

export default {
  name: 'shopping-cart-comp',
  props: {

  },
  data() {
    return {

    }
  },
  computed: {
    ...mapWritableState(useMenuesPedidos, { menuesPedidos: 'getMenuesPedidos' }),

    total_a_pagar() {
      this.suma = 0;
      for (let i = 0; i < this.menuesPedidos.length; i++) {
        this.suma += this.menuesPedidos[i].precio * this.menuesPedidos[i].cantidad;
      }
      return this.suma;
    },
  },
  methods: {
    goToMain() {
      this.$router.push('/main')
    },
    goToPay() {
      this.$router.push('/pay')
    },

    //Store methods Menues Pedidos
    ...mapActions(useMenuesPedidos, ['eliminarMenuPedido']),
    ...mapActions(useMenuesPedidos, ['editarCantidadMenuPedido']),
  },
  mounted() {
    console.log(this.menuesPedidos);
  }
}
</script>

<template>
  
  <div id="shopping-cart-comp">
    <HeaderComp></HeaderComp>
    <section class="h-100">
      <div class="container h-100 py-5">
        <div class="row d-flex justify-content-center align-items-center h-100">

          <div class="col-10">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h3 class="fw-normal mb-0">Carrito de compras</h3>
            </div>
            <div v-if="menuesPedidos.length != 0">
              <div v-for="item in menuesPedidos" :key="item.id">
                <div class="card rounded-3 mb-4">
                  <div class="card-body p-4">
                    <div class="row d-flex justify-content-between align-items-center">
                      <div class="col-md-2 col-lg-2 col-xl-2">
                        <img v-bind:src="'src/assets/' + item.imagen" class="img-fluid rounded-3" alt="Cotton T-shirt">
                      </div>
                      <div class="col-md-3 col-lg-3 col-xl-3">
                        <p class="lead fw-normal mb-2">{{ item.nombre }}</p>
                        <p class="text-muted">{{ item.nombre }}</p>
                      </div>
                      <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
                        <p>Cantidad: {{ item.cantidad }}</p>


                      </div>
                      <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                        <h5 class="mb-0">${{ item.precio * item.cantidad }}</h5>
                      </div>
                      <div class="col">
                        <button v-on:click="editarCantidadMenuPedido(item, item.cantidad + 1)"
                          class="btn btn-primary m-1">+</button>
                        <button v-on:click="editarCantidadMenuPedido(item, item.cantidad - 1)"
                          class="btn btn-danger m-1">-</button>
                        <br>
                        <button v-on:click="eliminarMenuPedido(item)" class="btn btn-danger m-1">Eliminar</button>

                      </div>

                    </div>
                  </div>
                </div>

              </div>
            </div>
            <div v-else>
              <p class="lead fw-normal mb-2 ">No hay productos en el carrito</p>
            </div>

            <div class="card ">
              <div class="card-body">
                <p class="lead fw-normal mb-2 ">Total a pagar: ${{ total_a_pagar }}</p>
              </div>
            </div>


            <div class="">
              <div class="mt-5">
                <button v-on:click="goToPay" type="button" class="btn btn-warning btn-lg">Pagar</button>

                <button @click="goToMain" class="btn btn-primary btn-lg ms-5">Volver</button>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>




  </div>


</template>