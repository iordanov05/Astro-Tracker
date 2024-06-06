<script>
import Header_main from '../components/Header_main.vue'
import Map from '../components/Map.vue'
import Side_panel from '../components/Side_panel.vue'
import Time_stamp from '../components/Time_stamp.vue'
import Footer_inf from '../components/Footer_inf.vue'
import Menu from '../components/Menu.vue'

export default{
    components: {Header_main, Map, Side_panel, Time_stamp, Footer_inf, Menu},
    data(){
        return{
            isMenuOpen: false,
            chooseNamesSelector: [],
            receivedLocation: [],
            jsonId: null, 
            dataDistance: {},
        };
    },
    methods: {
        openMenu(isButtonClick, dataForm){
            this.isMenuOpen = isButtonClick;
            this.$refs.childRef.formSend(dataForm);
            this.$refs.mapref.calculateChosenPoint(dataForm);
        },
        openMenuHeader(isButtonClick){
            this.isMenuOpen = isButtonClick;
        },
        dataToMenu(data){
            this.chooseNamesSelector = data;
        },
        getLocation(data){
            this.receivedLocation = data;
        },
        informationDisplay(id, name){
            this.jsonId = id;
            this.$refs.childRef.getNameTrack(name);
            console.log("Track: ", name)
            this.callChildFunction()
        },
        callChildFunction() {
            this.$refs.childRef.displayDetailInformation();
        }
    }
}

</script>

<template>
    <header className = 'header_header'>
            <Header_main 
                @openMenu="openMenuHeader"
                :receivedDistance="receivedLocation"
            ></Header_main>
    </header>
    <main>
    <div className="main_part">
        <div className="all">
            <Map
                ref="mapref"
                :receivedLocation="receivedLocation" 
                @informationDisplay="informationDisplay"
            ></Map>
            <Time_stamp></Time_stamp>
        </div>
        <Side_panel
            ref="childRef"
            @chooseMass="dataToMenu"
            @getLocation="getLocation"
            :jsonId="jsonId"
        ></Side_panel>
    </div>
    <Menu 
        v-show="isMenuOpen"
        @sendForm="openMenu"
        @closeWindow="openMenuHeader"
        :dataSelector="chooseNamesSelector"
    ></Menu>
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
    padding: 20px;
    position: relative;
    z-index: 1;
}

</style>