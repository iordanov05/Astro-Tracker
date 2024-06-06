<script>
    export default {
        props: {
            item_data: {
                type: Object,
                default: () => ({
                id: null,
                image: '',
                name: '',
                tg: '',
                city: '',
                job: '',
                gh: ''
            })
            }
        }
    }
</script>

<template>
    <div className="dev_wrapper">
        <div className="dev_inside">
            <h1 className="name_h1">{{ item_data.name }}</h1>
            <div className="dev_info">
                <ul className="info_inside">
                    <li className="main_text">Тг: {{ item_data.tg }}</li>
                    <li className="main_text">{{ item_data.city }}</li>
                    <li className="main_text">{{ item_data.job }}</li>
                    <li className="main_text">
                        Ссылка на Github: <br>
                        <a :href="item_data.gh" style="color: #a6c9d0; display: block; margin-top: 10px;">{{ item_data.gh }}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div className="photo_div">
            <img :src="`src/components/icons/${item_data.image}`" className="photo">
        </div>
    </div>
</template>

<style scoped>

p{
    margin: 0;
}

h1{
    margin: 0;
}

li {
    margin-bottom: 35px; 
}

ul{
    margin-bottom: 0;
    margin-top: 20px;
}

a{
    font-family: 'Berlin Sans', sans-serif;
    font-size: 28px;
}

.dev_wrapper{
    background: #bbe1ea;
    border-radius: 25px;
    max-width: 1000px;
    max-height: 500px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    box-shadow: 0 10px 20px 10px #17364b; 
    margin: 5% auto;
    position: relative;
    z-index: 1;
}

.dev_inside{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 20px;
    width: 60%;
    margin-left: 30px;
    margin-top: 50px;
}

.dev_info{
    display: flex;
    flex-direction: column;; 
    background:  #17364b;
    border-radius: 25px;
    width: 100%;
}

.photo{
    max-height: 100%;
}

.photo_div{
    display: flex;
    align-items: flex-end;
    justify-content: center;
    width: 40%;
    margin-right: 10px;
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
    font-size: 35px;
}

.main_text{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: white;
    font-size: 28px;
}

</style>