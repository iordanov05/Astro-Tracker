<template>
    <div className="time_rectangle">
        <p class= "name_time">2024-12-02 21:14:00 (UTC +3:00)</p>
    </div>
</template>

<style scoped>

.time_rectangle{
    box-shadow: 0 4px 4px 5px rgba(0, 0, 0, 0.25);
    background: #bbe1ea;
    border-radius: 15px;
    padding: 7px 10px;
    max-width: 300px;
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