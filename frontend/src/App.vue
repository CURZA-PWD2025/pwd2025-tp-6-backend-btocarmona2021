<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
    <router-link :to="{ name: 'home' }">Home</router-link>
    <router-link :to="{ name: 'marcas' }">Marcas</router-link>
    <RouterView />
</template>

<style scoped></style>
