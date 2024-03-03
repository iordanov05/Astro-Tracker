<script>
import Header_main from './components/Header_main.vue'
import Map from './components/Map.vue'
import Side_panel from './components/Side_panel.vue'

export default{
    components: {Header_main, Map, Side_panel}
}

</script>

<template>
    <header className = 'header_header'>
            <Header_main></Header_main>
    </header>
    <main>
        <div className="main_part">
            <Map></Map>
            <Side_panel></Side_panel>
        </div>
        
    </main>
    <footer>

    </footer>
</template>

<style scoped>
.header_header{
    box-shadow: 0 4px 10px 15px rgba(0, 0, 0, 0.35);
    background: #17364b;
    padding: 15px 20px 7px 35px
}
.main_part{
    display: flex;
    flex-direction: row;
    gap: 10px;
    padding: 20px;
}
</style>