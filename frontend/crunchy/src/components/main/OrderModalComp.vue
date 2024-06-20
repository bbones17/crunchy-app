<script setup>
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';
</script>

<script>
import { mapState, mapActions } from 'pinia'

export default {
    props: {
        show: Boolean,
        menu_activo_modal: {},
    },
    data() {
        return {
            cantidad_menu_modal: 1,
            maxima_cantidad_pedidos: 15,
            minima_cantidad_pedidos: 1,
        }
    },
    computed: {
        ...mapState(useMenuesPedidos, { menuesPedidos: 'getMenuesPedidos' }),
    },
    methods: {
        ...mapActions(useMenuesPedidos, ['agregarMenuPedidos']),
        ...mapActions(useMenuesPedidos, ['eliminarMenuPedido']),
        ...mapActions(useMenuesPedidos, ['editarCantidadMenuPedido']),

        agregarMenuAlPedidoModal(menu, cantidad) {
            this.agregarMenuPedidos(menu, cantidad);
            this.cantidad_menu_modal = 1;
            this.$emit('close')
        },
    },
}
</script>

<template>
    <Transition name="modal">
        <div v-if="show" class="modal-mask">
            <div class="modal-container p-5 bg-light m-auto w-50 modal-transition ">
              <!-- Header -->
                <div class="modal-header mb-3">
                    <h2>Agregar al pedido</h2>
                </div>
                <!-- Body -->
                <div class="modal-body">
                    <div class="row">
                        <div class="col-6">
                            <div class="row">
                                <img v-bind:src="'src/assets/' + menu_activo_modal.imagen" alt="Milanesa Napolitana"
                                    class="rounded img-fluid">
                            </div>
                            <!-- <div class="row">
                                Puntuacion
                            </div> -->
                        </div>
                        <div class="col-4">
                            <div class="row mb-3">
                                <h3>Descripcion</h3>
                                <p>{{ menu_activo_modal.descripcion }}</p>
                            </div>
                            <div class="row d-flex ">
                                <h3>Cantidad </h3>
                                <div class="col input-group">
                                    <input v-model="this.cantidad_menu_modal" class="form-control" type="number"
                                        v-bind:min="minima_cantidad_pedidos" v-bind:max="maxima_cantidad_pedidos">
                                </div>

                                <div class="col">
                                    <button
                                        v-on:click="this.cantidad_menu_modal < 15 ? this.cantidad_menu_modal++ : maxima_cantidad_pedidos"
                                        class="btn btn-primary me-1">+</button>
                                    <button
                                        v-on:click="this.cantidad_menu_modal > 1 ? this.cantidad_menu_modal-- : minima_cantidad_pedidos"
                                        class="btn btn-danger me-1 ">-</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <slot name="body"></slot>
                    <!-- Footer -->
                    <div class="row mt-5">
                        <div class="col d-flex justify-content-center">
                            <button class="btn btn-primary me-5"
                                @click="agregarMenuAlPedidoModal(menu_activo_modal, cantidad_menu_modal)">Agregar</button>
                            <button class=" btn btn-danger " @click="$emit('close')">Cerrar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Transition>
</template>


<style>
.modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    transition: opacity 0.3s ease;
}

.modal-enter-from {
    opacity: 0;
}

.modal-leave-to {
    opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
}
</style>