<script>
    export default{
        methods: {
            buttonClick(){
                this.$emit("openMenu", true);
            }
        }
    }
</script>

<template>
<div className = "header_wrapper">
    <div className="header_wrapper_inside">
        <RouterLink to="/">
            <img src=".\icons\icon.png" alt="">
        </RouterLink>
        <h1 className="nameApp_h1">HSE&MIEM ASTRO TRACKER</h1>
    </div>
</div> 
</template>

<style scoped>

img{
    width: 50px;
    height: 50px;
}

.reload_button{
    background: url('./icons/reload.svg') no-repeat; 
    background-size: cover; 
    width: 35px; 
    height: 35px; 
    border: none;
}

.reload_button:hover{
    cursor: pointer; 
    box-shadow: 0 0 6px 10px rgba(0, 0, 0, 0.25);
}

.distance{
    display: flex;
    flex-direction: row;
    gap: 20px;
    width: 35%;
}

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
</style>