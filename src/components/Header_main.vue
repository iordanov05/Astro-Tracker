<template>
<div className = "header_wrapper">
    <div className="header_wrapper_inside">
        <img src=".\icons\hse_logo.png" alt="">
         <h1 className="nameApp_h1">HSE&MIEM ASTRO TRACKER</h1>
    </div>
    <h1 className="inf_h1">Расстояние до МИЭМа: XXXXXX км</h1>
</div> 
</template>

<style scoped>
h1{
    margin: 0;
}
.header_wrapper{
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.header_wrapper_inside{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 20px;
}
@font-face {
    font-family: 'Berlin Sans' ;
    font-style: bold;
    font-weight: 700;
    src: url('/src/components/Fonts/Berlin_Sans_FB_Demi_Bold.ttf')
}
@font-face{
    font-family: 'Journal Sans';
    font-style: bold;
    font-weight: 700;
    src: url('/src/components/Fonts/Journal_SansSerif.tff') 
}
.nameApp_h1{
    font-family: 'Berlin Sans', sans-serif;
    color: #FFFF;
    font-size: 34px;
}
.inf_h1{
    font-family: 'Journal Sans', sans-serif;
    color:#FFFF;
    font-size: 28px;
}
</style>