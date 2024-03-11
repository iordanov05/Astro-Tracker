<script>
import axios from 'axios'

    export default{
        data(){
            return{
                showButton: true,
                selectedOption: '',
                jsonData: null,
                names: []
            }
        },
        mounted(){
                axios.get('/src/test_1.json')
                .then(response =>{
                    this.jsonData = response.data;
                    this.parseStringToArr(this.jsonData);
                });
        },
        computed: {
            argPerigee(){
                return "<b>Аргумент перигея: </b>" + this.jsonData[this.selectedOption - 1]["arg_perigee"];
            },
            bStar(){
                return "<b>Коэффицент торможения: </b>" + this.jsonData[this.selectedOption - 1]["bstar"];
            },
            checkSumLine1(){
                return "<b>Контрольная сумма 1: </b>" + this.jsonData[this.selectedOption - 1]["checksum"];
            },
            checkSumLine2(){
                return "<b>Контрольная сумма 2: </b>" + this.jsonData[this.selectedOption - 1]["checksum_2"];
            },
            classific(){
                return "<b>Классификация: </b>" + this.jsonData[this.selectedOption - 1]["classification"];
            },
            eccentr(){
                return "<b>Эксцентриситет: </b>" + this.jsonData[this.selectedOption - 1]["eccentricity"];
            },
            numbElementSet(){
                return "<b>Номер набора элементов: </b>" + this.jsonData[this.selectedOption - 1]["element_set_number"];
            },
            typeEpheremide(){
                return "<b>Тип эферемиды (орбитальная модель): </b>" + this.jsonData[this.selectedOption - 1]["ephemeris_type"];
            },
            epochIs(){
                return "<b>Эпоха: </b>" + this.jsonData[this.selectedOption - 1]["epoch"];
            },
            epochYear(){
                return "<b>Год эпохи: </b>" + this.jsonData[this.selectedOption - 1]["epoch_year"];
            },
            inclin(){
                return "<b>Наклонение: </b>" + this.jsonData[this.selectedOption - 1]["inclination"];
            },
            numbIss(){
                return "<b>Номер ИСЗ спутника в базе данных NORAD: </b>" + this.jsonData[this.selectedOption - 1]["iss_number"];
            },
            launchFragm(){
                return "<b>Фрагмент запуска: </b>" + this.jsonData[this.selectedOption - 1]["launch_fragment"];
            },
            launchNumb(){
                return "<b>Номер запуска в году: </b>" + this.jsonData[this.selectedOption - 1]["launch_number"];
            },
            launchYear(){
                return "<b>Год запуска: </b>" + this.jsonData[this.selectedOption - 1]["launch_year"];
            },
            meanAnomal(){
                return "<b>Средняя аномалия: </b>" + this.jsonData[this.selectedOption - 1]["mean_anomaly"];
            },
            meanMovement(){
                return "<b>Среднее движение (оборотов в день): </b>" + this.jsonData[this.selectedOption - 1]["mean_motion"];
            },
            derivativeFirst(){
                return "<b>Первая производная среднего движения по времени: </b>" + this.jsonData[this.selectedOption - 1]["mean_motion_derivative"];
            },
            derivativeSecond(){
                return "<b>Вторая производная среднего движения по времени: </b>" + this.jsonData[this.selectedOption - 1]["second_derivative"];
            },
            orbitNumb(){
                return "<b>Номер витка: </b>" + this.jsonData[this.selectedOption - 1]["orbit_number"];
            },
            rightAscension(){
                return "<b>Прямое восхождение восходящего узла: </b>" + this.jsonData[this.selectedOption-1]["raan"]
            }
        },
         methods: {
            hideButton(){
                this.showButton = false
            },
            parseStringToArr(inputData){
                for (let index = 0; index < inputData.length; index++){
                    const item = inputData[index];
                    this.names.push(item["satellite_name"]);
                }
            }
        },
    }
</script>

<template>
    <div className="side_panel_wrapper">
        <h1 className="name_h1">СПУТНИКИ</h1>
        <div className="get_data_wrapper">
            <div className="select_wrapper" >
                <select v-model="selectedOption" className="custom_select" name="" id="">
                    <option disabled value="">Выберите спутник</option>
                    <option v-for="(el, index) in names" :key="index" :value="index+1">{{ el }}</option>
                </select>  
            </div>
            <button 
                v-if="selectedOption != ''"
                v-show="showButton" @click="hideButton()"
                className="button_get_data button_text">
                Нажмите для получения данных
            </button>
            <button disabled v-else className="button_get_data button_text">Нажмите для получения данных</button>
            <img v-if="showButton" className='satellite_img' src="/src/components/icons/Satellite.svg" alt=""> 
            <div v-if="selectedOption!='' && !showButton" className="main_text">
                <div className="fixed_up">
                    <h3>ИНФОРМАЦИЯ О СПУТНИКЕ</h3>
                </div>
                <div className="line"></div>
                <ul className="scrolled">
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
    width: 80%;
    padding: 10px 15px;
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

.name_h1{
    font-family: 'Berlin Sans', sans-serif;
    -webkit-text-stroke: 1px black; 
    color: #17364b;
    font-size: 25px;
}

.select_wrapper{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    align-self: stretch;
}

.button_text{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 18px;
}

.custom_select{
    display: flex;
    padding: 10px 5px; 
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;

    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 20px;
}

.get_data_wrapper{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.button_get_data{
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;
    padding: 5px 10px;
    width: 100%;
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
    height: 420px;
}

.fixed_up{
    z-index: 1; 
    margin: 10px 20px;
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
</style>