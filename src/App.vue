<script>
import Header_main from './components/Header_main.vue'
import Map from './components/Map.vue'
import Side_panel from './components/Side_panel.vue'
import Time_stamp from './components/Time_stamp.vue'
import Footer_inf from './components/Footer_inf.vue'

export default{
    components: {Header_main, Map, Side_panel, Time_stamp, Footer_inf}
}

</script>

<template>
    <header className = 'header_header'>
            <Header_main></Header_main>
    </header>
    <main>
        <div className="main_part">
            <div className="all">
                <Map></Map>
                <Time_stamp></Time_stamp>
            </div>
            <Side_panel></Side_panel>
        </div>
    </main>
    <footer>
        <Footer_inf></Footer_inf>
    </footer>
</template>

<style scoped>

.header_header{
    box-shadow: 0 4px 10px 15px rgba(0, 0, 0, 0.35);
    background: #17364b;
    padding: 15px 20px 7px 35px
}

.all{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.main_part{
    display: flex;
    flex-direction: row;
    gap: 20px;
    padding: 20px
}

</style>