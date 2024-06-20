<script setup>
import LoginComp from './components/user/LoginComp.vue';

</script>

<script>
export default {
  name: 'app',
  
  components: {
    LoginComp,
  },
  props: {

  },
  data() {
    return {

    }
  },
}

</script>



<template>
  <div id="app" class="containter-sm text-center justify-content-md-center">

    <!-- <p>
      <strong>Current route path:</strong> {{ $route.fullPath }}
    </p>
    <nav>
      <RouterLink to="/login">Login</RouterLink>
      <RouterLink to="/app">Crunchy</RouterLink>
    </nav> -->


    <div class="row" v-if="$route.fullPath === '/'">
      <LoginComp />
    </div>
    <main v-else>
      <RouterView />
    </main>

  </div>


</template>
