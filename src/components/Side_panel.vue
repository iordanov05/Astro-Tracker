<template>
    <div className="side_panel_wrapper">
        <h1 className="name_h1">СПУТНИКИ</h1>
        <div style="width: 100%;">
            <div class="select_wrapper" >
                <select class="custom_select" name="" id="">
                    <option disabled selected hidden>Выберите спутник</option>
                    <option value="">1</option>
                </select>  
            </div>

        </div>
    </div>

</template>

<style scoped>

.side_panel_wrapper{
    background: #bbe1ea;
    border-radius: 25px;
    width: 100%;
    padding: 20px 10px;
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

.name_h1{
    font-family: 'Berlin Sans', sans-serif;
    -webkit-text-stroke: 1px black; 
    color: #17364b;
    font-size: 30px;
}

.select_wrapper{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    align-self: stretch;
}
.custom_select{
    display: flex;
    padding: 15px 10px; 
    justify-content: space-between;
    align-items: center;
    align-self: stretch;

    border: 1px solid #000;
    border-radius: 20px;
    background: #17364b;
}
</style>