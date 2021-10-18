<template>
  <div>
    <BankerNavbar />
    <br>
    <LoanCheck />
  </div>
</template>

<script>
import LoanCheck from '@/components/Banker/LoanCheck.vue'
// import Navbar from '@/components/MainPage/Navbar.vue'
import BankerNavbar from '@/components/Banker/BankerNavbar.vue'

export default {
  name: 'BankerLoan',
  components: {
    LoanCheck,
    BankerNavbar,
  }
}
</script>
