<script>
import SwiperCore from 'swiper/core';
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination'
import { Navigation} from 'swiper/modules';
import { Pagination } from 'swiper/modules'

SwiperCore.use([Navigation, Pagination]); 

import Header_extra from '../components/Header_extra.vue'
import ContactsItem from '../components/Contacts-item.vue'
import Footer_inf from '../components/Footer_inf.vue'

export default{
    components: {Header_extra, ContactsItem, Footer_inf, Swiper, SwiperSlide},
    data(){
        return{
            personalInfo: [
            {
                id: 0,
                image: '0.png',
                name: 'Воронцова Дарья',
                tg:'@darya_vorontsova',
                city: 'Город: Москва',
                job: 'Front-end разработчик',
                gh: 'https://github.com/DaryaVorontsova'
            },
            {
                id: 1,
                image: '1.png',
                name: 'Иорданов Павел',
                tg: '@Warymor',
                city: 'Город: Москва',
                job: 'Back-end разработчик',
                gh: 'https://github.com/iordanov05'
            }
            ],  
        }
    }       
}
</script>

<template>
    <header className = 'header_header'>
        <Header_extra></Header_extra>
    </header>
    <main>
        <div className="back_img" ></div>
        <Swiper 
            loop
            :slides-per-view="1"
            :space-between="50"
            navigation
            :pagination="{ clickable: true }"
        >        
            <SwiperSlide v-for="item in personalInfo" :key="item.id">
                    <ContactsItem :item_data="item" />
            </SwiperSlide>
        </Swiper>
    </main>
    <footer> 
        <Footer_inf></Footer_inf>
    </footer>
</template>

<style scoped> 

main{
    position: relative;
}

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
    opacity: 0.3;
    z-index: -1;
}

.header_header{
    box-shadow: 0 4px 10px 15px rgba(0, 0, 0, 0.35);
    background: #17364b;
    padding: 15px 20px 7px 35px
}
</style>
