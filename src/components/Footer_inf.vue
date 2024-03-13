<template>
    <div className="footer_main">
        <div className="tech_support">
            <div className="footer_mail">
                <a href="mailto:dnvorontsova@edu.hse.ru" style="color: #a6c9d0">dnvorontsova@edu.hse.ru</a>
                <a href="mailto:paiordanov@edu.hse.ru" style="color: #a6c9d0">paiordanov@edu.hse.ru</a>
            </div>
            <p>Техническая поддержка</p>
        </div>
        <p className="name_project">Astro Tracker</p>
         <div className="footer_information">
            <p>О сервисе</p>
            <p>Контакты</p>
            <p>Политика конфиденциальности</p>
        </div>
    </div>
</template>

<style scoped>  
    
.footer_main{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 5px;
    padding: 15px 50px 10px 50px;
    margin-top: 20px;
    box-shadow: 0 10px 20px 10px #17364b; 
}

.tech_support{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
}

.tech_support p{
    font-family: 'Journal Sans', sans-serif;
    font-style:  normal;
    font-size: 15px;
    color: #17364b;
    margin: 0;
}

.footer_information{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 50px;
}

.footer_mail{
    display: flex;
    flex-direction: row;
    gap: 20px;
    font-family: 'Berlin Sans', sans-serif;
    font-size: 15px;
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

.footer_information p{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: #bbe1ea;
    font-size: 15px;
    margin: 0;
}

.name_project{
    font-family: 'Berlin Sans', sans-serif;
    font-style: bold;
    font-size: 30px;
    margin: 0;
    letter-spacing: 10px;
    color: rgba(166, 201, 208, 0.4);
}
</style>