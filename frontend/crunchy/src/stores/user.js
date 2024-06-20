// /store/user.js

import { defineStore } from "pinia";
import axios from 'axios'

export const useUserStore = defineStore("user-store", {
    state: () => ({
        user: null,
        username: 'Martin',
        email: '',
        password: '',
    }),
    getters: {
        getUsername(state) {
            return state.username;
        },
        getEmail(state) {
            return state.email;
        },
        getPassword(state) {
            return state.password;
        },
    },

    actions: {
        setUsername(username) {
            this.username = username;
        },
        setEmail(email) {
            this.email = email;
        },
        setPassword(password) {
            this.password = password;
        },



        async getProfile() {
            // try {
            //     const response = await axios.get('http://127.0.0.1:8000/api/users/1/');
            //     this.user = response.data;
            //     console.log(this.user);
            //   } catch (err) {
            //     this.user = [];
            //     console.error('Error cargando menues:', err);
            //     return err;
            //   }

            axios.get('http://127.0.0.1:8000/api/menues/1/', {
                auth: {
                    username: 'admin',
                    password: 'admin'
                  },
            })
                .then((res) => console.log(res.data))
                .catch((err) => console.error(err));
        },

        async signUp(email, password) {
            const res = await fetch("http://localhost:8000/api/registration", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            });
            const user = await res.json();
            console.log(res.json());
            this.user = user;
        },
        // async signIn() {
        //     var email=this.email;
        //    var password=this.password;
        //     const res = await fetch("http://localhost:8000/api/authentication/login", {
        //         method: "POST",
        //         headers: {
        //             "Content-Type": "application/json",
        //         },
        //         body: JSON.stringify({ email, password }),
        //     });
        //     const user = await res.json();
        //     this.user = user;
        //     console.log(this.user);
        // },

        async signIn2() {
            var username = this.username;
            var password = this.password;
            const response = axios.post('http://localhost:8000/api/authentication/login', {
                username: username,
                password: password
            }, {
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                }
            }).then(function (response) {
                console.log(response);
            }).catch(function (error) {
                console.log(error);
            });
            console.log(response);
        }
    },
});