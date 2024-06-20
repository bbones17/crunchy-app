<script setup>
import HeaderComp from '../common/HeaderComp.vue';
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';

</script>

<script>
import { mapWritableState, mapActions } from 'pinia'
export default {
    name: 'pay-comp',
    props: {
    },
    data() {
        return {
            qr: "",
        }
    },
    computed: {
    },
    methods: {
        ...mapActions(useMenuesPedidos, ['reiniciarMenuesPedidos']),
        goToMain() {
            
            this.$router.push('/main')
        },
    },
    mounted(){
        this.reiniciarMenuesPedidos();
    }
}
</script>

<template>
    <div id="pay-comp">
        <HeaderComp></HeaderComp>
        <div class="row mt-5">
            <h1>¡Gracias por elegirnos!</h1>

        </div>

        <div class="row mt-5">
            <p>[QR]</p>
            <h3>Su comprobante de pedido ha sido generado</h3>
            <p>Para retirar su pedido dirijase a nuestro local hasta antes de las 15hs.</p>

        </div>

        <br>
        <button v-on:click="goToMain" class="btn btn-primary">Realizar otro pedido</button>
    </div>
</template>