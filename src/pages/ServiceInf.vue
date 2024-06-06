<script>
import Header_extra from '../components/Header_extra.vue'
import Footer_inf from '../components/Footer_inf.vue'

export default{
    components: {Header_extra, Footer_inf},
}
</script>

<template>
    <header className = 'header_header'>
        <Header_extra></Header_extra>
    </header>
    <main>
        <div className="wrapper">
            <div className="back_img"></div>
            <p className="text">Добро пожаловать в наше приложение для отслеживания спутников в реальном времени! Ниже представлена подробная инструкция о том, как пользоваться функционалом нашего сайта.
            </p>
            <div className="text_center">
                <h1 className="head">Начало работы</h1>
            </div>
            <p className="text"> Переход на сайт - Для начала необходимо перейти на наш сайт по ссылке. По прибытии на главную страницу вы увидите интерактивную карту и панель для выбора спутников.
            </p>
            <div className="text_center">
                <h1 className="head">Использование интерактивной карты</h1>
            </div>
            <ol>
                <li>Выбор региона</li>
                <p className="text_2">- Наведение на любой континент на карте приведет к подсветке региона и отображению его названия.</p>
                <li>Отображение спутников</li>
                <p className="text_2">- Для увидения расположения спутников в реальном времени, откройте раскрывающийся список в боковой панели и выберите интересующие вас спутники. Они автоматически появятся на карте.</p>
                <li>Информация о спутнике</li>
                <p className="text_2">- При наведении на спутник появится краткая информация: имя спутника, текущие координаты и высота, на которой он находится.</p>
                <li> Получение подробной информации</li>
                <p className="text_2">- Чтобы получить полное описание спутника, нажмите на него. Полная информация отобразится в боковой панели.</p>
                <li>Удаление спутников с карты</li>
                <p className="text_2">- Для удаления всех спутников с карты нажмите кнопку "Сбросить".</p>
            </ol>
            <div className="text_center">
                <h1 className="head">Расчет расстояния</h1>
            </div>
            <ol>
                <li>Рассчет расстояния</li>
                <p className="text_2">- Нажмите кнопку "Рассчитать расстояние" в верхней части сайта. В появившемся окошке введите свои координаты и выберите спутник из списка.</p>
                <li>Отображение расстояния</li>
                <p className="text_2"> - Нажмите кнопку "Рассчитать расстояние" в верхней части сайта. В появившемся окошке введите свои координаты и выберите спутник из списка.</p>
            </ol>
            <div className="text_center">
                <h1 className="head">Дополнительная функциональность</h1>
            </div>
            <ol>
                <li>Информация о разработчиках</li>
                <p className="text_2"> - Для просмотра информации о разработчиках сайта нажмите на кнопку "Контакты" в нижней части страницы.</p>
                <li>Возврат на главную страницу</li>
                <p className="text_2"> - Нажмите на логотип приложения в левом верхнем углу, чтобы вернуться на главную страницу.</p>
            </ol>
            <p className="text">
                Пользуйтесь нашим приложением с комфортом и уверенностью. Если у вас есть дополнительные вопросы, обратитесь к разделу Часто Задаваемых Вопросов ниже.
            </p>
            <div className="text_center">
                <h1 className="head">Часто Задаваемые Вопросы (FAQ)</h1>
            </div>
            <ol>
                <li>Как часто обновляются данные о спутниках?</li>
                <p className="text_2"> - Данные о спутниках обновляются каждые 5 секунд для обеспечения актуальной информации.</p>
                <li>Как узнать высоту, на которой находится спутник?</li>
                <p className="text_2"> - При наведении на спутник на карте вы увидите его текущие координаты и высоту.</p>
                <li>Как удалить все спутники с карты?</li>
                <p className="text_2"> - Для удаления всех спутников с карты нажмите кнопку "Сбросить" в боковой панели.</p>
                <li>Как рассчитать расстояние до спутника?</li>
                <p className="text_2"> - Нажмите кнопку "Рассчитать расстояние" в верхней части сайта.</p>
            </ol>
            <p className="text" style="margin: 20px 0 20px 0;">Выбирая интересующие спутники из раскрывающегося списка и используя функцию расчёта расстояния, вы сможете эффективно отслеживать и получать информацию о спутниках в реальном времени. Если у вас возникнут дополнительные вопросы, не стесняйтесь обращаться к разделу "Часто Задаваемые Вопросы" или связывайтесь с нами через раздел "Контакты".
            </p>
        </div>
    </main>
    <footer>
        <Footer_inf></Footer_inf>
    </footer>
</template>

<style scoped>
.header_header{
    box-shadow: 0 4px 10px 15px rgba(0, 0, 0, 0.35);
    background: #17364b;
    padding: 15px 20px 7px 35px
}

.wrapper{
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    gap: 20px;
}
/* .back_img{
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
} */

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

.text{
    text-align: center; 
    color: #fff; 
    font-family: 'Journal Sans', sans-serif; 
    font-style: italic;
    font-size: 25px;
}

.text_2{
    font-family: 'Berlin Sans', sans-serif;
    font-style: normal;
    font-size: 20px;
    color:#fff
}

.text_center{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}

p{
    margin: 0;
}

ol{
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
}

li{
    color: #fff; 
    font-family: 'Journal Sans', sans-serif; 
    font-style: italic;
    font-size: 20px;
    margin: 20px 0 10px 0 ;
}

.head{
    font-family: 'Berlin Sans', sans-serif;
    font-style: normal;
    font-size: 25px;
    margin: 0;
    color:#fff
}

</style>
