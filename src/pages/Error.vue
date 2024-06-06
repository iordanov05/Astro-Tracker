<template>
    <div className="wrapper">
        <div className="back_img" ></div>
        <div className="svg_div">
            <img style="transform: scaleY(-1);" src="../components/icons/Satellite_white.svg" alt="">
        </div>
        <div className="text">
            <h1>404</h1>
            <p>Похоже, вы потерялись в космосе...</p>
        </div>
</div>

</template>

<style scoped>

.back_img{
    width: 100%;
    height: 100%;
    background-image: url('../components/icons/kosmos.jpg') ;
    background-size: cover; 
    background-position: center center;
    background-repeat: no-repeat;
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0.4;
    z-index: -1;
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

.wrapper{
    width: 100%; 
    height: 100vh; 
    display: flex; 
    flex-direction: column; 
    justify-content: center; 
    align-items: center; 
    position: relative;
    gap: 10px;
}

.svg_div{
    position: relative;
    z-index: 1;
}

img{
    width: 150px;
}

h1{
    font-family: 'Berlin Sans', sans-serif;
    font-style: normal;
    font-size: 130px;
    margin: 0;
}

p{
    font-size: 35px;
    margin: 0;
}

.text{
    text-align: center; 
    color: #fff; 
    font-family: 'Journal Sans', sans-serif; 
    font-style: italic;
    position: relative; 
    z-index: 1;
}

</style>