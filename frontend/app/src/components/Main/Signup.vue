<template>
  <!-- signup box start -->
  <div class="text-center row align-items-center" id="signUpCSS">
    <div class="myform form col-md-4 mx-auto">
      <div class="logo mb-3">
        <div class="col-md-12 text-center mt-1">
          <h3>회원가입</h3>
        </div>
      </div>
      <form
        @submit.prevent="onSubmit"
        name="registration"
      >
        <div class="text-left form-group justify-content-between">
          <label for="user_name">이름</label>
          <input type="text"  name="user_name" v-model="userinfo.user_name"
          class="form-control" id="user_name" aria-describedby="nameHelp" placeholder="Enter Username">
          <span class="error" v-if="errors.has('user_name')">{{errors.first('user_name')}}</span>
        </div>
        <div class="form-group">
          <div class="d-flex justify-content-between">
            <label for="user_id">아이디</label>
          </div>
          <input type="id" name="user_id" v-validate="'required'" v-model="userinfo.user_id" data-vv-as="ID"
          class="form-control" :class="{error: errors.has('user_id')}"  id="id" aria-describedby="UserIdHelp" placeholder="Enter ID">
          <span class="error" v-if="errors.has('user_id')">{{errors.first('user_id')}}</span>
        </div>


        <!-- 생년월일 -->
        <div class="col-md-12"></div>
          <div class="form-group mb-3">
            <div class="text-left justify-content-between">
              <label for="exampleInputBirthday">출생연도</label>
              <div class="row_fluid">
                <div class="float-left">
                  <span class="">
                    <select
                    id="yy"
                    class="form-control float-left"
                    v-model="userinfo.year"
                    @focus="checkFlag = false"
                    >
                      <option value="">년도</option>
                      <option
                      v-for="(yy, index) in yyyyList"
                      :key="index"
                      :value="yy.value"
                      >
                      {{ yy.text }}
                      </option>
                    </select>
                  </span>
                </div>
                <div class="float-left mr-3 ml-3">
                  <span class="form-select">
                    <select
                    id="mm"
                    class="form-control"
                    v-model="userinfo.month"
                    @focus="checkFlag = false"
                    >
                      <option value="">월</option>
                      <option
                      v-for="(mm, index) in mmlist"
                      :key="index"
                      :value="mm.value"
                      >
                      {{ mm.text }}
                      </option>
                    </select>
                  </span>
                </div>
                <div class="float-left mr-3">
                  <span class="form-select">
                    <select
                    id="dd"
                    class="form-control"
                    v-model="userinfo.day"
                    @focus="checkFlag = false"
                    >
                      <option value="">일</option>
                      <option
                      v-for="(dd, idx) in ddlist"
                      :key="idx"
                      :value="dd.value"
                      >
                        {{ dd.text }}
                      </option>
                    </select>
                  </span>
                </div>
              </div>
            </div>
          </div>
          <br>
          <br>
          <div class="form-group text-left">
            <label class="mr-5" for="sex">성별</label>
            <label class="radio is-inline" v-for="sex in sexs" :key="sex">
              <input type="radio" :value="sex.value" class="radio-input" v-validate="'required'" data-vv-as="성별" v-model="userinfo.sex" name="sex">
              <span class="radio-label mr-3"> {{ sex.text }} </span>
            </label>
            <br>
            <span class="error" v-if="errors.has('sex')">{{errors.first('sex')}}</span>
          </div>
        <div class="form-group text-left">
          <label for="phone">전화번호</label>
          <input type="tel" name="phone" v-validate="'required|digits:11'" v-model="userinfo.phone_number" data-vv-as="전화번호"
          class="form-control" :class="{error: errors.has('phone')}" id="phone" aria-describedby="phoneHelp" placeholder="01012345678">
          <span class="error" v-if="errors.has('phoneNumber')">{{errors.first('phoneNumber')}}</span>
        </div>

        <div class="form-group text-left">
          <label for="job">직업</label>
          <input type="text" name="job" v-model="userinfo.job" data-vv-as="직업" v-validate="'required'"
          class="form-control" :class="{error: errors.has('salary')}" id="job" aria-describedby="jobHelp" placeholder="무직">
          <span class="error" v-if="errors.has('job')">{{errors.first('job')}}</span>
        </div>

        <div class="form-group text-left">
          <label for="salary">연봉(단위 : 만 원)</label>
          <input type="digit" name="salary" v-model="userinfo.salary" data-vv-as="연봉" v-validate="'required'"
          class="form-control" :class="{error: errors.has('salary')}" id="salary" aria-describedby="salaryHelp" placeholder="ex) 4500(만원)">
          <span class="error" v-if="errors.has('salary')">{{errors.first('salary')}}</span>
        </div>
        <div class="form-group text-left">
          <label for="password">Password</label>
          <input type="password" ref="password" name="password" v-validate="'required|min:4'" v-model="userinfo.user_pw" data-vv-as="Password"
          class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="Enter Password">
          <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
        </div>
        <div class="form-group text-left">
          <label for="passwordConfirmation">Password Confirmation</label>
          <input type="password" name="passwordConfirmation" v-validate="'confirmed:password'" v-model="userinfo.passwordConfirmation" data-vv-as="Password Confirmation"
          class="form-control" :class="{error: errors.has('passwordConfirmation')}"  id="passwordConfirmation" aria-describedby="passwordConfirmationHelp" placeholder="Enter Password One More">
          <span class="error" v-if="errors.has('passwordConfirmation')">{{errors.first('passwordConfirmation')}}</span>
        </div>
        <div class="text-center mb-3">
          <button type="submit" @click="signupCheck" class=" btn btn-block mybtn btn-primary tx-tfm">회원가입</button>
        </div>
        <div class="col-md-12 ">
          <div class="form-group">
            <p class="text-center"><router-link  :to="{ name: 'About' }"><a>로그인</a> </router-link> </p>
          </div>
        </div>
      </form>
    </div>
  </div>
  <!-- signup box end -->
</template>

<script>
import Vue from 'vue'
import axios from 'axios'

import VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'

ko.messages.required = (field) => `${field} 이/가 필요합니다.`

ko.messages.password = (field) => `${field}는 최소 4글자 여야합니다.`
ko.messages.passwordConfirmation = (field) => `${field}는 최소 4글자 여야합니다.`


const config = {
  locale: 'ko',
  dictionary: {
    ko
  }
}

Vue.use(VeeValidate, config)

export default {
  name: 'Signup',

  data: function () {
    return {
      sexs: [
        {
          value:0,
          text:"남성"
        },
        {
          value:1,
          text:"여성"
        }
      ],
      userinfo:{
        user_name:'',
        user_id:'',
        birth:'',
        year: "",
        month: "",
        day: "",
        sex:'',
        job:'',
        salary:'',
        phone_number:'',
        user_pw:'',
        passwordConfirmation: null
      },
      sendData:{
        user_name:'',
        user_id:'',
        birth:'',
        sex:'',
        salary:'',
        job:'무직',
        phone_number:'',
        user_pw:'',
      },
      yyyyList: [],
      mmlist: [],
      ddlist: [],
    };
  },
  created() {
    const nowYear = new Date().getFullYear();
    for (let i = 0; i <= 100; i++) {
      let date = nowYear - i;
      this.yyyyList.push({ value: date, text: date });
    }
    for (let i = 1; i < 13; i++) {
      if(i > 9){
        this.mmlist.push({
          value: i,
          text: i,
        });
      }else{
        this.mmlist.push({
          value: '0' + i,
          text: '0' + i,
        });
      }
    }
    for(let i = 1; i < 32; i++){
      if(i > 9){
        this.ddlist.push({
          value:i,
          text:i
        })
      }else{
        this.ddlist.push({
          value:'0' + i,
          text: '0' + i
        })
      }
    }
  },
  methods: {
    onSubmit() {
      this.$validator.validateAll()
      if (!this.errors.any()) {
          return true
      }
      return false
    },
    signupCheck() {
      var sumDate = this.userinfo.year
      sumDate = String(sumDate) + String(this.userinfo.month) + String(this.userinfo.day)
      this.userinfo.birth = sumDate

      this.sendData.user_name = this.userinfo.user_name
      this.sendData.user_id = this.userinfo.user_id
      this.sendData.user_pw = this.userinfo.user_pw
      this.sendData.birth = this.userinfo.birth
      this.sendData.sex = this.userinfo.sex
      this.sendData.job = this.userinfo.job
      this.sendData.salary = this.userinfo.salary
      this.sendData.phone_number = this.userinfo.phone_number
      if (this.onSubmit()) {
        if (this.userinfo.passwordConfirmation) {
          axios({
            method: 'post',
            url: `http://j5a205.p.ssafy.io:3000/signup`,
            data: this.sendData
          }).then((res) => {
            //console.log(res)
            res
            alert('회원가입이 완료되었습니다~!')
            //this.login()
            this.$router.push('/about')
          }).catch((err) =>{
            alert(err)
          })
        }else {
          alert('비밀번호 확인하여주세요!')
        }
      }
    }
  }
}

</script>

<style scoped>
#signUpCSS{
  @import url('https://unpkg.com/semantic-ui-css@2.2.9/semantic.css');
}

.signUpCSS{
  @import url('https://unpkg.com/semantic-ui-css@2.2.9/semantic.css');
}

</style>