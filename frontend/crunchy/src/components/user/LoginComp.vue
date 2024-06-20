<script setup>
import { useUserStore } from '../../stores/user.js';
</script>
<script>
import { mapActions } from 'pinia'

export default {
  name: 'login-comp',
  props: {
  },
  data() {
    return {
      usernameTemp: '',
      passwordTemp: '',
      emailTemp: '',

    }
  },
  computed: {

  },
  methods: {

    async login() {
      this.goToMain();
    },
    register() {
      this.goToMain();
    },
    goToMain() {
      this.$router.push('/main')
    },
    ...mapActions(useUserStore, ['signIn2']),
    ...mapActions(useUserStore, ['getProfile']),
    ...mapActions(useUserStore, ['setUsername']),
    ...mapActions(useUserStore, ['setPassword']),
  }


}
</script>

<template>
  <div id='login-comp' class="justify-content-center  mt-5">
    <div style="height: 75px;"></div>
    <section>
      <div class="container-fluid h-custom">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-md-9 col-lg-6 col-xl-5">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
              class="img-fluid" alt="Sample image">
          </div>
          <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
            <form>
              <h1>Iniciar Sesión</h1>

              <!-- Username input -->
              <div class="form-outline mt-3 mb-4">
                <label class="form-label" for="form3Example3">Nombre de usuario</label>
                <input v-model="usernameTemp" type="text" id="form3Example3" class="form-control form-control-lg"
                  placeholder="Ingresar nombre de usuario" />
              </div>

              <!-- Password input -->
              <div class="form-outline mb-3">
                <label class="form-label" for="form3Example4">Contraseña</label>
                <input v-model="passwordTemp" type="password" id="form3Example4" class="form-control form-control-lg"
                  placeholder="Ingrese una contraseña" />

              </div>

              <div class="d-flex justify-content-start align-items-center">
                <a href="#!" class="text-body">Olvide mi contraseña</a>
              </div>

              <div class="text-center text-lg-start mt-4 pt-2 ">
                <button v-on:click="login()" type="button" class="btn btn-primary btn-lg m-3">Login</button>

                <button v-on:click="register()" type="button" class="btn btn-danger btn-lg m-3">Registrar</button>

              </div>

            </form>
          </div>
        </div>
      </div>

    </section>
  </div>
</template>
