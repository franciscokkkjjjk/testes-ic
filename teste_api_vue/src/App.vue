<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="sidebar">
      <div class="logo">
          <img src="@/assets/logo.svg"/>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
  .sidebar {
    width: 70px;
    height: 100vh;
    background-color: var(--color-sidebar);
    display: flex;
    flex-direction: column;
  }
  .logo {
    width: 100%;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .logo > img{
    width: 40px;
  }

  @media (max-width: 425px) {
    .sidebar {
      height: 30px;
      width: 100vw;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    .logo {
      width: 40px;
      height: 100%;
    }
    .logo > img {
      width: 100%;
    }
    .links {
      flex-direction: row;
    }
    .links a {
      margin-right: 10px;
      padding: 5px 8px;
    }
  }
</style>
