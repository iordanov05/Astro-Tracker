<script>
import Header_main from './components/Header_main.vue';

export default{
    components: {Header_main}
}

</script>

<template>
    <header className = 'header_header'>
            <Header_main></Header_main>
    </header>
    <main>
        
    </main>
</template>

<style scoped>
.header_header{
    box-shadow: 0 4px 10px 15px rgba(0, 0, 0, 0.35);
    background: #17364b;
    padding: 15px 20px 7px 35px
}
</style>