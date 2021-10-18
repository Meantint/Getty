<template>
  <!-- Login about을 이름 바꿔도 됨 -->
  <div class="" id="about">
    <Navbar />
    <login-form></login-form>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import LoginForm from '@/components/Main/LoginForm.vue'

export default {
  name: 'About',
  components: {
    LoginForm,
    Navbar,
  }
}
</script>
