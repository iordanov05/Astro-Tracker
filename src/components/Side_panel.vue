<template>
    <div className="side_panel_wrapper">
        <h1 className="name_h1">СПУТНИКИ</h1>
        <div className="get_data_wrapper">
            <div className="select_wrapper" >
                <select className="custom_select" name="" id="">
                    <option disabled selected hidden>Выберите спутник</option>
                    <option value="">1</option>
                </select>  
            </div>
            <button className="button_get_data button_text">Нажмите для получения данных</button>
            <img className='satellite_img' src="/src/components/icons/Satellite.svg" alt=""> 
        </div>
    </div>

</template>

<style scoped>

.side_panel_wrapper{
    background: #bbe1ea;
    border-radius: 25px;
    width: 100%;
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

</style>