<script setup lang="ts">
import { Header } from "./components";
</script>

<template>
  <Header />
  <div class="mt-32">
    <router-view></router-view>
  </div>
</template>
