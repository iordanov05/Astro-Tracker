<script>
export  default{
    data() {
        return {
             currentDate: new Date().toLocaleDateString(),
        }
  },
    created(){
        setInterval(() => {
            this.currentDate = new Date().toLocaleDateString;
        }, 86400000);
    }
}
</script>

<template>
    <div className="time_rectangle">
        <p class= "name_time">Обновлено: {{ currentDate }} 14:00:00 (UTC +3:00)</p>
    </div>
</template>

<style scoped>

.time_rectangle{
    box-shadow: 0 4px 4px 5px rgba(0, 0, 0, 0.25);
    background: #bbe1ea;
    border-radius: 15px;
    padding: 7px 10px;
    max-width: 450px;
    margin: 0;
}

@font-face{
    font-family: 'Journal Sans' ;
    font-style: Italic;
    font-weight: 400;
    src: url('/src/components/Fonts/JournalSansItalic.ttf')
}

.name_time{
    font-family: 'Journal Sans', sans-serif;
    font-style: italic;
    color: black;
    font-size: 20px;
    margin: 0;
}

</style>