<template>
    <div id="first" class="row align-items-center wrapper">
        <div class="mx-auto col-md-4">
            <div class="myform form">
                <div class="logo mb-3 text-center">
                    <h3>로그인</h3>
                </div>
                    <div class="form-group">
                        <div class="d-flex justify-content-between">
                            <label for="id">아이디</label>
                        </div>
                        <input type="id" name="id" v-validate="'required'" v-model="credential.user_id" data-vv-as="ID"
                        class="form-control" :class="{error: errors.has('id')}"  id="id" aria-describedby="IdHelp" placeholder="Enter ID">
                        <span class="text-left error" v-if="errors.has('id')">{{errors.first('id')}}</span>
                    </div>
                    <div class="form-group">
                        <div class="d-flex justify-content-between">
                            <label for="id">비밀번호</label>
                        </div>
                        <input type="password" ref="password" name="password" v-validate="'required|min:4'" v-model="credential.user_pw" data-vv-as="Password"
                        class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="Enter Password">
                        <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
                    </div>
                    <div class="text-center">
                        <button type="submit" @click="loginCheck" class="btn btn-block mybtn btn-primary tx-tfm">Login</button>
                    </div>
                    <div class="links">
                        <div class="member text-center mt-3">
                            <router-link  :to="{ name: 'SignupMerge' }">
                                <a id="goSignup">  회원가입</a>
                            </router-link>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue'
//import VueRouter from 'vue-router'

import * as VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'
import axios from 'axios';

ko.messages.required = (field) => `${field} 이/가 필요합니다.`
ko.messages.password = (field) => `${field} 는 최소 4글자 여야합니다.`

const config = {
    locale: 'ko',
    dictionary: {
        ko
    }
}

Vue.use(VeeValidate, config)

export default {
    name: 'Login',
    data: function () {
        return {
            credential: {
                user_id: '',
                user_pw: '',
            }
        }
    },
    methods: {
        getJWT: function () {
            axios({
                method: 'post',
                url: `http://j5a205.p.ssafy.io:3000/signin`,
                data: this.credential
            }).then((res) => {
                var token = res.data.Authorization;
                localStorage.setItem('Token', token);
                if (localStorage.getItem('Token')) {
                  axios({
                    method: 'get',
                    url: `http://j5a205.p.ssafy.io:3000/user/info`,
                    headers:{
                      "token" : localStorage.getItem("Token")
                    }
                  }).then((user) => {
                    // console.log(1111,user.data.user)
                    alert(`${user.data.user.user_name} 님 반갑습니다!`);
                    this.$router.push({ name: 'Home'})
                  }).catch((err) => {
                    console.log(err);
                  });
                }
            }).catch((err) => {
                alert("탈퇴한 회원이거나 아이디 혹은 비밀번호가 일치하지 않습니다.")
                console.log(err.headers)
            })
        },
        loginCheck(){
            if(this.onSubmit()){
                this.getJWT();
            }else{
                alert("입력을 확인해주세요")
            }
        },
        onSubmit() {
            this.$validator.validateAll()
            if (!this.errors.any()) {
                return true
            }
            return false
        }
    }
}
</script>

<style>
.wrapper {
    display: grid;
    place-items: center;
    min-height: 75vh;
}
</style>
