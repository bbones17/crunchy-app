import { defineStore } from 'pinia'
import axios from 'axios'

export const useMenues = defineStore('menues-store', {
  state: () => {
    return {
      menues: [],
      cargando: false
    }
  },

  getters: {
    getMenues(state) {
      return state.menues;
    },

    estaCargando(state) {
      return state.fetching;
    }
  },

  actions: {
    async cargarMenues() {
      this.cargando = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/menues/');
        this.menues = response.data;
        console.log(this.menues);
      } catch (err) {
        this.menues = [];
        console.error('Error cargando menues:', err);
        return err;
      }
      this.cargando = false;
    },
  }
})