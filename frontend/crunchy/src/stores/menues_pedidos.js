import { defineStore } from 'pinia'

export const useMenuesPedidos = defineStore('menues-pedidos-store', {
    state: () => {
        return {
            menuesPedidos: [],
        }
    },
    getters: {
        getMenuesPedidos(state) {
            return state.menuesPedidos;
        },
    },

    actions: {
        agregarMenuPedidos(menu_pedido, cantidad) {
            let indice = this.menuesPedidos.findIndex(element => element.id === menu_pedido.id);
            //Menu encontrado
            if (indice >= 0) {
                if (cantidad >= 1) {
                    this.menuesPedidos[indice].cantidad += cantidad;

                } else {
                    this.menuesPedidos[indice].cantidad = cantidad;
                }
            } else {
                let indice_ultimo = this.menuesPedidos.length;
                //si menuesPedidos esta vacio se le asigna 0 por defecto
                this.menuesPedidos.push({ numero_pedido: indice_ultimo, cantidad: cantidad, ...menu_pedido })
            }
            console.log('Menues cargado: ', menu_pedido.nombre);
        },

        eliminarMenuPedido(menu_eliminar) {
            let indice = this.menuesPedidos.findIndex(element => element.id === menu_eliminar.id);
            //Menu encontrado
            if (indice >= 0) {
                this.menuesPedidos.splice(indice, 1);
                console.log('Menu eliminado: ', menu_eliminar.nombre);
            } else {
                console.log('Menu inexistente', menu_eliminar.nombre);
            }
        },
        editarCantidadMenuPedido(menu_editar, cantidad) {
            let indice = this.menuesPedidos.findIndex(element => element.id === menu_editar.id);
            if (cantidad === 0) {
                this.eliminarMenuPedido(menu_editar);
                return;
            }
            //Menu encontrado
            if (indice >= 0) {
                this.menuesPedidos[indice].cantidad = cantidad;
                console.log('Menu cantidad editada: %s %s', menu_editar.nombre, cantidad);
            } else {
                console.log('Menu inexistente', menu_editar.nombre);
            }
        },

        getMenuesPedidosAction() {
            return this.menuesPedidos;
        },

        reiniciarMenuesPedidos() {
            this.menuesPedidos = [];
        }
    },
})