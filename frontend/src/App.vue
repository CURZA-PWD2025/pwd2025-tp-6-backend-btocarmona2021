<script setup lang="ts">
import { RouterView, useRoute, useRouter } from 'vue-router'
const router = useRouter()
const route = useRoute()
function goTo(name: string) {
    router.push({ name })
}
</script>

<template>
    <div class="main-container">
        <header>
            <h1 class="app-title">Tienda de Productos Informáticos</h1>
            <nav class="nav-bar">
                <button class="nav-btn" @click="goTo('home')">Home</button>
                <button class="nav-btn" @click="goTo('marcas')">Marcas</button>
                <button class="nav-btn" @click="goTo('proveedores')">Proveedores</button>
                <button class="nav-btn" @click="goTo('categorias')">Categorías</button>
                <button class="nav-btn" @click="goTo('articulos')">Artículos</button>
            </nav>
        </header>
        <main>
            <RouterView />
        </main>
    </div>
</template>

<style scoped>
.main-container {
    min-height: 100vh;
    background: linear-gradient(135deg, #e0e7ff 0%, #f0f2f5 100%);
    padding-bottom: 2rem;
}

header {
    background: #22223b;
    padding: 1.5rem 0 1rem 0;
    box-shadow: 0 2px 8px rgba(34, 34, 59, 0.08);
    margin-bottom: 2rem;
}

.app-title {
    color: #f2e9e4;
    text-align: center;
    margin: 0 0 1rem 0;
    font-size: 2.2rem;
    letter-spacing: 2px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.nav-bar {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
}

.nav-btn {
    background: #4f8cff;
    color: #fff;
    border: none;
    border-radius: 8px;
    padding: 0.7rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition:
        background 0.2s,
        transform 0.15s;
    box-shadow: 0 2px 6px rgba(79, 140, 255, 0.08);
}
.nav-btn:hover,
.nav-btn:focus {
    background: #2563eb;
    transform: translateY(-2px) scale(1.04);
    outline: none;
}

main {
    max-width: 900px;
    margin: 0 auto;
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 4px 24px rgba(34, 34, 59, 0.07);
    padding: 2.5rem 2rem 2rem 2rem;
    min-height: 400px;
}

@media (max-width: 600px) {
    .main-container {
        padding: 0;
    }
    main {
        padding: 1rem 0.5rem;
    }
    .nav-bar {
        flex-direction: column;
        gap: 0.5rem;
    }
}
</style>
