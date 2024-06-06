<script>
import axios from 'axios'
import WebSocket from 'websocket';

    export default{
        data(){
            return{
                showButton: true,
                selectedOption: [],
                selectedNames: [],
                jsonData: null,
                names: [],
                isOpen: false,
                wsActive: false,
                ws: null,
                receivedData: [],
                isDisplay: false,
                dataDistance: {},
                name_track: null,
            }
        },
        props: {
            jsonId: {
                type: Number,
                required: true,
                default: 0
            }
        },
        mounted(){
            const host = import.meta.env.VITE_APP_HOST
            axios.get(`http://${host}:3000/api/data`)
                .then(response =>{
                    this.jsonData = response.data;
                    this.parseStringToArr(this.jsonData);
                    console.log(this.jsonData)
                })
                .catch(error => {
                    console.error('Ошибка при запросе данных:', error);
                });
        },
        computed: {
            nameSatellite() {
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Спутник: </b>" + this.jsonData[this.jsonId]["satellite_name"];
                } else {
                    return "<b>Спутник: </b> Данные недоступны";
                }
            },
            argPerigee() {
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Аргумент перигея: </b>" + this.jsonData[this.jsonId]["arg_perigee"];
                } else {
                    return "<b>Аргумент перигея: </b> Данные недоступны";
                }
            },
            bStar() {
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Коэффициент торможения: </b>" + this.jsonData[this.jsonId]["bstar"];
                } else {
                    return "<b>Коэффициент торможения: </b> Данные недоступны";
                }
            },
            checkSumLine1(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Контрольная сумма 1: </b>" + this.jsonData[this.jsonId]["checksum"];
                } else {
                    return "<b>Контрольная сумма 1: </b> Данные недоступны";
                }
            },
            checkSumLine2(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Контрольная сумма 2: </b>" + this.jsonData[this.jsonId]["checksum_2"];
                } else {
                    return "<b>Контрольная сумма 2: </b> Данные недоступны";
                }
            },

            classific(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Классификация: </b>" + this.jsonData[this.jsonId]["classification"];
                } else {
                    return "<b>Классификация: </b> Данные недоступны";
                }
            },

            eccentr(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Эксцентриситет: </b>" + this.jsonData[this.jsonId]["eccentricity"];
                } else {
                    return "<b>Эксцентриситет: </b> Данные недоступны";
                }
            },

            numbElementSet(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Номер набора элементов: </b>" + this.jsonData[this.jsonId]["element_set_number"];
                } else {
                    return "<b>Номер набора элементов: </b> Данные недоступны";
                }
            },

            typeEpheremide(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Тип эферемиды (орбитальная модель): </b>" + this.jsonData[this.jsonId]["ephemeris_type"];
                } else {
                    return "<b>Тип эферемиды (орбитальная модель): </b> Данные недоступны";
                }
            },

            epochIs(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Эпоха: </b>" + this.jsonData[this.jsonId]["epoch"];
                } else {
                    return "<b>Эпоха: </b> Данные недоступны";
                }
            },

            epochYear(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Год эпохи: </b>" + this.jsonData[this.jsonId]["epoch_year"];
                } else {
                    return "<b>Год эпохи: </b> Данные недоступны";
                }
            },

            inclin(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Наклонение: </b>" + this.jsonData[this.jsonId]["inclination"];
                } else {
                    return "<b>Наклонение: </b> Данные недоступны";
                }
            },

            numbIss(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Номер ИСЗ спутника в базе данных NORAD: </b>" + this.jsonData[this.jsonId]["iss_number"];
                } else {
                    return "<b>Номер ИСЗ спутника в базе данных NORAD:: </b> Данные недоступны";
                }
            },

            launchFragm(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Фрагмент запуска: </b>" + this.jsonData[this.jsonId]["launch_fragment"];
                } else {
                    return "<b>Фрагмент запуска: </b> Данные недоступны";
                }
            },

            launchNumb(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Номер запуска в году: </b>" + this.jsonData[this.jsonId]["launch_number"];
                } else {
                    return "<b>Номер запуска в году: </b> Данные недоступны";
                }
            },

            launchYear(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Год запуска: </b>" + this.jsonData[this.jsonId]["launch_year"];
                } else {
                    return "<b>Год запуска: </b> Данные недоступны";
                }
            },

            meanAnomal(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Средняя аномалия: </b>" + this.jsonData[this.jsonId]["mean_anomaly"];
                } else {
                    return "<b>Средняя аномалия: </b> Данные недоступны";
                }
            },

            meanMovement(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Среднее движение (оборотов в день): </b>" + this.jsonData[this.jsonId]["mean_motion"];
                } else {
                    return "<b>Среднее движение (оборотов в день): </b> Данные недоступны";
                }
            },

            derivativeFirst(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Первая производная среднего движения по времени: </b>" + this.jsonData[this.jsonId]["mean_motion_derivative"];
                } else {
                    return "<b>Первая производная среднего движения по времени: </b> Данные недоступны";
                }
            },

            derivativeSecond(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Вторая производная среднего движения по времени: </b>" + this.jsonData[this.jsonId]["second_derivative"];
                } else {
                    return "<b>Вторая производная среднего движения по времени: </b> Данные недоступны";
                }
            },

            orbitNumb(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Номер витка: </b>" + this.jsonData[this.jsonId]["orbit_number"];
                } else {
                    return "<b>Номер витка: </b> Данные недоступны";
                }
            },

            rightAscension(){
                if (this.jsonData && this.jsonData[this.jsonId]) {
                    return "<b>Прямое восхождение восходящего узла: </b>" + this.jsonData[this.jsonId]["raan"]
                } else {
                    return "<b>Прямое восхождение восходящего узла: </b> Данные недоступны";
                }
            }

        },
         methods: {        
            hideButton(){
                this.showButton = false
            },
            openSelect(){
                this.isOpen = !this.isOpen
            },
            clearChoice(){
                var checkboxes = document.querySelectorAll('input[type="checkbox"]');
                checkboxes.forEach(function(checkbox) {
                    checkbox.checked = false;
                });
                this.selectedOption = [];
                this.isDisplay = false;
                this.checkboxChange(this.selectedOption);
            },
            parseStringToArr(inputData){
                for (let index = 0; index < inputData.length; index++){
                    const item = inputData[index];
                    this.names.push(item["satellite_name"]);
                }
            },
            formSend(data){
                this.dataDistance = data;
                this.checkboxChange(this.selectedOption);
            },
            checkboxChange(arrIndex){
                this.selectedNames = arrIndex.map(index => {
                    return {
                        name: this.names[index - 1],
                        numberInitial: (index - 1)
                    };
                });
                this.selectedNames.sort((a, b) => (a.name > b.name) ? 1 : -1);
                this.$emit("chooseMass", this.selectedNames);
                this.sendData(this.moveFormatArray(this.selectedNames))
            },
            getNameTrack(name){
                this.name_track = name;
                this.checkboxChange(this.selectedOption);
            },
            moveFormatArray(arrNames){
                let transformedArray = arrNames.map( (element) => {
                    return {
                        satellite_name: element.name,
                        numb_json_data: element.numberInitial,
                        line_1: this.jsonData[element.numberInitial]['line1'],
                        line_2: this.jsonData[element.numberInitial]['line2'],
                        latitude: null,
                        longitude: null,
                        height: null
                    };
                });
                let newObject = {
                    sat_name: this.dataDistance.sat, 
                    longitude: this.dataDistance.long, 
                    latitude: this.dataDistance.lat, 
                    distance: null,
                    track: this.name_track,
                };
                transformedArray.unshift(newObject);
                return transformedArray;
            },      
            sendData(data) {
                let ws;
                if (this.wsActive === true) {
                    this.ws.close();
                }
                const host = import.meta.env.VITE_APP_HOST
                this.ws = new window.WebSocket(`ws://${host}:8765`); 
                this.ws.onopen = function() {
                    this.ws.send(JSON.stringify(data));
                    console.log('Отправлено: ' + JSON.stringify(data))
                }.bind(this); 
                this.ws.onmessage = (event) => {
                    this.receivedData = JSON.parse(event.data);
                    console.log('Получены обработанные данные:');
                    console.log(this.receivedData);

                    this.$emit("getLocation", this.receivedData)
                };
                this.wsActive = true; 
            },
            displayDetailInformation(){
                this.isDisplay = true;
                this.isOpen = false;
            },   
            clearDetailInformation(){
                this.isDisplay = false;
                this.isOpen = true;
            }
    //         selectAll() {
    //     this.selectedOption = Array.from({ length: 1000 }, (_, index) => index + 1);
    //     this.checkboxChange(this.selectedOption);
    // }  
        }
    }
</script>

<template>
    <div className="side_panel_wrapper">
        <h1 className="name_h1">СПУТНИКИ</h1>
        <div className="get_data_wrapper">
            <div className="select_wrapper">
                <button className="button_get_data" @click="openSelect()">
                    <p className="button_text">Выберите спутник</p>
                    <img v-if="!isOpen" src="./icons/arrow.svg" className="img_svg_down" alt="">
                    <img v-else src="./icons/arrow.svg" className="img_svg_up" alt="">
                </button>
                <div v-show="isOpen" className="custom_select">
                    <div className="scrolled_inside_select"> 
                        <div v-for="(el, index) in names" :key="index" >
                            <label> 
                                <input type="checkbox" :value="index+1" v-model="selectedOption" @change="checkboxChange(this.selectedOption)" className="real_checkbox">
                                <span className="custom_checkbox"></span>
                                {{ el }}
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            <img v-show="!isOpen && !isDisplay" className='satellite_img' src="/src/components/icons/Satellite.svg" alt=""> 
            <button v-show="isOpen" className="button_get_data" @click="clearChoice()">
                <p className="button_text" style="margin: 5px">Сбросить</p>
            </button>
            <!-- <button v-show="isOpen" className="button_get_data" @click="selectAll">
                <p className="button_text" style="margin: 5px">Выбрать все</p>
            </button> -->
               <div v-if="isDisplay && !isOpen" className="main_text"> 
                <div className="fixed_up">
                    <div className="fixed_head">
                        <h3>ИНФОРМАЦИЯ О СПУТНИКЕ</h3>
                    </div>
                    <button @click="clearDetailInformation()" className="close_button"></button>
                </div>
                <div className="line"></div>
                <ul className="scrolled">
                    <li v-html="nameSatellite"></li>
                    <li v-html="numbIss"></li>
                    <li v-html="classific"></li>
                    <li v-html="launchYear"></li> 
                    <li v-html="launchNumb"></li> 
                    <li v-html="launchFragm"></li>
                    <li v-html="epochYear"></li>  
                    <li v-html="epochIs"></li>
                    <li v-html="derivativeFirst"></li>
                    <li v-html="derivativeSecond"></li>   
                    <li v-html="bStar"></li>
                    <li v-html="typeEpheremide"></li>
                    <li v-html="numbElementSet"></li>
                    <li v-html="checkSumLine1"></li>
                    <li v-html="inclin"></li>
                    <li v-html="rightAscension"></li>  
                    <li v-html="eccentr"></li>
                    <li v-html= "argPerigee" ></li>
                    <li v-html="meanAnomal"></li>
                    <li v-html="meanMovement"></li> 
                    <li v-html="orbitNumb"></li>  
                    <li v-html="checkSumLine2"></li>
                </ul>
            </div>     
        </div>
    </div>
</template>

<style scoped>

.side_panel_wrapper{
    background: #bbe1ea;
    border-radius: 25px;
    width: 100%;
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

@font-face {
    font-family: 'Berlin Sans' ;
    font-style: bold;
    font-weight: 700;
    src: url('/src/components/Fonts/Berlin_Sans_FB_Demi_Bold.ttf')
}

@font-face {
    font-family: 'Journal Sans' ;
    font-style: Italic;
    font-weight: 400;
    src: url('/src/components/Fonts/JournalSansItalic.ttf')
}

.close_button{
    background: url('./icons/close_side.svg') no-repeat; 
    background-size: cover; 
    width: 30px; 
    height: 30px; 
    border: none;
    padding: 0;
}

.close_button:hover{
    cursor: pointer;
    width: 32px;
    height: 32px;
}

.img_svg_down{
    width: 15px;
}

.img_svg_up{
    width: 15px;
    transform: scaleY(-1);
}

.name_h1{
    font-family: 'Berlin Sans', sans-serif;
    -webkit-text-stroke: 1px black; 
    color: #17364b;
    font-size: 25px;
    margin: 5px;
}

.select_wrapper{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    width: 100%;
}

.custom_select{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;

    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 15px;
    width: 100%;
    max-height: 420px;
}

.scrolled_inside_select{
    margin: 10px 15px;
    height: 100%;
    overflow-y: auto;
    display: grid;
    gap: 7px;
}

.get_data_wrapper{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.button_text{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 18px;
    margin: 10px 5px;
}

.button_get_data{
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;
    padding: 5px 10px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.button_get_data:hover{
    background: #122939;
    box-shadow: 0 4px 4px 2px rgba(0, 0, 0, 0.25);
    cursor: pointer;
}

.button_get_data:focus{
    background: #122939;
    border: 2px solid black;
    box-shadow: 0 4px 4px 2px rgba(0, 0, 0, 0.25);
}

.satellite_img{
    margin-top: 40%;
    width: 60%;
    max-width: 250px;
    transform: scaleY(-1);
    opacity: 0.7;
}

.main_text li{
    font-family: 'Journal Sans', sans-serif;
    font-size: 15px;
    color: #fff;
}

.main_text ul{
    padding-inline-start: 20px;
}

.main_text{
    background: #17364b;
    border: 1px solid #000;
    border-radius: 20px;
    gap: 2px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    height: 500px;
}

.fixed_up{
    z-index: 1; 
    margin: 15px 10px 5px 10px;
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 15px;
    justify-content: center;
}

.fixed_head{
    width: 70%;
}

.fixed_up h3{
    margin: 0;
    font-family: 'Berlin Sans', sans-serif;
    font-size: 18px;
    text-align: center;
    color: #fff;
}

.scrolled{
    height: 100%;
    overflow-y: auto;
    margin: 10px;
    padding: 0px 10px 0 0;
}

::-webkit-scrollbar {
    width: 11px; 
    margin-right: -10px;
}

::-webkit-scrollbar-track {
    background: rgba(217, 217, 217, 0.71);
    border-radius: 25px;
}

::-webkit-scrollbar-thumb {
    background: rgba(24, 27, 32, 0.53);
    border-radius: 25px; 
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.line{
    width: 100%;
    border-top: 6px solid #bbe1ea; 
}

.real_checkbox{
    width: 0;
    height: 0;
    opacity: 0;
    position: absolute;
    z-index: -1;
}

.custom_checkbox{
    position: relative;
    display: inline-block;
    width: 15px;
    height: 15px;
    background: #ffff;
    border: none;
    border-radius: 50%;
    vertical-align: sub;
    margin-right: 5px;
}

.custom_checkbox::before{
    content: '';
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #122939;
    border-radius: 50%;
    background-repeat: no-repeat;
    background-size: contain;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%) scale(0); 

    transition: 0.2s ease-in;
}

.real_checkbox:checked + .custom_checkbox::before{
    transform: translate(-50%, -50%) scale(1); 
}

</style>