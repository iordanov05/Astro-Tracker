<script>
    export default{
        data(){
            return{
                longitude: null,
                latitude: null,
                error: false,
                selectedSatellite: null
            };
        },
        props: {
            dataSelector: {
                type: Array,
                required: true
            }
        },
        methods: {
            checkSendForm(){
                this.error = true;
                if (this.longitude.trim() !== '' && this.latitude.trim() !== '' && !isNaN(this.latitude) && !isNaN(this.longitude)){
                    if ( (this.latitude >= -90 && this.latitude <= 90) && (this.longitude >= -180 && this.longitude <= 180) ){
                        if (this.selectedSatellite !== null && this.selectedSatellite !== -1 ){
                            this.error = false;
                        }
                    }
                };
                if (!this.error){
                    const dataForm = {
                        lat: this.latitude,
                        long: this.longitude,
                        sat: this.dataSelector[this.selectedSatellite-1].name
                    }
                    this.$emit("sendForm", false, dataForm);
                    this.latitude = null;
                    this.longitude = null;
                };
                console.log(this.error);
            },
            closeWindow(){
                this.$emit("closeWindow", false);
            }
        }
    }
</script>

<template>
    <div className="menu_wrapper">
        <button @click="closeWindow()" className="close_button"></button>
        <h3 className="h_3">Рассчитать расстояние</h3>
        <label className="name">
            Долгота:
            <input v-model="longitude" className="input_wrapper" type="text" required title="Долгота должна быть от -180 до 180 градусов" placeholder="37.4098">
        </label>
        <label className="name">
            Широта:
            <input v-model="latitude" className="input_wrapper" type="text" required title="Широта должна быть от -90 до 90 градусов" placeholder="55.80339">
        </label>
        <div className="selector_wrapper">
            <select v-model="selectedSatellite" className="custom_select">
                <option :value="null" selected>Выберите спутник</option>
                <option v-for="(el, index) in dataSelector" :key="index" :value="index+1">{{ el.name }}</option>
            </select>
        </div>
        <p v-show="error" className="show_error">Заполните поля корректно!</p>
        <div className="button_location">
            <button @click="checkSendForm()" className="button_get_data">
                <p className="button_text">Готово</p>
            </button>
        </div>
    </div>
</template>

<style scoped>

.close_button{
    background: url('./icons/close.svg') no-repeat; 
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

.h_3{
    font-family: 'Berlin Sans', sans-serif;
    -webkit-text-stroke: 1px black; 
    color: #17364b;
    font-size: 25px;
    margin: 0;
}

.menu_wrapper{
    background: #bbe1ea;
    margin: auto;
    position: absolute;
    z-index: 2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 15px 20px; 
    border-radius: 15px;
    box-shadow: 0 0 1000px rgba(0, 0, 0, 1);
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

.name{
    margin: 5px;
    font-family: 'Berlin Sans', sans-serif;
    -webkit-text-stroke: 1px black; 
    color: #17364b;
    font-size: 18px;
    margin: 5px;
    letter-spacing: 2px;
}

.input_wrapper{
    border: none;
    border-radius: 20px;
    background: rgb(155, 186, 193);
    padding: 5px 10px;
    font-family: 'Berlin Sans', sans-serif;
    font-style: normal;
    color: #fff;
    -webkit-text-stroke: initial;
    font-size: 20px;
}

input:focus {
    outline: none; 
}

.button_location{
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 100%;
    margin-right: 10%;
}

.button_text{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 15px;
    margin: 4px 7px;
}

.button_get_data{
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;
    padding: 5px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
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

::placeholder{
    color: rgba(29, 60, 81, 0.3);
    -webkit-text-stroke: initial;
}

.selector_wrapper{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    width: 80%;
}

.custom_select{
    display: flex;
    padding: 10px; 
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;

    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #fff;
    font-size: 18px;
}

.show_error{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #17364b;
    font-size: 18px;
    margin: 10px 0 0 0;
}


::-webkit-scrollbar {
    width: 11px; 
    margin-right: 100px;
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

</style>