<script setup>
import SideBarComp from "./SideBarComp.vue";
import HeaderComp from "../common/HeaderComp.vue";
import OrderModalComp from "./OrderModalComp.vue"
import { useMenues } from '../../stores/menues.js';
import { useMenuesPedidos } from '../../stores/menues_pedidos.js';

</script>

<script>
import { mapState, mapActions } from 'pinia'

export default {
  name: 'menu-comp',
  components: {
    SideBarComp,
    HeaderComp,
  },
  data() {
    return {
      active_sidebar: false,
      active_modal: false,
      menu_activo_modal: {},
      cantidad_modal_activo: 0,

      menu_buscado: "",
      checked_tags: [],

    }
  },

  computed: {
    menuesFiltrados() {
      let menues_filtrados = [];
      //Ambos activos
      if (this.checked_tags.length != 0 && this.menu_buscado != "") {
        let menues_etiquetas = this.menues.filter((menu) => this.checked_tags.includes(menu['etiqueta']));
        let menues_buscados = menues_etiquetas.filter((menu) => menu['nombre'].toLowerCase().includes(this.menu_buscado.toLowerCase()));
        menues_filtrados.push(menues_buscados);
        return menues_filtrados.pop();
      }  //Ninguno de los 2 
      else if (this.checked_tags.length === 0 && this.menu_buscado === "") {
        return this.menues;
      }

      //Uno u otro
      if (this.checked_tags.length != 0) {
        menues_filtrados.push(this.menues.filter((menu) => this.checked_tags.includes(menu['etiqueta'])));
        return menues_filtrados.pop();
      }
      //Busqueda
      menues_filtrados.push(this.menues.filter((menu) => menu['nombre'].toLowerCase().includes(this.menu_buscado.toLowerCase())));
      return menues_filtrados.pop();
    },

    //Store props
    ...mapState(useMenues, { menues: 'getMenues' }),
    ...mapState(useMenuesPedidos, { menuesPedidos: 'getMenuesPedidos' }),
  },

  methods: {
    mostrarOcultarCarrito() {
      this.active_sidebar = !this.active_sidebar;
    },

    mostrarModalMenu(menu) {
      this.active_modal = true;
      this.active_sidebar = true;
      this.menu_activo_modal = menu;
    },
    //Store methods Menues
    ...mapActions(useMenues, ['cargarMenues']),
  },
  created() {
    this.cargarMenues();
    console.log("Menues cargados");
  },
}
</script>

<template>
  <div id="menu-comp">

    <!-- Modal -->
    <Teleport to="body">
      <OrderModalComp :show="active_modal" @close="active_modal = false" 
      :menu_activo_modal="menu_activo_modal">
        <!-- <template #body>
        </template> -->
      </OrderModalComp>
    </Teleport>



    <div class="row ">
      <div class="col-md ">
        <HeaderComp @mostrarOcultarCarrito="mostrarOcultarCarrito" />
      </div>
    </div>



    <nav class="navbar bg-body-tertiary">
      <div class="row container-fluid">
        <div class="col d-flex">
          <div class="btn-group justify-content-start" role="group" aria-label="Basic checkbox toggle button group">
            <input v-model="checked_tags" value="Vegetariano" type="checkbox" class="btn-check" id="btncheck1"
              autocomplete="off">
            <label class="btn btn-outline-primary" for="btncheck1">Vegetariano</label>

            <input v-model="checked_tags" value="Celiaco" type="checkbox" class="btn-check" id="btncheck2"
              autocomplete="off">
            <label class="btn btn-outline-primary" for="btncheck2">Celiaco</label>

            <input v-model="checked_tags" value="Vegano" type="checkbox" class="btn-check" id="btncheck3"
              autocomplete="off">
            <label class="btn btn-outline-primary" for="btncheck3">Vegano</label>
          </div>

        </div>
        <div class="col">
          <input v-model="menu_buscado" class="form-control " type="search" placeholder="Buscar" aria-label="Search">
        </div>
      </div>
    </nav>

    <div class="row me-3 ms-3">
      <div class="col">
        <div class="row m-3">
          <h4 v-if="menuesFiltrados.length === 0">No se encontraron resultados</h4>
          <!-- este div col indica la cantidad de elementos por fila 4 ( margen 3 x 4)=12 
            | si necesito 3 por fila entonces md-4 -->
          <div class="col-md-3" v-for="menu in menuesFiltrados" v-bind:key="menu.id">

            <div class="card h-100">
              <img v-bind:src="'src/assets/' + menu.imagen" class="card-img-top h-50" v-bind:alt=menu.nombre>
              <div class="card-body">
                <h5 class="card-title">{{ menu.nombre }}</h5>
                <p class="card-text">{{ menu.etiqueta }} </p>
                <button href="#" class="btn btn-primary" v-on:click="mostrarModalMenu(menu)">Agregar</button>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div class="col-2 bg-secondary-subtle" v-if="active_sidebar">

        <h4 v-if="menuesPedidos.length === 0" class="mt-5">No se registraron pedidos</h4>
        <SideBarComp v-bind:menuesPedidos="menuesPedidos" v-else />

      </div>

    </div>
  </div>
</template>
