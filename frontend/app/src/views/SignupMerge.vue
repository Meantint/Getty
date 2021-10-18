<template>
  <div class="" >
    <Navbar />
    <Signup class="mt-5" />
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import Signup from '@/components/Main/Signup.vue'

export default {
  name: 'SignupMerge',
  components: {
    Signup,
    Navbar,
  }
}
</script>
