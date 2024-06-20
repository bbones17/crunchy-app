<script setup>
import { useUserStore } from '../../stores/user.js';
</script>
<script>
import { mapState, mapActions } from 'pinia'

export default {
    name: 'profile-comp',
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
        ...mapState(useUserStore, { username: 'getUsername' }),
        ...mapState(useUserStore, { password: 'getPassword' }),
        ...mapState(useUserStore, { email: 'getEmail' }),

    },
    methods: {
        goToMain() {
            this.$router.push('/main')
        },
        ...mapActions(useUserStore, ['setUsername']),
        ...mapActions(useUserStore, ['setEmail']),
        ...mapActions(useUserStore, ['setPassword']),
        ...mapActions(useUserStore, ['getProfile']),
    }


}
</script>

<template>
    <div id='profile-comp' class="justify-content-center  mt-5">
        <h1>Profile Template</h1>
        <button v-on:click="goToMain" class="btn btn-primary" >Volver</button>
    </div>
</template>