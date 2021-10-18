<template>
  <div class="home">
    <Navbar/>
    <MainPageCenter />
    <MainPageBottom />
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import MainPageCenter from '@/components/MainPage/MainPageCenter.vue'
import MainPageBottom from '@/components/MainPage/MainPageBottom.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    MainPageCenter,
    MainPageBottom
  }
}
</script>

<style scoped>

</style>
